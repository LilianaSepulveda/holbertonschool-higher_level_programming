#!/usr/bin/node
const ArgPass = Number(process.argv[2]);
function factorial (nb) {
  return nb === 0 || isNaN(nb) ? 1 : nb * factorial(nb - 1);
}
console.log(factorial(ArgPass));
