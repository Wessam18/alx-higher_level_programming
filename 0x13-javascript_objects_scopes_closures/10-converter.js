#!/usr/bin/node

exports.converter = function (base) {
  function toconvert (number) {
    return (number.toString(base));
  }
  return (toconvert);
};
