#!/usr/bin/node

/**
 * Prints the name of the star wars
 * Title depending on the given int
 */

const url = 'https://swapi-api.hbtn.io/api/films/${procces.argv[2]}';

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const Data = JSON.parse(body);
    console.log(movieData.title);
  }
});