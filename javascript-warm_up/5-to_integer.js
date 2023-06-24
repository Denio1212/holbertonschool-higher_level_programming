#!/usr/bin/node

/* converting to int */
if (!parseInt(process.argv[2])) {
  console.log('Not a number')
} else {
  console.log('My number: %d', parseInt(process.argv[2]))
}
