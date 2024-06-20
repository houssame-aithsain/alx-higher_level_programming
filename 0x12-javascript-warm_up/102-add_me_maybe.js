#!/usr/bin/node
// script that increments and calls a function.

exports.callMeMoby = function (number, theFunction) {
  theFunction(++number);
};
