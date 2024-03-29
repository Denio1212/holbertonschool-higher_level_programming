#!/usr/bin/node

/**
 * Prints the name of the star wars
 * Title depending on the given int
 */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/${process.argv[2]}';

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const Data = JSON.parse(body);
    console.log(Data.title);
  }
});
