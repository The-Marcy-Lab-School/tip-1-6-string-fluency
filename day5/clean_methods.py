# Day 5: Looking up string methods -- cleaning what people type
# Work top to bottom: PREDICT -> RUN -> INVESTIGATE -> MODIFY.
# Edit this file as you go.
#
# Working habit: Trace, predict, explain (today: test one change -- when you're
# not sure what a method does, change one thing in the REPL and run it)

# ==================== PREDICT ====================
# Fill in EVERY "Prediction:" below before you run anything.

# Goal: a phone number pasted into the sign-up form arrives with extra spaces
# and punctuation. Clean it with string methods:
#   " (718) 555-0142 " --> "7185550142"
# Each print puts [ ] around the result so you can see spaces at the edges.

raw = " (718) 555-0142 "

# Positions in raw:
#         (   7   1   8   )       5   5   5   -   0   1   4   2
#     0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15

print("A: [" + raw.strip() + "]")
"""
raw = " (718) 555-0142 "

1. raw.strip() -> a NEW string without the spaces at both ends -> "(718) 555-0142"
2. "A: [" + "(718) 555-0142" + "]" -> "A: [(718) 555-0142]"

print("A: [(718) 555-0142]")
"""
# Prediction:
# Actual:
# Explanation:

print("B: [" + raw.replace("-", "") + "]")
"""
raw = " (718) 555-0142 "

1.
"""
# Prediction:
# Actual:
# Explanation:

print("C: [" + raw.replace(" ", "").replace("(", "").replace(")", "").replace("-", "") + "]")
"""
raw = " (718) 555-0142 "

1.
"""
# Prediction:
# Actual:
# Explanation:

print("D:", raw.find(")"))
"""
raw = " (718) 555-0142 "

1.
"""
# Prediction:
# Actual:
# Explanation:

raw.strip()
print("E: [" + raw + "]")
"""
raw = " (718) 555-0142 "

1.
"""
# Prediction:
# Actual:
# Explanation:


# ==================== MODIFY ====================
# One change at a time. Run after each one.
#
# 1. Change one line so E prints the number without the edge spaces.
#
# 2. Test one change: set raw = "718.555.0142" and run C again. Then try
#    raw = "718-555-0142 cell". What does C give back for each? Write one
#    sentence: when is C enough, and when do you need Day 4's normalize_phone?
#
# 3. Write area_code(raw): clean raw with methods, then return the area code.
#    area_code(" (718) 555-0142 ") --> "718"
#    Use .find() to locate ")" instead of counting positions by hand.
