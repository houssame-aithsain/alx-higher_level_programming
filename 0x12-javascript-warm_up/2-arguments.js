#!/usr/bin/node
// Access command line arguments (excluding the first two)

const arg = process.argv.slice(2);

if (arg.length === 0) {
  console.log("No argument");
} 
else if (arg.length === 1 ){
  console.log("Argument found");
}
else {
  console.log("Arguments found");
}
