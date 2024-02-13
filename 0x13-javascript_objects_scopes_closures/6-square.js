#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    console.log(c.repeat(this.width).split('').join('').repeat(this.height).split('').join('\n'));
  }
}

module.exports = Square;
