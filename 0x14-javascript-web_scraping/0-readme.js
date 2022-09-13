#!/usr/bin/node

const fs = require('fs');

fs.writeFile(
  'cisfun',
  'C is super fun!',
  function (err) {
    if (err) {
      return console.error(err);
    }

    fs.readFile(process.argv[2], function (err, data) {
      if (err) {
        return console.error(err);
      }
      console.log(data.toString());
    });
  }
);
