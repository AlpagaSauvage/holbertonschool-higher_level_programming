#!/usr/bin/node
const a = process.argv[2];
const b = process.argv[3];
if (b) {
  console.log(process.argv[2], 'is', process.argv[3]);
} else if (a) {
  console.log(process.argv[2], 'is', 'undefined');
} else {
  console.log('undefined', 'is', 'undefined');
}
