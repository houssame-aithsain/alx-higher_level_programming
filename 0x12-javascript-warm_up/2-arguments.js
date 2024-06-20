#!/usr/bin/node
// Access command line arguments (excluding the first two)

const args = process.argv[2];

// Check the number of arguments
if (args.length === 0) {
  console.log("No argument");
} 
else if (args.length === 1 ){
  console.log("Argument found");
}
else {
  console.log("Arguments found");
}
