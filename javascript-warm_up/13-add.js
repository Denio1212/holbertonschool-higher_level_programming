#!/usr/bin/node

/* Returns addition of 2 integers, now EXPORTABLE */
function add (a, b) {
  return a + b;
}
module.exports.add = add;
