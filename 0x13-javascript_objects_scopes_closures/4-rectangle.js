#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let side = '';
    for (let i = 0; i < this.width; i++) {
      side += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(side);
    }
  }

  rotate () {
    this.width += this.height;
    this.height = this.width - this.height;
    this.width -= this.height;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
