import { LOAD_SOURCES, ADD_SOURCE, UPDATE_SOURCE, DELETE_SOURCE } from "./mutation_types";
import { getSources } from "application/api/source";

const state = () => (
{
    sources: []
});

const getters = {}

const actions = {
    async [LOAD_SOURCES] (context)
    {
        let sources = await getSources();
        if (sources != null)
            context.commit(LOAD_SOURCES, sources);

    },
    [ADD_SOURCE] (context, source)
    {
        context.commit(ADD_SOURCE, source);
    },
    [DELETE_SOURCE] (context, source)
    {
        context.commit(DELETE_SOURCE, source);
    }
}

const mutations = {
    [LOAD_SOURCES](state, sources)
    {
        state.sources = sources;
    },
    [ADD_SOURCE] (state, source)
    {
        state.sources.push(source);
    },
    [UPDATE_SOURCE] (state, source)
    {

    },
    [DELETE_SOURCE] (state, source)
    {
        let tmp = state.sources.find(s => s.id == source.id);
        if (tmp != null) 
        {
            let index = state.sources.indexOf(tmp);
            if (index != null)
                state.sources.splice(index, 1);
        }
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}