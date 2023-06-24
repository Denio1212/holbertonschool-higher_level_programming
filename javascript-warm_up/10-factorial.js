#!/usr/bin/node

/* makes the factorial happen */

function factorial (n) {
  if (!n) {
    return 1;
  } else if (n > 0) {
    return n * factorial(n - 1);
  }
}

console.log(factorial(parseInt(process.argv[2])));
