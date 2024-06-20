#!/usr/bin/node
// Script that prints My number

const arg = process.argv[2];
if (Number.isInteger(parseInt(arg))) {
  console.log('My number:', parseInt(arg));
} else {
  console.log('Not a number');
}
