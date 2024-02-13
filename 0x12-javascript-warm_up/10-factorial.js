#!/usr/bin/node

const args = +process.argv[2];

function factorial (num) {
  if (num === 0 || isNaN(num)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const fact = factorial(args);

console.log(fact);
