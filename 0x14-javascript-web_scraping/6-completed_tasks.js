#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2]; // The API URL

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    return;
  }
  
  const todos = JSON.parse(body);
  const completedTasks = {};

  todos.forEach(task => {
    if (task.completed) {
      if (completedTasks[task.userId]) {
        completedTasks[task.userId] += 1;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
  });

  console.log(completedTasks);
});
