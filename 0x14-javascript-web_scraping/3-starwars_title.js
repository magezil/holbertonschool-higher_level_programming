#!/usr/bin/node

let request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (err) { console.log(err); }
  if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
