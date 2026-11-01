# Day 2: Slicing -- phone numbers on a contact card
# Work top to bottom: PREDICT -> RUN -> INVESTIGATE -> MODIFY.
# Edit this file as you go.
#
# Working habit: Trace, predict, explain (today: trace)

# ==================== PREDICT ====================
# Fill in EVERY "Prediction:" below before you run anything.

# Goal: a contact card shows a clean 10-digit number the way people read it:
#   "7185550142" --> "(718) 555-0142"
# and a receipt shows only the last 4 digits:
#   "7185550142" --> "(***) ***-0142"

# Positions in "7185550142":
#     7   1   8   5   5   5   0   1   4   2
#     0   1   2   3   4   5   6   7   8   9


def format_phone(digits):
    return "(" + digits[:3] + ") " + digits[3:6] + "-" + digits[6:]


def mask_phone(digits):
    return "(***) ***-" + digits[-4:]


print("A:", format_phone("7185550142"))
"""
digits = "7185550142"

1. digits[:3]  -> positions 0, 1, 2      -> "718"
2. digits[3:6] -> positions 3, 4, 5      -> "555"
3. digits[6:]  -> positions 6 to the end -> "0142"
4. "(" + "718" + ") " + "555" + "-" + "0142" -> "(718) 555-0142"

print("A:", "(718) 555-0142")
"""
# Prediction:
# Actual:
# Explanation:

print("B:", mask_phone("7185550142"))
"""
digits = "7185550142"

1.
"""
# Prediction:
# Actual:
# Explanation:

print("C:", format_phone("17185550142"))
"""
digits = "17185550142"     (someone typed the country code)

1.
"""
# Prediction:
# Actual:
# Explanation:

print("D:", mask_phone("17185550142"))
"""
digits = "17185550142"

1.
"""
# Prediction:
# Actual:
# Explanation:

print("E:", format_phone("718 555 0142"))
"""
digits = "718 555 0142"     (never cleaned)

1.
"""
# Prediction:
# Actual:
# Explanation:


# ==================== MODIFY ====================
# One change at a time. Run after each one.
#
# 1. Make format_phone drop a leading country code: if digits has 11 characters
#    and starts with "1", keep everything after the first character.
#    C should now print (718) 555-0142.
#
# 2. Write parse_phone(digits) that returns the three named parts:
#    parse_phone("3475550199") --> {'area': '347', 'exchange': '555', 'line': '0199'}
#    Get the line with a negative slice.
#
# 3. Write same_last_four(a, b): two numbers that end in the same 4 digits.
#    same_last_four("7185550142", "17185550142") --> True
#    same_last_four("7185550142", "3475550199")  --> False
