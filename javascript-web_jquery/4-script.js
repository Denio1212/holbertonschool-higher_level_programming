#!/usr/bin/node

/**
 * triggers only when the id toggle header is input
 */
$('#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
