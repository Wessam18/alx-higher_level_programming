#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  const movies = JSON.parse(body).results;
  let num = 0;
  movies.forEach(element => {
    if (element.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      num++;
    }
  });
  console.log(err || num);
});
