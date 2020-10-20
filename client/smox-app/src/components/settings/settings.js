import Vue from "vue";
import { mapState } from "vuex";
import { addProfile, deleteProfile } from "src/api/access_profile";
import { ADD_ACCESS_PROFILE, DELETE_ACCESS_PROFILE } from "src/store/modules/access_profile/mutation_types";

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
    computed: mapState({
        accessProfiles: state => state.accessProfile.accessProfiles
    }),
    methods: 
    {
        async addAccessProfile()
        {
            let result = await addProfile({ id: 0, name: this.name, accessToken: this.accessToken, current: false });
            if (result != null)
                this.$store.dispatch(ADD_ACCESS_PROFILE, result);
        },
        async deleteAccessProfile(profile)
        {
            if (await deleteProfile(profile))
            {
                this.$store.dispatch(DELETE_ACCESS_PROFILE, profile);
            }
        }
    }
});