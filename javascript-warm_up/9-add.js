#!/usr/bin/node

/* A function to add 2 numbers */
function add (a, b) {
  return a + b;
}

console.log(add(parseInt(console.argv[2]), parseInt(console.argv[3])));