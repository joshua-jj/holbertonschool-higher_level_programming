#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const wedge = 'https://swapi.co/api/people/18/';
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let films = JSON.parse(body).results;
    let count = 0;
    for (let filmIndex in films) {
      let filmChars = films[filmIndex].characters;
      if (filmChars.includes(wedge)) {
        count++;
      }
    }
    console.log(count);
  }
});
