/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;
/******/
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			exports: {},
/******/ 			id: moduleId,
/******/ 			loaded: false
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.loaded = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	//noinspection JSUnresolvedFunction
	__webpack_require__(1);
	
	//noinspection JSUnresolvedFunction
	window.viewability = function () {
	  return __webpack_require__(5);
	}();

/***/ },
/* 1 */
/***/ function(module, exports) {

	// removed by extract-text-webpack-plugin

/***/ },
/* 2 */,
/* 3 */,
/* 4 */,
/* 5 */
/***/ function(module, exports) {

	'use strict';
	
	/**
	 * Created by mrskull on 24.11.16.
	 */
	
	var set_ground_size = function set_ground_size() {
		var $container = document.getElementById('CONTAINTER'),
		    $header = $container.querySelectorAll('.header')[0],
		    $ground = $container.querySelectorAll('.ground')[0],
		    $ground_block = $container.querySelectorAll('.ground-block')[0],
		    $footer = $container.querySelectorAll('.footer-content')[0],
		    window_height = window.document.body.clientHeight,
		    header_height = $header.clientHeight,
		    footer_height = $footer.clientHeight,
		    ground_before_height = $ground.offsetTop,
		    ground_height = window_height - header_height,
		    ground_block_height = ground_height - footer_height - ground_before_height;
	
		$ground.style.height = ground_height + 'px';
		$ground_block.style.minHeight = ground_block_height + 'px';
	};
	
	window.addEventListener('load', set_ground_size);
	
	window.addEventListener('resize', set_ground_size);

/***/ }
/******/ ]);
//# sourceMappingURL=bundle.js.map