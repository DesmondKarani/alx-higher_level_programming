#!/usr/bin/node
// 9-logme.js
let printCount = 0;

exports.logMe = function (item) {
  console.log(`${printCount}: ${item}`);
  printCount++;
};
