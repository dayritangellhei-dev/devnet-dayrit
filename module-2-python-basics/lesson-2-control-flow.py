"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Angel Lhei D. Dayrit
Date: 9/30/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Control flow is how your computer makes decisions. It's like a 
flowchart for your code: "IF this is true, do step A. ELSE IF 
something else is true, do step B. OTHERWISE, do step C." 

It lets your program choose different paths instead of running 
the exact same lines every time.

============================================
KEY VOCABULARY
============================================
- condition: A question or rule that results in either True or False.
- if / elif / else: statement for code to make decisions based on conditions
using if, elif, else. It checks conditions from top to bottom, and otherwise runs else.
- comparison operator: Symbols used to compare values.
- boolean expression: True or false value as a result.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---
passenger_type = "student"

if passenger_type == "student":
    fare = 13
    print(f"Student Fare: {fare}")
elif passenger_type == "regular":
    fare = 15
    print(f"Regular Fare: {fare}")
else:
    fare = 10
    print(f"Regular Fare: {fare}")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]
Confusing = with ==
because = is used to assign value
and == is used to compare values

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
