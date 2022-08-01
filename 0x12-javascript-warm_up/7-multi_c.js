#!/usr/bin/node
const myVar = process.argv[2];
if (parseInt(myVar)) {
  for (let x = 0; x < myVar; ++x) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
