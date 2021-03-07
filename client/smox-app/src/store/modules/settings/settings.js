import { SET_APPEARANCE, UPDATE_DATABASE_CONNECTION, READ_DATABASE_CONNECTION } from './mutation_types';
import { readDatabaseConnection } from "src/api/settings";

const state = () => (
{
    appearance: 
    {
        dark_mode: false
    },
    db: {}
});

const getters = {}

const actions = {
    async [READ_DATABASE_CONNECTION] (context)
    {
        let db = await readDatabaseConnection();
        if (db != null)
            context.commit(READ_DATABASE_CONNECTION, db);

    },
    [SET_APPEARANCE] (context, appearance)
    {
        context.commit(SET_APPEARANCE, appearance);
    },
    [UPDATE_DATABASE_CONNECTION] (context, db)
    {
        context.commit(UPDATE_DATABASE_CONNECTION, db);
    }
}

const mutations = {
    [READ_DATABASE_CONNECTION](state, db)
    {
        state.db = db;
    },
    [SET_APPEARANCE] (state, appearance)
    {
        state.appearance = appearance;
    },
    [UPDATE_DATABASE_CONNECTION] (state, db)
    {
        state.db = db;
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}