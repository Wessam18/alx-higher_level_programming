#!/usr/bin/node

const arg = process.argv;

if (+arg[2]) {
  console.log('My number: '+arg[2]);
} else {
  console.log('Not a number');
}
