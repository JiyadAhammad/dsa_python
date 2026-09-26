"""
227. Basic Calculator II

Given a string s which represents an expression,
evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid.
All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function
which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5
"""

"""
The BODMAS Rule is a simple guide that tells you the correct order to 
solve math problems with more than one operation.
What BODMAS Stands ForThe letters stand for the steps you must follow 
in order:
B - Brackets: Solve anything inside brackets ( ), { }, [ ] first.
O - Orders: Next, solve powers, indices, or square roots.
D - Division and 
M - Multiplication: Do these operations from left to right as they appear. 
    They have equal priority.
A - Addition and 
S - Subtraction: Do these operations last, also working from left to right. 
    They also have equal priority.
"""
