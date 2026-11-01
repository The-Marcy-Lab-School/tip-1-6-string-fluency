# Day 3: Comparison and `in` -- validating a sign-up form
# Work top to bottom: PREDICT -> RUN -> INVESTIGATE -> MODIFY.
# Edit this file as you go.
#
# Working habit: Trace, predict, explain (today: hypothesize -- when a prediction
# is wrong, name the line and what you believed: "I thought ___, but Python ___")

"""
A phone number is valid when:
  1. it has only digits and these characters: ( ) - . + and space
  2. after cleaning, it has exactly 10 digits
  3. the area code doesn't start with 0 or 1
"""

ALLOWED = "()-. +"


# A working cleaner (you'll write your own on Day 5).
def normalize_phone(raw):
    digits = ""
    for ch in raw:
        if ch.isdigit():
            digits += ch
    if len(digits) == 11 and digits[0] == "1":
        digits = digits[1:]
    return digits


# ---------------------------------------------------------------
# PREDICT: A teammate wrote these two helpers. Trace, predict, then run.
# ---------------------------------------------------------------

# Goal: only_phone_chars says whether EVERY character is allowed:
#   "(718) 555-0142" --> True,  "718-555-0142 cell" --> False
# area_code_ok says whether the area code doesn't start with 0 or 1:
#   "7185550142" --> True,  "0185550142" --> False

def only_phone_chars(raw):
    for ch in raw:
        if ch.isdigit() or ch in ALLOWED:
            return True
        else:
            return False


def area_code_ok(digits):
    if digits[0] == "0" or "1":
        return False
    return True


print(only_phone_chars("(718) 555-0142"))     # expected True
"""
raw = "(718) 555-0142"

iteration 1/14:
- ch = "("
- ch.isdigit() -> False
- ch in ALLOWED -> True
- False or True -> True
- return True

print(True)
"""
# Prediction:
# Actual:

print(only_phone_chars("718-555-0142 cell"))  # expected False
"""
raw = "718-555-0142 cell"

iteration 1/?:
"""
# Prediction:
# Actual:

print(only_phone_chars("call me"))            # expected False
"""
raw = "call me"

iteration 1/?:
"""
# Prediction:
# Actual:

print(only_phone_chars(""))                   # expected True (no bad characters)
"""
raw = ""

iteration 1/?:
"""
# Prediction:
# Actual:

print(area_code_ok("7185550142"))             # expected True
"""
digits = "7185550142"

1.
"""
# Prediction:
# Actual:

print(area_code_ok("0185550142"))             # expected False
"""
digits = "0185550142"

1.
"""
# Prediction:
# Actual:

# Explanation (one sentence per helper):
#


# ---------------------------------------------------------------
# MODIFY 3: Your validator. Use normalize_phone and both fixed helpers.
# ---------------------------------------------------------------

# In:
# Out:


def is_valid_phone(raw):
    return True  # replace this line


# print(is_valid_phone("(718) 555-0142"))     # expected True
# print(is_valid_phone("+1 347 555 0199"))    # expected True
# print(is_valid_phone("718-555-0142 cell"))  # expected False
# print(is_valid_phone("212-555-01"))         # expected False
# print(is_valid_phone("(018) 555-0142"))     # expected False
# print(is_valid_phone(""))                   # expected False
