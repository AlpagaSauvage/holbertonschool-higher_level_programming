#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('No argument');
} else if (process.argv[3] === undefined && process.argv[2]) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
