#!/usr/bin/node

let fs = require('fs');
const filename = process.argv[2];
const text = process.argv[3];
fs.writeFile(filename, text, function (err) {
  if (err) {
    console.log(err);
  }
});
