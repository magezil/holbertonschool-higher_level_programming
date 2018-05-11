#!/usr/bin/node

let request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) { console.log(err); }
  if (response.statusCode === 200) {
    const completed = {};
    let results = JSON.parse(body);
    for (let cur in results) {
      let current = results[cur];
      if (current['completed'] === true) {
        let userId = current['userId'];
        if (userId in completed) {
          completed[userId]++;
        } else {
          completed[userId] = 1;
        }
      }
    }
    console.log(completed);
  }
});
