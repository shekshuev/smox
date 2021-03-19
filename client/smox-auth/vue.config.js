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
      filename: 'auth/auth.[hash].js',
      chunkFilename: 'auth/auth.chunk.[hash].js',
    }
  },
  css: {
    extract: {
      filename: 'auth/auth.[hash].css',
      chunkFilename: 'auth/auth.chunk.[hash].css',
    },
  },
  pages: {
    index: {
      entry: 'src/main.js',
      template: 'public/auth.html',
      filename: 'auth.html',
      title: 'SMOX Login'
    }
  }
}