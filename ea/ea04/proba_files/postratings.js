/*
+----------------------------------------------------------------+
|                                                                |
|	Modified WordPress 2.0 Plugin: WP-PostRatings 1.02       |
|	Copyright (c) 2006 Lester "GaMerZ" Chan                  |
|                                                                |
|	File Written By:                                         |
|	- Lester "GaMerZ" Chan                                   |
|	- http://www.lesterchan.net                              |
|                                                                |
|	File Information:                                        |
|	- Post Ratings Javascript File                           |
|	- wp-content/plugins/postratings/postratings-js.js       |
|                                                                |
+----------------------------------------------------------------+
*/


// Variables
var post_id = 0;
var post_rating = 0;
var rate_fadein_opacity = 0;
var rate_fadeout_opacity = 100;
var is_ie = (document.all && document.getElementById);
var is_moz = (!document.all && document.getElementById);
var is_being_rated = false;


function rate_process_nofade() {
	ratings.setVar("id", post_id);
	ratings.setVar("answer", post_rating);
	ratings.method = 'GET';
	ratings.element = 'post-ratings-' + post_id;
	ratings.runAJAX();
}

