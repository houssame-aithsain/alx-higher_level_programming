#!/usr/bin/node
// Access command line arguments (excluding the first two)

if (process.argv[2] === undefined) {
    console.log('No argument');
  } else {
    console.log(process.argv[2]);
  }
