Week 1: Conditions – recommendations.py
In this lesson, I learned how to use conditional statements (if, elif, else) to control the flow of a program based on user input.

The script asks the user to choose the difficulty level (Difficult or Casual) and the number of players (Multiplayer or Single-player). Based on their choices, it recommends a card game using a function called recommend().

I practiced using nested if statements, creating functions, and handling invalid input by printing error messages.

What I learned:

How to take input from the user using input()

How to use if, elif, and else for branching logic

How to call a function with a parameter

How to give useful feedback when the input is invalid

######################################################################

in this lesson, I learned how to use if not to validate user input early in the program. By checking whether the input is not one of the expected values, I can give feedback and exit the function early using return. This helps avoid deeply nested conditions and keeps the main logic cleaner.

I also reinforced how to:

Use or inside if not (...) for validation

Simplify logic by removing unnecessary else blocks

Make the code more readable and robust

######################################################################################

This part contains beginner Python problem sets that helped me practice foundational programming concepts, such as conditionals, string methods, type conversion, and user input handling.

📁 deep.py
Inspired by The Hitchhiker’s Guide to the Galaxy, this program checks whether the user's answer to the ultimate question of life is "42", "forty-two", or "forty two" (case-insensitive).
✅ What I practiced:

Normalizing input with .strip() and .lower()

Comparing multiple acceptable answers

Simple conditional logic

📁 bank.py
Inspired by a Seinfeld episode, this program evaluates greetings. If a user enters a greeting starting with "hello", it returns R0; if it starts with any "h" word (like “hey”), it returns R20; otherwise, R100.
✅ What I practiced:

String methods like .strip() and .lower()

Input validation using if and startswith()

Using local currency (Rands) in outputs

📁 extensions.py
This script maps file extensions (e.g., .jpg, .pdf, .txt) to their correct MIME/media type. If unknown, it defaults to application/octet-stream.
✅ What I practiced:

Input normalization

File type detection using .endswith()

Using elif chains for clean condition handling

📁 interpreter.py
A mini math interpreter that takes an arithmetic expression (like 3 + 4) from the user and evaluates the result, printing it to 1 decimal place.
✅ What I practiced:

Splitting and unpacking strings with .split()

Type casting (int())

Float formatting with f"{result:.1f}"

📁 meal.py
A meal-time checker that tells you if it's breakfast, lunch, or dinner time based on a time input in 24-hour format.
✅ What I practiced:

Creating and using helper functions (convert)

Time conversion (e.g., "7:30" → 7.5)

Range-based conditionals

🚀 What I’ve Learned So Far
String methods: .strip(), .lower(), .split(), .startswith(), .endswith()

Conditional logic: if, elif, else

Function creation and use

Basic math and type conversion

Formatting output using f-strings

