#!/usr/bin/node
let i = 0;
const list = require('./100-data').list;
const newArray = list.map(x => x * i++);
console.log(list);
console.log(newArray);
