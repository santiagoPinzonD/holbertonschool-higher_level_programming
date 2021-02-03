#!/usr/bin/node
const argv1 = parseInt(process.argv[2]);
if (!isNaN(argv1)) {
  console.log('My number:', argv1);
} else {
  console.log('Not a number');
}
