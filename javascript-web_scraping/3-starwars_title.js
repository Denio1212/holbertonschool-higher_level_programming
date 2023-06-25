#!/usr/bin/node

/**
 * Prints the name of the star wars
 * Title depending on the given int
 * const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/${process.argv[2]}';

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const Data = JSON.parse(body);
    console.log(Data.title);
  }
});
 */
const request = require('request');

request.get(`https://swapi.co/api/films/${process.argv[2]}/`,
  function (error, response, body) {
    if (error) console.log(error);
    else console.log(JSON.parse(body).title);
  });
