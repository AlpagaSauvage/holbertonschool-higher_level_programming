#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; ++x) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    this.temp = this.width;
    this.width = this.height;
    this.height = this.temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let x = 0; x < this.height; ++x) {
        console.log('C'.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Rectangle;
module.exports = Square;
