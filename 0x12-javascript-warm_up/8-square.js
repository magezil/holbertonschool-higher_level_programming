#!/usr/bin/node
const c = 'X';
const size = parseInt(process.argv[2], 10);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let line = '';
  for (let i = 0; i < size; i++) {
    line += c;
  }
  for (let i = 0; i < size; i++) {
    console.log(line);
  }
}
