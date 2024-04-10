#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];
const writeStream = fs.createWriteStream(filePath);

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  writeStream.write(data);
  writeStream.end();
});
