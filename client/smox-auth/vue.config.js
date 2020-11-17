const path = require("path");

module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],
  outputDir: path.resolve(__dirname, "../../src/app/templates/smox-auth"),
  assetsDir: "../../static/smox-auth",
  configureWebpack: {
    resolve: {
      alias: {
          src: path.resolve(__dirname, "src"),
      },
      extensions: ['.js', '.vue', '.json']
    }
  }
}