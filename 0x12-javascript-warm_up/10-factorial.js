#!/usr/bin/node
const integer = parseInt(process.argv[2]);
if (integer) {
  console.log(factorial(integer));
} else {
  console.log('1');
}
function factorial (a) {
  if (a <= 1) {
    return (1);
  }
  return a * factorial(a - 1);
}
