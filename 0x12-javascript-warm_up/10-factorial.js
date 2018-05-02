#!/usr/bin/node
function f (x) {
  if (isNaN(x)) {
    return 1;
  }
  if (x === 1) {
    return 1;
  }
  return x * f(x - 1);
}

console.log(f(parseInt(process.argv[2])));
