#!/usr/bin/node

/* Second only */
if (process.argv.length == 2 || process.argv.length == 3) {
  console.log('0');
} else {
  const list = process.argv.slice(2).sort((a, b) => a - b);
  const len = list.length;

  console.log(list[len - 2]);
}
