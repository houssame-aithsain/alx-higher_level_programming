#!/usr/bin/node
// Script that passed:

function f (n) {
    if (n === 1) {
      return (1);
    }
    return (n * f(n - 1));
}
  
const args = process.argv;

if (isNaN(args[2])) {
  console.log('1');
}
else {
  let num = f(parseInt(args[2], 10));
  console.log(num);
}
