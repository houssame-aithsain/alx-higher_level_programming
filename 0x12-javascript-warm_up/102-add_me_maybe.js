#!/usr/bin/node
// script that increments and calls a function.

exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
