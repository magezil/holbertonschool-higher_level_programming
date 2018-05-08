#!/usr/bin/node

let fs = require('fs');
const filename = process.argv[2];
fs.readFile(filename, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
