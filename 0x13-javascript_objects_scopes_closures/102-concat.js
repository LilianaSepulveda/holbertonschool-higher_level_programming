#!/usr/bin/node
const fs = require('fs');
const 1 = fs.readFileSync(process.argv[2], 'r');
const 2 = fs.readFileSync(process.argv[3], 'r');
fs.writeFileSync(process.argv[4], 1 + 2);
