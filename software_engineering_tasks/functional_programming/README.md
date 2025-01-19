This is a small program for demonstrating principles of **functional programming**. It processes a list of numbers and applies various transformations, such as:

Filtering out even numbers. \
Doubling the odd numbers. \
Summing up the results. 

Pure Functions:

is_odd, double, and square are pure functions because they do not have side effects and always produce the same output for the same input.

Higher-Order Functions:

apply_function_to_list is a higher-order function because it takes a function (fn) as an argument and applies it to each element in the numbers list.

Immutability:

The numbers list and all the transformations (odd_numbers, doubled_odds, and squared_odds) are immutable in the sense that no elements are modified in place. Instead, new lists are created with the transformed data.

I also added some **unit tests**. I used Python's built-in unittest framework to test the core functions and the higher-order function. test.py includes:

Tests for each individual function (is_odd, double, square)
Tests for the higher-order function apply_function_to_list
A full workflow test that verifies the entire chain of operations
Edge cases like negative numbers and empty lists

To run the tests:

```
python -m unittest test.py
```

This is what I got:

<img width="497" alt="Image" src="https://github.com/user-attachments/assets/96bfd6ff-d7df-413a-b066-5a691b43817f" />

All the tests passed. '.' represents a passing test, OK means all tests passed successfully. If any test had failed, there would be an F. The code is working exactly as expected!

Used Claude, prompt "I have this program: 'my program'. Help me write simple unit tests for it".
