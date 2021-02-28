import Vue from "vue";
import Vuex from "vuex";
import accessProfile from "src/store/modules/access_profile/access_profile";
import source from "src/store/modules/source/source";
import task from "src/store/modules/task/task";
import post from "src/store/modules/post/post";
import target from "src/store/modules/target/target";
import settings from "src/store/modules/settings/settings";

Vue.use(Vuex);

const debug = process.env.NODE_ENV !== "production";

const store = new Vuex.Store(
{
    mutations: {
        initialiseStore(state) 
        {
            if (localStorage.getItem('options')) 
            {
				state.post.options = JSON.parse(localStorage.getItem('options'))
            }
            if (localStorage.getItem('startDate')) 
            { 
				state.post.startDate = new Date(localStorage.getItem('startDate'));
            }
            if (localStorage.getItem('endDate')) 
            {
				state.post.endDate = new Date(localStorage.getItem('endDate'));
			}
            if (localStorage.getItem('appearance'))
            {
                state.settings.appearance = JSON.parse(localStorage.getItem('appearance'));
            }
		}
	},
    modules: 
    {
        accessProfile,
        source,
        task,
        post,
        target,
        settings
    },
    strict: debug
});
store.subscribe((mutation, state) => 
{
    localStorage.setItem('options', JSON.stringify(state.post.options));
    localStorage.setItem('startDate', state.post.startDate);
    localStorage.setItem('endDate', state.post.endDate);
    localStorage.setItem('appearance', JSON.stringify(state.settings.appearance));
});

export default store;