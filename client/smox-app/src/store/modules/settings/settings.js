import { SET_APPEARANCE } from './mutation_types';

const state = () => (
{
    appearance: 
    {
        dark_mode: false
    }
});

const getters = {}

const actions = {
    [SET_APPEARANCE] (context, appearance)
    {
        context.commit(SET_APPEARANCE, appearance);
    }
}

const mutations = {
    [SET_APPEARANCE] (state, appearance)
    {
        
        state.appearance = appearance
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}