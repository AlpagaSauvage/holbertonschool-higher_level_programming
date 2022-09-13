#!/usr/bin/node

const axios = require('axios');
const fs = require('fs');

axios.get(process.argv[2]).then(resp => {
  fs.writeFile(
    process.argv[3],
    resp.data,
    function (err) {
		  if (err) {
        return console.error(err);
		  }
    }
	  );
});
