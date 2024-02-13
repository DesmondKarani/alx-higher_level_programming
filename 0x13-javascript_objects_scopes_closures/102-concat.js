#!/usr/bin/node
const fs = require('fs');

// Grab command line arguments for file paths
const [,, fileA, fileB, fileC] = process.argv;

// Read the content of the first file
fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) throw err;

  // Read the content of the second file
  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) throw err;

    // Concatenate the content of both files and write to the destination file
    fs.writeFile(fileC, dataA + dataB, 'utf8', (err) => {
      if (err) throw err;
    });
  });
});
