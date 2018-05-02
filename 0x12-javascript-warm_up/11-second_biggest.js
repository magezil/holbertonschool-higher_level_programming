#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(process.argv.sort().reverse()[1]);
}
