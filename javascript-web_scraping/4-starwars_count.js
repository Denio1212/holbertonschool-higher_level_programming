#!/usr/bin/node

/**
 * Wedge Antilles
 */

const request = require('request');

let count = 0;

request.get(process.argv[2], function (error, response, body) {
  if (error) console.log(error);
  else {
    for (const film of JSON.parse(body).results) {
      for (const character of film.characters) {
        if (character.includes('18')) ++count;
      }
    }
    console.log(count);
  }
});
