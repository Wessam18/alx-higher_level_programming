#!/usr/bin/node

const fs = require('fs');
const args = process.argv[2];

try {
  const data = fs.readFileSync(args, 'utf-8');
  console.log(data);
} catch (err) {
  console.log(err);
}
