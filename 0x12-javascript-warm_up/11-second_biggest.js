#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  let numbers = process.argv.slice(2).map(Number);
  numbers = numbers.sort(function (a, b) { return b - a; });
  console.log(numbers[1]);
}
