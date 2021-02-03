#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log('0');
} else {
  args.sort(function (a, b) {
    return a - b;
  });
  const arrayNew = args.slice(args.length - 2);
  console.log(arrayNew[0]);
}
