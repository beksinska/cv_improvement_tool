#Pure function: Returns a transformed value, no side effects.
def is_odd(number):
    return number % 2 != 0

def double(number):
    return number * 2

def square(number):
    return number * number

#Higher-order function: Takes other functions as arguments.
def apply_function_to_list(fn, numbers):
    return [fn(n) for n in numbers]

#Immutability: Only immutable data structures.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Filter out even numbers (pure function).
odd_numbers = list(filter(is_odd, numbers))
print("Odd numbers:", odd_numbers)

#Double the odd numbers (higher-order function).
doubled_odds = apply_function_to_list(double, odd_numbers)
print("Doubled odd numbers:", doubled_odds)

#Apply a transformation and sum the results (composing functions).
squared_odds = apply_function_to_list(square, odd_numbers)
sum_of_squares = sum(squared_odds)
print("Sum of squares of odd numbers:", sum_of_squares)
