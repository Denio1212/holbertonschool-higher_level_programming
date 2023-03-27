#!/usr/bin/node

/**
 * fetches name from URL and is
 * displayed in the id
 */
$.get('https://swapi.co/api/people/5/?format=json', (data) => {
  $('#character').text(data.name);
});
