"""
Module 2 — Lesson 3: Loops & Lists
Student: Angel Lhei D. Dayrit
Date: 10/3/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
A list is like a digital notebook page where you store multiple items 
under one single variable name, it could be something like a grocery list.

Then A loop is like setting an automated timer that performs an action repeatedly. 
Instead of typing the same code 10 times, a loop tells the computer, 
"Do this step for every item on my list until I run out."
============================================
KEY VOCABULARY
============================================
- list: An ordered collection of items stored inside square brackets `[]`.
- for loop: A loop used to repeat code a specific number of times or iterate 
  over every item in a list.
- while loop: A loop that keeps repeating as long as a specific condition 
  remains True.
- index: The position number of an item in a list (starting at 0).
- iteration: One single repetition or pass through a loop.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

grocery_list = ["Rice", "Eggs", "Cooking Oil", "Coffee"]

print("--- Items to Buy ---")
for item in grocery_list:
    print(f"- {item}")

print("\nTotal items:", len(grocery_list))




"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
something that is easy to mistake here is when trying to call out an index from a list,
for example I want to call out coffee from my list, doing [4] would actually cause an error
because index starts from zero.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
