#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let num in list) {
    if (list[num] === searchElement) {
      count++;
    }
  }
  return count;
};
