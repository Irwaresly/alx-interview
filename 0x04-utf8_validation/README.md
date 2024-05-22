# UTF-8 Validation

## Overview

This project focuses on validating whether a given dataset represents a valid UTF-8 encoding using Python programming skills, bitwise operations, and an understanding of the UTF-8 encoding scheme.

## Concepts and Resources

- **Bitwise Operations in Python**: Understanding how to manipulate bits in Python.
- **UTF-8 Encoding Scheme**: Familiarity with UTF-8 encoding rules and patterns.
- **Data Representation**: Handling data at the byte level.
- **List Manipulation in Python**: Iterating through lists and list comprehensions.
- **Boolean Logic**: Applying logical operations for decision-making.

## Project Tasks

### Task 0: UTF-8 Validation

Write a method `validUTF8(data)` to determine if a given dataset represents a valid UTF-8 encoding.

- Return `True` if data is a valid UTF-8 encoding, else return `False`.
- A character in UTF-8 can be 1 to 4 bytes long.
- The data set can contain multiple characters.
- Each integer in the data list represents 1 byte of data, so handle only the 8 least significant bits of each integer.


