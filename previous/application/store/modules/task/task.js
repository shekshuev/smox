import { LOAD_TASKS, ADD_TASK, UPDATE_TASK, DELETE_TASK } from "./mutation_types";
import { getTasks } from "application/api/task";
import Vue from "vue";

const state = () => (
{
    tasks: []
});

const getters = {}

const actions = {
    async [LOAD_TASKS] (context)
    {
        let tasks = await getTasks();
        if (tasks != null)
            context.commit(LOAD_TASKS, tasks);

    },
    [ADD_TASK] (context, task)
    {
        context.commit(ADD_TASK, task);
    },
    [UPDATE_TASK] (context, task)
    {
        context.commit(UPDATE_TASK, task);
    },
    [DELETE_TASK] (context, task)
    {
        context.commit(DELETE_TASK, task);
    }
}

const mutations = {
    [LOAD_TASKS](state, tasks)
    {
        state.tasks = tasks;
    },
    [ADD_TASK] (state, task)
    {
        state.tasks.push(task);
    },
    [UPDATE_TASK] (state, task)
    {
        let tmp = state.tasks.find(t => t.id == task.id);
        if (tmp != null) 
        {
            let index = state.tasks.indexOf(tmp);
            if (index != null)
            {
                state.tasks[index] = task;
                Vue.set(state, "tasks", [...state.tasks]);
            }
                
        }
    },
    [DELETE_TASK] (state, task)
    {
        let tmp = state.tasks.find(t => t.id == task.id);
        if (tmp != null) 
        {
            let index = state.tasks.indexOf(tmp);
            if (index != null){}
                state.tasks.splice(index, 1);
        }
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}