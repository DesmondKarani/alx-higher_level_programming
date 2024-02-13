#!/usr/bin/node
// Import the dict from 101-data.js
const dict = require('./101-data').dict;

// Convert the dictionary into an array of [key, value] pairs
const totalist = Object.entries(dict);

// Extract the values from the dictionary
const vals = Object.values(dict);

// Create a unique set of values to eliminate duplicates, then convert back to array
const valsUniq = [...new Set(vals)];

// Initialize an empty object for the new dictionary
const newDict = {};

// Iterate over each unique value
for (const j in valsUniq) {
  const list = []; // Initialize a list to hold keys corresponding to the current value
  // Iterate over the total list of [key, value] pairs
  for (const k in totalist) {
    // Check if the current pair's value matches the unique value we're focusing on
    if (totalist[k][1] === valsUniq[j]) {
      // If so, add the key to the list for this unique value
      list.unshift(totalist[k][0]);
    }
  }
  // Assign the list of keys to the unique value in the new dictionary
  newDict[valsUniq[j]] = list;
}

// Print the newly constructed dictionary
console.log(newDict);
