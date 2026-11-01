# Day 4: Iteration -- find the first index
# Work top to bottom: PREDICT -> RUN -> INVESTIGATE -> MODIFY.
# Edit this file as you go.
#
# Working habit: Trace, predict, explain (today: trace each iteration)

# ==================== PREDICT ====================
# Fill in EVERY "Prediction:" below before you run anything.

# Goal: when a phone number has a character that doesn't belong, the sign-up
# form points to it. first_bad_char returns the position of the FIRST
# character that isn't a digit or one of ( ) - . + space, or -1 if there is none:
#   "718-555-0142 cell" --> 13
#   "(718) 555-0142"    --> -1

ALLOWED = "()-. +"

# Positions in "718-555-0142 cell":
#     7   1   8   -   5   5   5   -   0   1   4   2       c   e   l   l
#     0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16


def first_bad_char(raw):
    for i in range(len(raw)):
        if not (raw[i].isdigit() or raw[i] in ALLOWED):
            return i
    return -1


print("A:", first_bad_char("718-555-0142 cell"))
"""
raw = "718-555-0142 cell"

iterations 1-13/17: i = 0 to 12, raw[i] is a digit, "-" or " ", all allowed

iteration 14/17:
- i = 13
- raw[13] = "c"
- raw[13].isdigit() -> False
- raw[13] in ALLOWED -> False
- not (False or False) -> True
- return 13   (the loop stops; iterations 15-17 never run)

print("A:", 13)
"""
# Prediction:
# Actual:
# Explanation:

print("B:", first_bad_char("(718) 555-0142"))
"""
raw = "(718) 555-0142"

iteration 1/?:
"""
# Prediction:
# Actual:
# Explanation:


# A teammate tried three other versions. Each one changes one thing.

def first_bad_char_c(raw):
    for i in range(len(raw)):
        if not (raw[i].isdigit() or raw[i] in ALLOWED):
            return i
        else:
            return -1


def first_bad_char_d(raw):
    bad = -1
    for i in range(len(raw)):
        if not (raw[i].isdigit() or raw[i] in ALLOWED):
            bad = i
    return bad


def first_bad_char_e(raw):
    for ch in raw:
        if not (ch.isdigit() or ch in ALLOWED):
            return ch
    return -1


print("C:", first_bad_char_c("718-555-0142 cell"))
"""
raw = "718-555-0142 cell"

iteration 1/?:
"""
# Prediction:
# Actual:
# Explanation:

print("D:", first_bad_char_d("718-555-0142 cell"))
"""
raw = "718-555-0142 cell"
bad = -1

iteration 1/?:
"""
# Prediction:
# Actual:
# Explanation:

print("E:", first_bad_char_e("718-555-0142 cell"))
"""
raw = "718-555-0142 cell"

iteration 1/?:
"""
# Prediction:
# Actual:
# Explanation:


# ==================== MODIFY ====================
# One change at a time. Run after each one.
#
# 1. Use first_bad_char to print the form's error message:
#    Unexpected "c" at position 13
#    For "(718) 555-0142" print: Looks good
#
# 2. In the REPL, try "718-555-0142 cell".find("c"). It matches A.
#    Write one sentence: why can't .find() replace first_bad_char for
#    "718-555-0142 ext 12"?
#
# 3. From memory: write normalize_phone(raw) that keeps only the digits,
#    building a new string. normalize_phone("(718) 555-0142") --> "7185550142"
