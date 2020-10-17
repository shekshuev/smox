import Vue from "vue";
import sourceCard from "application/components/source/sourcecard.vue";

export default Vue.component("tasksourcecard",
{
    components: { sourceCard },
    props: [ "taskSource" ]
});