#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2]; // The first argument passed to the script

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    // If an error occurs, print the error object
    console.error(err);
  } else {
    // If no error, print the content of the file
    console.log(data);
  }
});
