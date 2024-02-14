#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, async (err, response, body) => {
  if (err == null) {
    const resp = JSON.parse(body);
    const characters = resp.characters;
    for (const character of characters) {
      await new Promise((resolve, reject) => {
        request(character, function (err, response, body) {
	  if (err == null) {
	    console.log(JSON.parse(body).name);
	      resolve();
	  }
	});
      });
    }
  }
});
