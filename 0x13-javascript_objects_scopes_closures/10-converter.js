#!/ usr/bin/node
exports.converter = function (base) {
  return function convert (num) {
    if (isNaN(parseInt(num / base)) || parseInt(num / base) === 0) {
      return '0123456789abcdef'[num % base];
    } else {
      return '0123456789abcdef'[parseInt(num / base)] + convert(num % base);
    }
  };
};
