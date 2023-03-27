#!/usr/bin/node

const Previous = require('./5-square');
/* Squares now, + print */

module.exports = class Square extends Previous {
  charPrint (c) {
    if (c == null) {
      super.print();
    } else {
      for (let i = 0; i < this.width; ++i) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
