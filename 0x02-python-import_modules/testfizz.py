#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        print("FizzBuzz ", end="") if number % 3 == 0 and number % 5 == 0 else ((print("Fizz ", end="") if number % 3 == 0 else print("Buzz ", end="") if number % 5 == 0 else print("{} ".format(number), end=""))
