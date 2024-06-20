#!/usr/bin/node
// Script that passed:

const n = process.argv[2];

function fac (n) {
  if (n <= 1 || isNaN(n)) {
    return 1;
  } else {
    return n * fac(n - 1);
  }
}

console.log(fac(n));
