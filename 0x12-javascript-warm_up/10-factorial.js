#!/usr/bin/node
const c = parseInt(process.argv[2]);

function factorial (n) {
  if (Number.isInteger(c) === false) {
    return 1;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(c));
