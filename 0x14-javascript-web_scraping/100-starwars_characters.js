#!/usr/bin/node

const axios = require('axios');

axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2]).then(resp => {
	for (const char of resp.data.characters) {
		axios.get(char)
		  .then(res => {
			console.log(res.data.name);
		  })
	}
})
.catch(err => console.log(err));
