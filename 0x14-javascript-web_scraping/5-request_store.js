#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const { json } = require('stream/consumers');

const url = process.argv[2];
const filePath = process.argv[3];
const writeStream = fs.createWriteStream(filePath);

request(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  }
  const x = JSON.parse(body);

  writeStream.write(x.data);
  writeStream.end();
});
