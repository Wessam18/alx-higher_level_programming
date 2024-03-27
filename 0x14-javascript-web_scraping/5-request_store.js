#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];
const writeStream = fs.createWriteStream(filePath);

request(url, (err, resp, data) => {
  if (err) {
    console.log(err);
  }

  writeStream.write(data);
  writeStream.end();
});
