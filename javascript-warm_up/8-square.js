#!/usr/bin/node

const size = process.argv[2];

/* Makes square */
if (!parseInt(size)) {
  console.log('Missing size');
} else if (size > 0) {
  for (let i = 0; i < size; ++i) {
    console.log('X'.repeat(size));
  }
}
