#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const tasks = JSON.parse(body);
  const completedTasks = tasks.reduce((acc, task) => {
    if (task.completed) {
      if (!acc[task.userId]) {
        acc[task.userId] = 0;
      }
      acc[task.userId] += 1;
    }
    return acc;
  }, {});

  console.log(completedTasks);
});
