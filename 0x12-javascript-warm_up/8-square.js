#!/usr/bin/node
const i = process.argv[2];
if (parseInt(process.argv[2])) {
  for (let x = 0; x < process.argv[2]; ++x) {
    const j = i;
    console.log('X'.repeat(j));
  }
} else {
  console.log('Missing size');
}
