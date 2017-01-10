# 100 Days Of Code - Log

# 1484033087 20170109 23:24 Day 4 Altum Videtur
** Today I took a little sojourn into the server side; and into lxml/xpath
   parsing.  I decided to use the full Latin Phrases list on Wikipedia as
   a source for my own quote server; extract all the quotes from the tables
   in that page (over 2100 of them), encode them out as JSON, then write
   a very tiny Python Bottle app to serve them up:

   http://www.starshine.org:8888/phrase/latin

   The code to pull the data and extract the quotes is in quotes2json.py
   and and the Bottle server is in quotegen.py.  The data is in quotes.json


# 1483779653 20170107 01:00 Day 3 "JSON APIs and Ajax (2 hours)"
** Today I finished the last little sections on JSON APIs.

  I think they do a terrible job explaining what the server side processing
  looks like.  I know how it works, because I have writtent that sort of
  code (from old-fashioned CGI to AJAX even).  But a novice might get
  lost in the abstractions here.

# 1483670268 20170105 18:37 Day 2
** Today finshed the rest of the "Basic Algorithm Scripting"


  A few of the bits of code I came up with are surprising;

    Example:

        function mutation(arr) {
          var map = {};
          arr[0].toLowerCase().split('').filter(function(i){map[i]=i;return map;});
          result = arr[1].toLowerCase().split('').filter(function(k){return !(k in map);});
          return !(result.length);
        }

        mutation(["hello", "hey"]);

  ... The !(k in map) and !(result.length)  parts work;
  I build a map from the first string and then filter out everythign that is not an element thereof
  ... but result.length == 0 flags as a warning. :(

    Example:

        function destroyer(arr) {
          var args = Array.prototype.slice.call(arguments);
          var targ = args.shift();
          var kill = {};
          args.filter(function(i){kill[i]=i;});
          return targ.filter(function(k){return !(k in kill);});
        }

        destroyer([1, 2, 3, 1, 2, 3], 2, 3);

  ... arr in this case is a red herring; it contains a flattening of all the arguments
  while we want to use the arguments object; and preferably to build an Array() of them
  so we can use shift(), slice(), ... etc.

    Example:

        function getIndexToIns(arr, num) {
          arr = arr.sort(function(a,b) {return a>b;});
          for (var i=0; i<arr.length;i++){
            if (num <= arr[i]) {
              return i;
            }
          }
          return arr.length;
        }

        getIndexToIns([5, 3, 20, 3], 50);

  ... .sort() is lexical rather than by "scalar" comparison by default; had to pass a function
  to make it sort numerically!

    Example:

        function bouncer(arr) {
          return arr.filter(function(i){return !(!(i));});
        }
        bouncer([7, "ate", "", false, 9]);

    Example:  (ord() and chr() in JavaScript are a mess!)

        function rot13(str) { // LBH QVQ VG!
          var base = 'A'.charCodeAt(0);
          var result = str.split('').map(function(c){
            var chr = c.charCodeAt(0) - base;
            if (0 <= chr && chr < 26 ) {
              return String.fromCharCode(((chr + 13) % 26)+base);
            } else { return c;}
          });
          return result.join('');
        }

        // Change the inputs below to test
        rot13("SERR PBQR PNZC");


# 1483558021 20170104 11:27 Day 1
** Today: Finished Object Oriented and Functional Programming (2 hours)
   in about 20 min. while in a conference call at work

   Moving on to Basic Algorithm Scripting (50 hours)!

** Finished 6 of 17 of those.

   Suggestions to the FCC development team:
    * Add optional audio recitation to (almost) every page
    * Add orientation explaining TDD (test-driven development) and how it relates to the FCC service
    * Move jQuery to be after JavaScript
    ** Add orientation emphasizing that jQuery is JavaScript
    *** note that $ is just a variable name ... the entry point for jQuery
    *** note that _ is a similar example for "underscore" and "lodash"
    * Add info about and orientation for ES6 (ES2016?)
    * Add SQL/SQLite Section!!!!
    * Start adding test-driven development (TDD)

*** URL for LinkedIn posting (pythy.html): www.linkedin.com/hp/update/6222725051016450049

** Yesterday:
*** URL for LinkedIn posting (nobox.html): https://lnkd.in/gTsDEDh
*** URL for FCC Forum Question: https://forum.freecodecamp.com/t/add-bootstrap-classes-to-svg-elements/71896/1
  (About SVG and Bootstrap buttons)
 

# 1483520887 20170104 01:08 Day 0

** Yesterday: finished review of FCC stuff
   Finished FCC HTML5 and CSS (5 hours), Responsive Design with Bootstrap (5 hours),
 Gear up for Success (20 minutes), jQuery (3 hours), Basic Front End Development Projects (50 hours)
** Today: finished Basic JavaScript (10 hours)

* Thoughts: I also posted links to my old Pythy (JS animation) and "Nine Dots" (SVG) pages and a question
  regarding how to clean up the latter.

** Links:
*** http://www.starshine.org/jimd/pythy.html
*** http://www.starshine.org/jimd/nobox.html


