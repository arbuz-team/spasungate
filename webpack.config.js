"use strict";

var
    ExtractTextPlugin = require('extract-text-webpack-plugin'),
    base_path = './client/';

module.exports = {
  entry: base_path + 'sandbox.js',
  output: { 
    path: __dirname, 
    filename: base_path + 'static/js/bundle.js'
  },
  devtool: "source-map",
  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        loader: 'babel', // 'babel-loader' is also a valid name to reference
        query: {
          presets: ['es2015']
        }
      },
      {
        test: /\.sass$/,
        loader: ExtractTextPlugin.extract(
          "style",
          "css?-url!sass" // &minimize
        )
      }

    ]
  },
  plugins: [
    new ExtractTextPlugin(base_path + 'static/css/bundle.css')
  ]
};