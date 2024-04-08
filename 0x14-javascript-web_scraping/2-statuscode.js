#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, Response, body) => {
  if (error) {
    return;
  }
  console.log('code:', Response.statusCode);
});
