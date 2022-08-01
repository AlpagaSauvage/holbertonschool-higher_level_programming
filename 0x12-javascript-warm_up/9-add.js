#!/usr/bin/node
function add (a, b) {
  if (Number.isInteger(a) && Number.isInteger(b)) {
    console.log(a + b);
  } else {
    console.log('NaN');
  }
}
add(parseInt(process.argv[2]), parseInt(process.argv[3]));
