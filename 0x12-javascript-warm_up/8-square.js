#!/usr/bin/node
const argv1 = parseInt(process.argv[2]);
let height;
let weight;
if (isNaN(argv1)) {
  console.log('Missing size');
} else {
  for (height = 0; height < argv1; height++) {
    for (weight = 0; weight < argv1; weight++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
