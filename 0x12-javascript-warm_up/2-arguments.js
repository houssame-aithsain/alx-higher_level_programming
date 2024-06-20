#!/usr/bin/node
// Script that passed:

const args = process.argv.slice(2);

// If no argument passed to the script, print “No argument”
if (args.length === 0) {
  console.log("No argument");
} 
else if (args.length === 1 ){
  console.log("Argument found");
}
else {
  console.log("Arguments found");
}
