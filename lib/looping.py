#!/usr/bin/env python3
def happy_new_year():
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")

happy_new_year()

    
    

def square_integers(numbers):
    squared_numbers = [num ** 2 for num in numbers]
    return squared_numbers





    
def fizzbuzz(n):
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Example usage:
fizzbuzz(100)

