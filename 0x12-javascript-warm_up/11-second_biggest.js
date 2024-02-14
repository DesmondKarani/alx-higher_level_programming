#!/usr/bin/node
let args = process.argv.slice(2).map(Number); // Convert arguments to numbers, ignoring the first two entries
args = [...new Set(args)]; // Remove duplicates to handle edge cases
args.sort((a, b) => b - a); // Sort numbers in descending order
console.log(args.length > 1 ? args[1] : 0); // Print second biggest or 0
