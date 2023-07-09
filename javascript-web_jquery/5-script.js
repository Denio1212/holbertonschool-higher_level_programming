#!/usr/bin/node

/**
 * Adds a list when user clicks on
 * an id.
 */
$('#add_item').click(() => {
    $('ul.my_list').append($('<li>Item</li>'));
  });
