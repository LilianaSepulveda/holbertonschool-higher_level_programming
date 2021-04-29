#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if argv[2] != "+" and argv[2] != "-" and argv[2] != "*" and argv[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if argv[2] == "+":
        calculate = add(a, b)
    if argv[2] == "-":
        calculate = sub(a, b)
    if argv[2] == "*":
        calculate = mul(a, b)
    if argv[2] == "/":
        calculate = div(a, b)
    print("{} {} {} = {}".format(a, sys.argv[2], b, calculate))
