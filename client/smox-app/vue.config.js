const path = require("path");
module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],
  configureWebpack: {
    resolve: {
      alias: {
          src: path.resolve(__dirname, "src"),
      },
      extensions: ['.js', '.vue', '.json']
  }
  }
}