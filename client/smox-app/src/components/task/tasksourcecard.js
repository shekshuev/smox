import Vue from "vue";
import sourceCard from "src/components/source/sourcecard.vue";

export default Vue.component("tasksourcecard",
{
    components: { sourceCard },
    props: [ "taskSource" ]
});