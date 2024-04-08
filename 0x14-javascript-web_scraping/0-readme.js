#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (error, Data) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  console.log(Data);
});
