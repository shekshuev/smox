const path = require("path");

module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],
  outputDir: path.resolve(__dirname, "../../src/app/templates/smox"),
  configureWebpack: {
    resolve: {
      alias: {
          src: path.resolve(__dirname, "src"),
      },
      extensions: ['.js', '.vue', '.json']
    },
    output: {
      filename: 'app/app.[hash].js',
      chunkFilename: 'app/app.chunk.[hash].js',
    }
  },
  css: {
    extract: {
      filename: 'app/app.[hash].css',
      chunkFilename: 'app/app.chunk.[hash].css',
    },
  }
}