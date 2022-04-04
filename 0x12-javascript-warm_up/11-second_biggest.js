#!/usr/bin/node
let c = 2;
const values = [];
if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log(0);
} else {
  while (process.argv[c] !== undefined) {
    if (!values.includes(process.argv[c])) {
      values.push(process.argv[c]);
    }
    c++;
  }

  console.log(values.sort().reverse()[1]);
}
