#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv[2];

fs.readFile(filepath, 'utf8', (error, Data) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  console.log(Data);
});
