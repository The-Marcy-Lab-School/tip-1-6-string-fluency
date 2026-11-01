# Day 1: Indexing
# Work top to bottom: PREDICT -> RUN -> INVESTIGATE -> MODIFY.
# Edit this file as you go.
#
# Working habit: Trace, predict, explain (today: predict vs observe)

# ==================== PREDICT ====================
# Fill in EVERY "Prediction:" below before you run anything.

# Goal: get the school's initials: "Marcy Lab School" --> "MLS"

school = "Marcy Lab School"
# Data types of these values:

# Positions from the front. Fill in the positions from the end on the last row.
#     M   a   r   c   y       L   a   b       S   c   h   o   o   l
#     0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
#

print("Length:", len(school))
# Prediction:
# Actual:
# Explanation:

print("A:", school[0] + school[6] + school[10])
"""
school = "Marcy Lab School"

1. school[0]  -> "M"
2. school[6]  -> "L"
3. school[10] -> "S"
4. "M" + "L" + "S" -> "MLS"

print("A:", "MLS")
"""
# Prediction:
# Actual:
# Explanation:

print("B:", school[-16] + school[-10] + school[-6])
"""
school = "Marcy Lab School"

1.
"""
# Prediction:
# Actual:
# Explanation:

print("C:", school[1] + school[7] + school[11])
"""
school = "Marcy Lab School"

1.
"""
# Prediction:
# Actual:
# Explanation:

print("D:", school[-1] + school[len(school) - 1])
"""
school = "Marcy Lab School"

1.
"""
# Prediction:
# Actual:
# Explanation:

print("E:", school[len(school)])
"""
school = "Marcy Lab School"

1.
"""
# Prediction:
# Actual:
# Explanation:


# ==================== MODIFY ====================
# Exercise 1: fix E so it prints the last letter.
# Exercise 2: change school to "Industry City" on line 12. Predict A and B, then run.
# Exercise 3: predict, then trace step by step:
# print(school[-len(school)] + school[-1])
