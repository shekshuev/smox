import Vue from "vue";
import { mapState } from "vuex";
import { addProfile, deleteProfile } from "src/api/access_profile";
import { ADD_ACCESS_PROFILE, DELETE_ACCESS_PROFILE } from "src/store/modules/access_profile/mutation_types";
import { createSource, searchSource, deleteSource } from "src/api/source";
import { ADD_SOURCE, DELETE_SOURCE } from "src/store/modules/source/mutation_types";
import { SET_APPEARANCE } from "src/store/modules/settings/mutation_types";
import sourceCard from "src/components/source/sourcecard.vue";

export default Vue.component("settings",
{
    components: { sourceCard },
    data: function()
    {
        return {
            sourceDialog: false,
            step: 0,
            source: null,
            selectedAccessProfile: null,
            request: "",
            loading: false,
            delay: 0,
            valid: false,
            name: "",
            rules: [
                v => !!v || "Поле обязательно для заполнения",
            ],
            accessToken: ""
        }
    },
    computed: {
        ...mapState({
            sources: state => state.source.sources,
            accessProfiles: state => state.accessProfile.accessProfiles,
        }),
        dark_mode: 
        {
            get()
            {
                return this.$store.state.settings.appearance.dark_mode
            },
            set()
            {
                this.$vuetify.theme.dark = !this.dark_mode
                let appearance = Object.assign({}, this.$store.state.settings.appearance)
                appearance.dark_mode = !this.dark_mode
                this.$store.dispatch(SET_APPEARANCE, appearance)
            }
        }
    },
    watch: 
    {
        request: async function (newRequest)
        {
            
            clearTimeout(this.delay);
            if (newRequest == "") return;
            this.delay = setTimeout(async () => 
            {
                this.loading = true;
                this.source = await searchSource(newRequest, this.selectedAccessProfile.access_token);
                this.loading = false;
            }, 2000);
        }
    },
    methods: 
    {
        async addAccessProfile()
        {
            let result = await addProfile({ name: this.name, accessToken: this.accessToken });
            if (result != null)
                this.$store.dispatch(ADD_ACCESS_PROFILE, result);
        },
        async deleteAccessProfile(profile)
        {
            if (await deleteProfile(profile))
            {
                this.$store.dispatch(DELETE_ACCESS_PROFILE, profile);
            }
        },
        async deleteSource(source)
        {
            if (await deleteSource(source))
                this.$store.dispatch(DELETE_SOURCE, source);
        },
        async saveSource()
        {
            let result = await createSource(this.source)
            if (result != null)
            {
                this.$store.dispatch(ADD_SOURCE, result);
                this.sourceDialog = false;
                this.clearSource()
            }
        },
        clearSource()
        {
            this.source = null;
            this.request = "";
            this.loading = false;
            clearTimeout(this.delay);
            this.delay = 0;
        }
    }
});