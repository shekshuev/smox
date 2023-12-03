<template>
    <div>
        <transition name="fade">
            <div key="2" v-if="!loading">
                <App />
            </div>
        </transition>
        <transition name="fade">
            <div key="1" v-if="loading">
                <LoadingScreen :progress="progress" />
            </div>
        </transition>
    </div>
</template>
<script>
import Vue from "vue";
import App from "src/app.vue";
import LoadingScreen from "src/loadingscreen.vue";
import { LOAD_ACCESS_PROFILES } from "./store/modules/access_profile/mutation_types";
import { READ_DATABASE_CONNECTION } from "./store/modules/settings/mutation_types";
import { LOAD_SOURCES } from "./store/modules/source/mutation_types";
import { LOAD_TASKS } from "./store/modules/task/mutation_types";
import { READ_TARGETS } from "./store/modules/target/mutation_types";

export default Vue.component("initial", {
    components: { App, LoadingScreen },
    data: function() {
        return {
            loading: true,
            progress: 0,
        };
    },
    watch: {
        progress: function(newVal) {
            if (newVal >= 100) {
                setTimeout(() => (this.loading = false), 500);
            }
        },
    },
    created: function() {
        this.$vuetify.theme.dark = this.$store.state.settings.appearance.dark_mode;
        this.$store.dispatch(LOAD_ACCESS_PROFILES).then(() => (this.progress += 25));
        this.$store.dispatch(LOAD_SOURCES).then(() => (this.progress += 25));
        this.$store.dispatch(LOAD_TASKS).then(() => (this.progress += 25));
        this.$store.dispatch(READ_TARGETS).then(() => (this.progress += 25));
        this.$store.dispatch(READ_DATABASE_CONNECTION);
    },
});
</script>
<style>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 1s;
}
.fade-enter,
.fade-leave-to {
    opacity: 0;
}
</style>
