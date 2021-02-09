#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
request.get(url, function (err, response, body) {
  err = 0;
  response = '';
  const json = JSON.parse(body);
  console.log(json.title);
});
