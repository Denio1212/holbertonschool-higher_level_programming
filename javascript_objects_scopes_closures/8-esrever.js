#!/usr/bin/node

/* Returns a reversed list */

exports.esrever = function (list) {
  let tmp;
   
  for (let i = 0, j = list.length - 1; i < j; ++i, --j) {
    tmp = list[i];
    list[i] = list[j];
    list[j] = tmp;
   }
   return (list);
};
