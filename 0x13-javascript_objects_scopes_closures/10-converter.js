#!/usr/bin/node
exports.converter = function (base) {
  return function (nombre) {
    return (nombre.toString(base));
  };
};
