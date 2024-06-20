#!/usr/bin/node
// Access command line arguments (excluding the first two)

const count = process.argv.length;

// Check the number of arguments
if (count === 0) {
  console.log("No argument");
} 
else if (count === 1 ){
  console.log("Argument found");
}
else {
  console.log("Arguments found");
}
