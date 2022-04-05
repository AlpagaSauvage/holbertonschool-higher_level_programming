#!/usr/bin/node
const Square = require('./4-rectangle')

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let myvar = c;
    if (myvar === undefined) {
      myvar = 'X';
    }
    let i = this.height;
    while (i !== 0) {
      console.log(myvar.repeat(this.width));
      i--;
    }
  }
}

module.exports = Square;
