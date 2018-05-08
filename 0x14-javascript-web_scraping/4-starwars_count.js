#!/usr/bin/node

let request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) { console.log(err); }
  if (response.statusCode === 200) {
    let results = JSON.parse(body).results;
    let count = 0;
    for (let res in results) {
      let characters = results[res]['characters'];
      for (let c in characters) {
        if (characters[c].search('/18/') > 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
