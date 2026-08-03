# Use this file to try out the examples as you work through the lab.
# Type them in, run the file, then clear it out and use it again for the next one.
#
# Run it from the terminal with:   python exercise.py
# On Windows you may need:         py exercise.py
#
# Nothing in this file is marked, so experiment as much as you like.
# Numeric data types
age = 21                    # int (integer)
height = 5.9               # float (floating-point number)
temperature = -15.5        # float (can be negative)

# String data type
student_name = "Muhammad Ali"    # str (string)
course_title = 'Python Programming'  # str (single or double quotes)
description = """This is a multi-line
string that spans several lines."""   # str (triple quotes)

# Boolean data type
is_active = True           # bool (boolean)
has_submitted = False      # bool (boolean).

# Special data type
nothing = None             # NoneType (represents absence of value)
print(type(age))
print(type(temperature))
print(type(student_name))
print(type(is_active))
print(type(nothing))
print(type(25))
print(type("25"))
number_text = "25"
print(type(number_text))

real_number = int(number_text)
print(type(real_number))
text = "Hello World"

# len() is a function, so the value goes inside the brackets
print(len(text))          # 11

# upper() and lower() are methods, so the value comes before the dot
print(text.upper())       # HELLO WORLD
print(text.lower())       # hello world