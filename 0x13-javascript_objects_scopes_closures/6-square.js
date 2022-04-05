#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let myVar = c;
    if (myVar === undefined) {
      myVar = 'X';
    }
    let i = this.height;
    while (i !== 0) {
      console.log(myVar.repeat(this.width));
      i--;
    }
  }
}

module.exports = Square;
