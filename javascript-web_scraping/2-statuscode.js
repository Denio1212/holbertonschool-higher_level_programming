#!/usr/bin/node

/**
 * Displays the status code of a get request
 */

const request = require('request');

request.get(process.argv[2], (error, response) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
