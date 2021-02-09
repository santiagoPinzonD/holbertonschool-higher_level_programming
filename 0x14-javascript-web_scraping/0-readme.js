#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
fs.readFile(file, (error, datos) => {
  if (error) {
    console.log(error);
  } else {
    console.log(datos.toString());
  }
});
