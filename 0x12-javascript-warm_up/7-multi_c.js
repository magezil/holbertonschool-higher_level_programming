#!/usr/bin/node
const cisfun = 'C is fun';
const num = parseInt(process.argv[2], 10);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log(cisfun);
  }
}
