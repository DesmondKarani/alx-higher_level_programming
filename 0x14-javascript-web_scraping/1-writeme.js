#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2]; // The file path is the first argument
const content = process.argv[3]; // The string to write is the second argument

fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    // If an error occurs, print the error object
    console.error(err);
  }
});
