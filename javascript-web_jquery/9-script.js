#!/usr/bin/node

/**
 * Fetches from url and
 * displays the value hello in the id
 */
$.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: (r) => {
      $('#hello').text(r.hello);
    }
  });
