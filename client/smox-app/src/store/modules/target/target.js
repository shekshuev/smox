import { READ_TARGETS, DELETE_TARGET, CREATE_TARGET } from "./mutation_types";
import { readTargets } from "src/api/target";

const state = () => (
{
    targets: []
});

const getters = {}

const actions = {
    async [READ_TARGETS] (context)
    {
        let targets = await readTargets();
        if (targets != null)
            context.commit(READ_TARGETS, targets);
    },
    [CREATE_TARGET] (context, target)
    {
        context.commit(CREATE_TARGET, target);
    },
    [DELETE_TARGET] (context, target)
    {
        context.commit(DELETE_TARGET, target);
    }
}

const mutations = {
    [READ_TARGETS](state, targets)
    {
        state.targets = targets;
    },
    [CREATE_TARGET] (state, target)
    {
        state.targets.push(target);
    },
    [DELETE_TARGET] (state, target)
    {
        let tmp = state.targets.find(p => p.id == target.id);
        if (tmp != null) 
        {
            let index = state.targets.indexOf(tmp);
            if (index != null)
                state.targets.splice(index, 1);
        }
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}