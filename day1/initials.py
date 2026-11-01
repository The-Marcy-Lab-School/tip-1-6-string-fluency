# Day 1: Indexing -- initials for name badges
# Work top to bottom: PREDICT -> RUN -> INVESTIGATE -> MODIFY.
# Edit this file as you go.
#
# Working habit: Trace, predict, explain (today: predict vs observe)

# ==================== PREDICT ====================
# Fill in EVERY "Prediction:" below before you run anything.

# Goal: the front desk prints initials on name badges:
#   "Marcy Lab School" --> "MLS"

# Positions in "Marcy Lab School". Fill in the positions from the end on the last row.
#     M   a   r   c   y       L   a   b       S   c   h   o   o   l
#     0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
#


def initials(name):
    result = name[0]
    for i in range(len(name)):
        if name[i] == " ":
            result += name[i + 1]
    return result


print("A:", initials("Marcy Lab School"))
"""
name = "Marcy Lab School"
result = "M"

iterations 1-5/16: i = 0 to 4, no space, result stays "M"

iteration 6/16:
- i = 5
- name[5] = " "
- result = "M" + name[6] -> "M" + "L" -> "ML"

iterations 7-9/16: i = 6 to 8, no space

iteration 10/16:
- i = 9
- name[9] = " "
- result = "ML" + name[10] -> "ML" + "S" -> "MLS"

iterations 11-16/16: i = 10 to 15, no space

return "MLS"
print("A:", "MLS")
"""
# Prediction:
# Actual:
# Explanation:

print("B:", initials("marcy lab school"))
"""
name = "marcy lab school"
result =

iteration 1/?:
"""
# Prediction:
# Actual:
# Explanation:

print("C:", initials("Industry City"))
"""
name = "Industry City"
result =

iteration 1/?:
"""
# Prediction:
# Actual:
# Explanation:

print("D:", initials("Marcy  Lab School"))
"""
name = "Marcy  Lab School"     (two spaces after Marcy)
result =

iteration 1/?:
"""
# Prediction:
# Actual:
# Explanation:

print("E:", initials("Marcy Lab School "))
"""
name = "Marcy Lab School "     (a space at the end)
result =

iteration 1/?:
"""
# Prediction:
# Actual:
# Explanation:


# ==================== MODIFY ====================
# One change at a time. Run after each one.
#
# 1. Fix E without changing the name: the loop should never look past the end.
#    Hint: which position is i on when name[i + 1] crashes?
#
# 2. The badge printer only takes capital letters. Make B print "MLS" too.
#    Look up the string method that does this. Use it in one place only.
#
# 3. Add a second function, last_initial(name), that returns the first letter
#    of the LAST word: "Marcy Lab School" --> "S", "Industry City" --> "C".
#    Use a negative position somewhere.
