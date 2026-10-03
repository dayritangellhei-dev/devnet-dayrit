"""
Module 2 — Lesson 4: Functions
Student: Angel Lhei D. Dayrit
Date: 10/3/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Functions are like custom shortcut buttons on a microwave or phone. 

Instead of typing out 10 lines of steps every time you need to do a task, 
you package those steps into a named block of code once. Whenever you 
need that task done, you just "call" the function by its name, give it 
any necessary inputs, and let it do the work.
============================================
KEY VOCABULARY
============================================
- function: A named, reusable block of code that performs a specific task.
- def: The Python keyword used to create a function.
- parameter: A variable inside the function definition that expects input.
- argument: The actual value you pass into the function when calling it.
- return: The keyword that sends a result back out from the function to your main code.

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""
def calculate_total(price, quantity):
    return price * quantity

final_total = calculate_total(15, 3)

print("Total price: " + str(final_total))

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
Confusing print() with return.

- print() just shows text on the screen for you to see.
- return actually gives the result back so your program can save 
  and use it in other variables or calculations.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
