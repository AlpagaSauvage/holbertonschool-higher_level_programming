#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let c = 0;
  let i = 0;
  while (i <= list.length) {
    if (list[i] === searchElement) {
      c++;
    }
    i++;
  }
  return (c);
};
