import Vue from "vue";
import { mapState } from "vuex";
import { addProfile, deleteProfile } from "src/api/access_profile";
import { ADD_ACCESS_PROFILE, DELETE_ACCESS_PROFILE } from "src/store/modules/access_profile/mutation_types";
import { deleteSource } from "src/api/source";
import { DELETE_SOURCE } from "src/store/modules/source/mutation_types";
import { SET_APPEARANCE } from "src/store/modules/settings/mutation_types";

export default Vue.component("settings",
{
    data: function()
    {
        return {
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
        }
    }
});