export default 
{
    methods: {
        getTitle: function()
        {
            const { title } = this.$options
            if (title) {
                return typeof title === 'function' ? title.call(this) : title
            }
        }
    },
    created () {
        const title = this.getTitle(this)
        if (title) {
          document.title = title
        }
    }
}