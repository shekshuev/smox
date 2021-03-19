import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
import os

class XGBModel:

    def __init__(self):
        pass

    # аппроксимация натуральным логарифмом
    def __ln_coefs(self, x, y):
        if len(y) < 1:
            return np.zeros(2)
        coefs = np.polyfit(np.log(x), y, 1)
        return coefs

    # значения логарифмической функции
    def __ln_val(self, x, coefs):
        a = coefs[0]
        b = coefs[1] if len(coefs) > 1 else 0
        return [ a * np.log(xi) + b for xi in x ]

    # производная натурального логарифма
    def __ln_dx(self, x, coefs):
        return [ coefs[0] / xi for xi in x ]

    # убираем пропуски в данных и выравниваем просмотры, чтобы они были
    # в строго возрастающем порядке, иначе не сработают сплайны
    def __prepare_data(self, groups):
        groups.sort(key=lambda g: len(g))
        groups = [g for g in groups if len(g) >= 25]
        groups = [group[1:25] for group in groups]
        for i in range(0, len(groups)):
            groups[i] = groups[i].fillna(0)
        for i in range(0, len(groups)):
            for j in range(1, len(groups[i])):
                val = groups[i].loc[groups[i].index[j], "views"] - groups[i].loc[groups[i].index[j-1], "views"]
                if val <= 0:
                    groups[i].loc[groups[i].index[j], "views"] = groups[i].loc[groups[i].index[j], "views"] + abs(val) + 1
        return groups

    def __convert_data(self, data):
        data = data.groupby("id")
        groups = [data.get_group(x) for x in data.groups]
        posts_count = len(groups)
        groups = self.__prepare_data(groups)
        if len(groups) == 0:
            return None
        rows = []
        for _, group in enumerate(groups):
            x = np.arange(1, len(group) + 1)
            last = group.iloc[len(group) - 1]
            # первичные показатели
            row = [ last["id"], last["comments"], last["likes"], last["views"], last["reposts"] ]
            # далее производные показатели
            # аппроксимация функций изменения комментариев, лайков и просмотров от времени натуральным логарифмом
            coefs_comments = self.__ln_coefs(x, group["comments"])
            coefs_likes = self.__ln_coefs(x, group["likes"])
            coefs_views = self.__ln_coefs(x, group["views"])
            x = range(60, 1020, 30)
            # значения аппроксимированной функций изменения комментариев, лайков и просмотров от времени натуральным логарифмом
            row.extend(self.__ln_val(x, coefs_comments))
            row.extend(self.__ln_val(x, coefs_likes))
            row.extend(self.__ln_val(x, coefs_views))
            # значения производной аппроксимированной функции изменения комментариев, лайков и просмотров от времени натуральным логарифмом
            row.extend(self.__ln_dx(x, coefs_comments))
            row.extend(self.__ln_dx(x, coefs_likes))
            row.extend(self.__ln_dx(x, coefs_views))
            rows.append(row) 
        converted = pd.DataFrame(rows)
        converted = converted.rename(columns={ 0: "id" })
        scaler = StandardScaler()
        X = scaler.fit_transform(converted.drop(columns=["id"]))
        return X, converted.drop(columns=range(1, len(converted.columns), 1)), posts_count

    def predict(self, data):
        X, posts, posts_count = self.__convert_data(data)
        if posts_count == 0 or X is None:
            return None
        X = xgb.DMatrix(X)
        model = xgb.Booster() 
        model.load_model(os.path.join(os.path.dirname(__file__), "trained_xgb.json"))
        y_pred = model.predict(X)
        posts["value"] = y_pred
        unique, counts = np.unique(y_pred, return_counts=True)
        results = dict(zip(unique, counts))
        total = 0
        pos = 0
        for i in [0, 1]:
            if i in results.keys():
                total += results[i]
                if i == 1:
                    pos += results[i]
        if total == 0:
            return None
        return {
            "value": pos / total,
            "posts": posts
        }