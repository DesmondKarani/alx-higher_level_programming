#!/usr/bin/node
// Import the list from the file
const list = require('./100-data.js').list;
// Print both lists
console.log(list);
console.log(list.map((item, index) => item * index));
