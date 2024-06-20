#!/usr/bin/node
// Write a function that increments a value and calls a function.

const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

myObject.incr = function () {
  this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
