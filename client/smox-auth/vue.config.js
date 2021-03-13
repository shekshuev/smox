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
  chainWebpack: (config) => {
    if (process.env.NODE_ENV === 'production') {
        config.plugin('html').tap((opts) => {
            opts[0].filename = './auth.html';
            return opts;
        });
    }
  }
}