#!/usr/bin/node

const arg = process.argv;

function add (a, b) {
  console.log(a + b);
}

add(+arg[2], +arg[3]);
