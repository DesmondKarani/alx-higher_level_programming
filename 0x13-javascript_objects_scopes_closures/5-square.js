#!/usr/bin/node
// 5-square.js
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(size) {
    super(size, size); // Calling the constructor of Rectangle
  }
}

module.exports = Square;
