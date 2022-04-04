#!/usr/bin/node
const myVar = 'X';
const i = parseInt(process.argv[2]);
let c = i;
if (Number.isInteger(i) && Math.sign(i) === 1) {
  while (c !== 0) {
    console.log(myVar.repeat(i));
    c--;
  }
} else if (Number.isInteger(i) && Math.sign(i) !== 1) {
  c--;
} else {
  console.log('Missing size');
}
