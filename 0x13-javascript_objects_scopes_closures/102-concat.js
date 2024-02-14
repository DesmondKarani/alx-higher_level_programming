#!/usr/bin/node
// Import the fs module to work with the file system
const fs = require('fs');

// Read the content of the first file synchronously, converting it to a string
const fArg = fs.readFileSync(process.argv[2]).toString();

// Read the content of the second file synchronously, converting it to a string
const sArg = fs.readFileSync(process.argv[3]).toString();

// Write the concatenated content of the first and second files to the destination file
fs.writeFileSync(process.argv[4], fArg + sArg);
