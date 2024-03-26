#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2]; // The URL from which to fetch the content
const filePath = process.argv[3]; // The file path to store the content

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    return;
  }
  // Write the body of the response to the specified file
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
