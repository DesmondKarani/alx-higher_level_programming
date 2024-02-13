#!/usr/bin/node
// Import the list from the file
const { list } = require('./100-data.js');

// Use map to create a new list where each value is multiplied by its index
const newList = list.map((value, index) => value * index);

// Print both lists
console.log(list);
console.log(newList);
