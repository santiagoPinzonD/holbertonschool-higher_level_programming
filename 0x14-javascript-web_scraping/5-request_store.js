#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const fs = require('fs');
const filePath = process.argv[3];
request.get(url, function (err, response, body) {
  err = 0;
  response = '';
  const data = body.toString();
  fs.writeFile(filePath, data, (err) => {
    if (err) { console.log(err); }
  });
});
