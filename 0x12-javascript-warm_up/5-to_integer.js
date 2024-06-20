#!/usr/bin/node
// Script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer

const arg = process.argv[2];
if (Number.isInteger(parseInt(arg))) {
  console.log('My number:', parseInt(arg));
} else {
  console.log('Not a number');
}
