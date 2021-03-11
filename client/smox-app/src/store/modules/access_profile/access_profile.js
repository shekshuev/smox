import { LOAD_ACCESS_PROFILES, ADD_ACCESS_PROFILE, DELETE_ACCESS_PROFILE } from "./mutation_types";
import { getProfiles } from "src/api/access_profile";

const state = () => (
{
    accessProfiles: []
});

const getters = {}

const actions = {
    async [LOAD_ACCESS_PROFILES] (context)
    {
        let profiles = await getProfiles();
        if (profiles != null)
            context.commit(LOAD_ACCESS_PROFILES, profiles);
    },
    [ADD_ACCESS_PROFILE] (context, profile)
    {
        context.commit(ADD_ACCESS_PROFILE, profile);
    },
    [DELETE_ACCESS_PROFILE] (context, profile)
    {
        context.commit(DELETE_ACCESS_PROFILE, profile);
    }
}

const mutations = {
    [LOAD_ACCESS_PROFILES](state, profiles)
    {
        state.accessProfiles = profiles;
    },
    [ADD_ACCESS_PROFILE] (state, profile)
    {
        state.accessProfiles.push(profile);
    },
    //[UPDATE_ACCESS_PROFILE] (state, profile)
    //{

    //},
    [DELETE_ACCESS_PROFILE] (state, profile)
    {
        let tmp = state.accessProfiles.find(p => p.id == profile.id);
        if (tmp != null) 
        {
            let index = state.accessProfiles.indexOf(tmp);
            if (index != null)
                state.accessProfiles.splice(index, 1);
        }
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}