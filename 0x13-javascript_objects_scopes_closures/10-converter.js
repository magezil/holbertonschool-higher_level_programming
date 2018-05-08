#!/ usr/bin/node
exports.converter = function (base) {
  return function (num) {
    console.log(convert(num, base));
  }
}

convert = function (num, base) {
  if (num === undefined || isNaN(num))
    return '';
  if (num < base) {
    return "0123456789abcdef"[num];
  }
console.log(num % base);
  return "0123456789abcdef"[parseInt(num / base)] + convert(num % base);
}
