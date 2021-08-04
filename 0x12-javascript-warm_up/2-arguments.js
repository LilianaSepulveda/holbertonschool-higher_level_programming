#!/usr/bin/node
const ArgPass = process.argv.length;
if (ArgPass === 2) {
  console.log('No argument');
} else if (ArgPass === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
