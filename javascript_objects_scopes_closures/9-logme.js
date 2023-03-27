#!/usr/bin/node

/** prints number of arguments already printed
 * Including the new argument
*/

let count = 0;
exports.logMe = function (item) {
  console.log('%d: %s', count, item);
  ++count;
};
