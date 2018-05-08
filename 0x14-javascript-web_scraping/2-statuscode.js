#!/usr/bin/node

let request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) { console.log(err); }
  console.log('code: ' + response.statusCode);
});
