#!/usr/bin/node
// Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

const { dict } = require('./101-data');

const occurrences = {};

for (const userId in dict) {
  const occurrencesCount = dict[userId];
  if (occurrences[occurrencesCount]) {
    occurrences[occurrencesCount].push(userId);
  } else {
    occurrences[occurrencesCount] = [userId];
  }
}

console.log(occurrences);
