This is a small program for demonstrating principles of functional programming.It processes a list of numbers and applies various transformations, such as:

Filtering out even numbers.
Doubling the odd numbers.
Summing up the results.

Pure Functions:

is_odd, double, and square are pure functions because they do not have side effects and always produce the same output for the same input.

Higher-Order Functions:

apply_function_to_list is a higher-order function because it takes a function (fn) as an argument and applies it to each element in the numbers list.

Immutability:

The numbers list and all the transformations (odd_numbers, doubled_odds, and squared_odds) are immutable in the sense that no elements are modified in place. Instead, we create new lists with the transformed data.