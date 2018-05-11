#!/usr/bin/node

let fs = require('fs');
let request = require('request');
const url = process.argv[2];
const filename = process.argv[3];
request(url, function (err, response, body) {
  if (err) { console.log(err); }
  if (response.statusCode === 200) {
    fs.writeFile(filename, body, function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
