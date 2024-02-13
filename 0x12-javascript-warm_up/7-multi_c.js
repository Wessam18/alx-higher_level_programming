#!/usr/bin/node

const arg = process.argv;
const x = arg[2];

if (+x) {
  for (let i = 1; i <= +x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
