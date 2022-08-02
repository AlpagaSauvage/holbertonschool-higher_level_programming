#!/usr/bin/node

exports.esrever = function (list) {
  let i = list.length - 1;
  let x = 0;
  const newlist = [];
  while (i >= 0) {
    newlist[x] = list[i];
    i--;
    x++;
  }
  return newlist;
};
