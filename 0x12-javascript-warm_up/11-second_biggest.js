#!/usr/bin/node
// Script that searches the second biggest integer in the list of arguments.

const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  const sortedArgs = args.map(Number).sort((a, b) => b - a);
  console.log(sortedArgs[1]);
}
