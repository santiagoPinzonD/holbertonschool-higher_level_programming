#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/people/18/';
request.get(url, function (err, response, body) {
  err = 0;
  response = '';
  const json = JSON.parse(body);
  const array = json.films;
  console.log(array.length);
});
