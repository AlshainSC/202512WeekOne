#!/usr/bin/env python3
"""
Test script for calculator operations.
"""

from calculator.operations import add, subtract, multiply, divide

print("Testing Calculator Operations")
print("-----------------------------")
print(f"add(5, 3) = {add(5, 3)}")
print(f"subtract(10, 4) = {subtract(10, 4)}")
print(f"multiply(7, 2) = {multiply(7, 2)}")
print(f"divide(20, 5) = {divide(20, 5)}")
print(f"divide(10, 0) = {divide(10, 0)}")
