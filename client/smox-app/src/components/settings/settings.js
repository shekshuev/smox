import Vue from "vue";
import { mapState } from "vuex";
import { addProfile, deleteProfile } from "src/api/access_profile";
import { ADD_ACCESS_PROFILE, DELETE_ACCESS_PROFILE } from "src/store/modules/access_profile/mutation_types";
import { createSource, searchSource, deleteSource } from "src/api/source";
import { ADD_SOURCE, DELETE_SOURCE } from "src/store/modules/source/mutation_types";
import { SET_APPEARANCE , UPDATE_DATABASE_CONNECTION} from "src/store/modules/settings/mutation_types";
import { updateDatatbaseConnection } from "src/api/settings";

export default Vue.component("settings",
{
    data: function()
    {
        return {
            accessProfileDialog: false,
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
            accessToken: "",
            confirmDialog: false,
            deletableObject: null,
            showPassword: false
        }
    },
    computed: {
        ...mapState({
            sources: state => state.source.sources,
            accessProfiles: state => state.accessProfile.accessProfiles,
            db: state => state.settings.db
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
        },
        dbHost: 
        {
            get()
            {
                return this.$store.state.settings.db.host
            },
            set(newVal)
            {
                let db = Object.assign({}, this.$store.state.settings.db)
                db.host = newVal
                this.$store.dispatch(UPDATE_DATABASE_CONNECTION, db)
            }
        },
        dbName: 
        {
            get()
            {
                return this.$store.state.settings.db.name
            },
            set(newVal)
            {
                let db = Object.assign({}, this.$store.state.settings.db)
                db.name = newVal
                this.$store.dispatch(UPDATE_DATABASE_CONNECTION, db)
            }
        },
        dbLogin: 
        {
            get()
            {
                return this.$store.state.settings.db.login
            },
            set(newVal)
            {
                let db = Object.assign({}, this.$store.state.settings.db)
                db.login = newVal
                this.$store.dispatch(UPDATE_DATABASE_CONNECTION, db)
            }
        },
        dbPassword: 
        {
            get()
            {
                return this.$store.state.settings.db.password
            },
            set(newVal)
            {
                let db = Object.assign({}, this.$store.state.settings.db)
                db.password = newVal
                this.$store.dispatch(UPDATE_DATABASE_CONNECTION, db)
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
            if (this.$refs.accessProfileForm.validate())
            {
                let result = await addProfile({ name: this.name, accessToken: this.accessToken });
                if (result != null)
                {
                    this.$store.dispatch(ADD_ACCESS_PROFILE, result);
                    this.name = ""
                    this.accessToken = ""
                    this.accessProfileDialog = false;
                    this.$refs.accessProfileForm.reset();
                }
            }
        },
        async deleteAccessProfile(profile)
        {
            this.deletableObject = 
            {
                type: "profile",
                payload: profile
            };
            this.confirmDialog = true;
        },
        async deleteSource(source)
        {
            this.deletableObject = 
            {
                type: "source",
                payload: source
            };
            this.confirmDialog = true;
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
        },
        async deleteObject()
        {
            if (this.deletableObject.type == "source")
            {
                if (await deleteSource(this.deletableObject.payload))
                {
                    this.$store.dispatch(DELETE_SOURCE, this.deletableObject.payload);
                    this.closeConfirmDialog();
                }   
            }
            else 
            {
                if (await deleteProfile(this.deletableObject.payload))
                {
                    this.$store.dispatch(DELETE_ACCESS_PROFILE, this.deletableObject.payload);
                    this.closeConfirmDialog();
                } 
            }
        },
        closeConfirmDialog()
        {
            this.deletableObject = null;
            this.confirmDialog = false;
        },
        async updateDbConnection()
        {
            if (await updateDatatbaseConnection(this.db))
            {
                console.log("fuck yeah!")
            }
        }
    }
});