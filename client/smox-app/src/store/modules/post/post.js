import { SET_OPTIONS, SET_START_DATE, SET_END_DATE } from "./mutation_types";

const state = () => (
{
    options: null,
    startDate: new Date(),
    endDate: new Date()
});

const getters = {}

const actions = {
    [SET_OPTIONS] (context, options)
    {
        context.commit(SET_OPTIONS, options);
    },
    [SET_START_DATE] (context, date)
    {
        context.commit(SET_START_DATE, date);
    },
    [SET_END_DATE] (context, date)
    {
        context.commit(SET_END_DATE, date);
    }
}

const mutations = {
    [SET_OPTIONS] (state, options)
    {
        state.options = options
    },
    [SET_START_DATE] (state, date)
    {
        state.startDate = date
    },
    [SET_END_DATE] (state, date)
    {
        state.endDate = date
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}