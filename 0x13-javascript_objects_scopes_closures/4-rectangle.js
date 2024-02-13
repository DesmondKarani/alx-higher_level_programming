#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (Number.isInteger (w) && w > 0 && Number.isInteger (h) && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if w or h is not a positive integer or is 0
      // This effectively makes this instance an empty object
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat (this.width));
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
