#!/usr/bin/node

const { error } = require('console');
const fs = require('fs');

fs.readFile(process.argv[1], 'utf8', (error, Data) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  console.log(Data);
});
