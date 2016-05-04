var config = require('./webpack.base.config')

config.devtool = '#eval-source-map'

config.devServer = {
    noInfo: true,
    proxy: {
        "/api_*": "http://localhost:9000",
        "/login": "http://localhost:9000",
        "/static/*": "http://localhost:9000"
    }
}

module.exports = config
