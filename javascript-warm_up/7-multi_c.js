#!/usr/bin/node

/* Prints the set times */
if (!procces.argv[2]) {
  console.log('Missing number of occurences');
} else if (procces.argv[2] > 0) {
  for (let i = procces.argv[2]; i; i--) {
    console.log('C is fun');
  }
}