# Chapter 7 notes
______
**Loop Structures and Booleans**

Concepts to learn:
* Definite and indefinite loops
* Interactive loop programming pattern
* sentinel loop programming pattern
* Basic ideas of boolean algebra

## Review Questions
### True/False
1. A Python `while` loop implements a definite loop.
   1. False. The number of iterations of the loop is unknown,
2. The counted loop pattern uses a definite loop.
   1. True. The number of iterations is known beforehand
3. A sentinel loop asks the user whether to continue on each iteration
   1. False - a sentinel loop continues iterations until a sentinal value triggers termination.
4. A sentinel loop sould not actualy process the sentinel value
   1. True. The loop terminates upon reading the sentinel value
5. The `checkMouse` method does not wait for the user to click the mouse
   1. True. It returns a value (including `none`) based on the last mouse click.
6. A `while` loop is a post-test loop.
   1. False. A `while` loop checks the condition before beginning the loop, meaning if the condition for termination is met before the loop begins, the loop will never actually begin. A pre-test loop is c's `do-while` loop.
7. The Boolean operator `or` returns `True` when both of its operands are true.
   1. This is True, through it's not the only condition under which the `or` operator returns `True`.
8. a and (b or c) == (a and b) or (a and c)
   1. True
9. not (a or b) == (not a) or not(b)
   1.  False

### Multiple Choice
1. A loop pattern that asks the user whether to continue on each iteration is called a(n):
   1. interactive loop
2. A loop pattern that continues until a special value is input is called a(n):
   1. Sentinel loop
3. A loop structure that tests the loop condition after executing the loop body is called a:
   1. post-test loop
4. A priming read is part of the pattern for a(n)
   1. Sentinel loop
5. What statement can be executed in the body of a loop to cause it to terminate
   1. break
6. Which of the following is not a valid rule of Boolean algebra
   1. not(a and b) == not(a) and not(b)
7. A loop that never terminates is called
   1. infinite
8. Which line would not be found in a truth table for `and`
   1. TFT
9. Which line would not be found in a truth table for `or`
   1. FTF
10. The term for an operator that may not evaluate one of its subexpressions is:
    1.  short-circuit