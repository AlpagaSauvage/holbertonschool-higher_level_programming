#!/usr/bin/node

const axios = require('axios');

axios.get(process.argv[2]).then(resp => {
  let nb = 0;
  for (const film of resp.data.results) {
    for (const id of film.characters) {
      if (id.includes('18')) {
        nb += 1;
      }
    }
  }
  console.log(nb);
})
  .catch(err => console.log(err));
