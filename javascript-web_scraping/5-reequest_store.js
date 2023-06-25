#!/usr/bin/node

/**
 * Gets contents and turns it to a file
 */

const request = require('request');
const fs = require('fs');

request.get(process.argv[2], function (error, response, body) {
  if (error) console.log(error);
  else {
    fs.writeFile(process.argv[3], body, (err) => {
      if (err) console.log(err);
    });
  }
});
