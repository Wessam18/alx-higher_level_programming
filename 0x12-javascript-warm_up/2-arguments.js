#!/usr/bin/node

const arg = process.argv;
const aargs = arg.length;

if (aargs === 2) {
  console.log('No argument');
} else if (aargs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
