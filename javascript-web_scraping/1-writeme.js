#!/usr/bin/node

/**
 * Writes a string to a file
 */

const fs = require('fs');

fs.writeFile(procces.argv[2], procces.argv[3], (err) => {
  if (err) throw err;
});
