#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const data = process.argv[3];

try {
  fs.writeFileSync(filePath, data, 'utf-8');
} catch (err) {
  console.log(err);
}
