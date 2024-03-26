#!/usr/bin/node

const request = require('request');
const url = process.argv[2]; // The URL is the first argument

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  } else {
    console.log('code:', response && response.statusCode); // Print the response's status code.
  }
});
