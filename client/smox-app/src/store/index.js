import Vue from "vue";
import Vuex from "vuex";
import accessProfile from "src/store/modules/access_profile/access_profile";
import source from "src/store/modules/source/source";
import task from "src/store/modules/task/task";
import post from "src/store/modules/post/post";

Vue.use(Vuex);

const debug = process.env.NODE_ENV !== "production";

const store = new Vuex.Store(
{
    mutations: {
        initialiseStore(state) 
        {
            console.log(typeof(localStorage.getItem('startDate')))
            if(localStorage.getItem('options')) 
            {
				state.post.options = JSON.parse(localStorage.getItem('options'))
            }
            if(localStorage.getItem('startDate')) 
            { 
				state.post.startDate = new Date(localStorage.getItem('startDate'));
            }
            if(localStorage.getItem('endDate')) 
            {
				state.post.endDate = new Date(localStorage.getItem('endDate'));
			}
		}
	},
    modules: 
    {
        accessProfile,
        source,
        task,
        post
    },
    strict: debug
});
store.subscribe((mutation, state) => 
{
    localStorage.setItem('options', JSON.stringify(state.post.options));
    localStorage.setItem('startDate', state.post.startDate);
    localStorage.setItem('endDate', state.post.endDate);
});

export default store;