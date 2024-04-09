#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const antiId = '18';

request.get(url, (error, Response, body) => {
  if (error) {
    return;
  }
  const movie = JSON.parse(body).results;
  const a = movie.filter(function (el) {
    return el.characters.includes(`https://swapi-api.alx-tools.com/api/people/${antiId}/`);
  });
  console.log(a.length);
});
