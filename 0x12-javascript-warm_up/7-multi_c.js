#!/usr/bin/node
const myVar = 'C is fun';
let c = parseInt(process.argv[2]);
if (Number.isInteger(c) && Math.sign(c) === 1) {
  while (c !== 0) {
    console.log(myVar);
    c--;
  }
} else if (Number.isInteger(c) && Math.sign(c) !== 1) {
  c--;
} else {
  console.log('Missing number of occurrences');
}
