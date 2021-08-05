#!/usr/bin/node
const Dict = require('./101-data').dict;
const newD = {};
for (const key in Dict) {
  if (newD[Dict[key]] === undefined) {
    newD[Dict[key]] = [key];
  } else {
    newD[Dict[key]].push(key);
  }
}
console.log(newD);
