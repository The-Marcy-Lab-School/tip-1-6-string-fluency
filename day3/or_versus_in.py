# Day 3 reteach: `or` versus `in`
# Work top to bottom: PREDICT -> RUN -> READ -> MODIFY -> MAKE.
# Edit this file as you go.
#
# Yesterday, we discussed the unexpected result using digits[0] == "0" or "1".
# This lesson shows why and how to fix it. 


# ---------------------------------------------------------------
# 1. PREDICT: a restaurant's delivery check
# ---------------------------------------------------------------

# Goal: the restaurant delivers only to Brooklyn and Queens.
#   "Queens" --> True,  "Bronx" --> False

def can_deliver(borough):
    if borough == "Brooklyn" or "Queens":
        return True
    return False


print(can_deliver("Brooklyn"))
print(can_deliver("Queens"))
print(can_deliver("Bronx"))
# Prediction:
# Actual:
# Explanation:


# ---------------------------------------------------------------
# 2. READ: why it breaks, and the fix
# ---------------------------------------------------------------

# Python reads the condition as two separate pieces:
#
#     (borough == "Brooklyn")   or   "Queens"
#
# For "Bronx": False or "Queens" --> "Queens". Non-empty text counts as true,
# so the `if` runs. Python never adds the missing `borough ==` for you.
#
# One fix writes every comparison in full:
#
#     borough == "Brooklyn" or borough == "Queens"
#
# That works, but every new borough means another `borough ==`, and leaving
# one out brings the bug back.
#
# The fix engineers use: put the allowed values in a list, and ask `in`.

DELIVERY_BOROUGHS = ["Brooklyn", "Queens"]


def can_deliver(borough):
    if borough in DELIVERY_BOROUGHS:
        return True
    return False


print(can_deliver("Brooklyn"))    # True
print(can_deliver("Queens"))      # True
print(can_deliver("Bronx"))       # False

# `value in some_list` asks: is value one of the items in the list?
# It compares against each item for you, so there's no `==` to forget.
# The name in CAPITALS tells the reader: this is a setting, change it here.


# ---------------------------------------------------------------
# 3. MODIFY the fix
# ---------------------------------------------------------------

# A. The restaurant starts delivering to Manhattan.
#    Change ONE line so can_deliver("Manhattan") gives True.

print(can_deliver("Manhattan"))   # should be True after your change
print(can_deliver("Bronx"))       # should still be False


# B. The checkout page needs the opposite question. Write delivery_message
#    with `not in`.
#   "Bronx"  --> "Sorry, we don't deliver to Bronx."
#   "Queens" --> "Delivery available."

def delivery_message(borough):
    return ""  # replace this line


# print(delivery_message("Bronx"))
# print(delivery_message("Queens"))


# ---------------------------------------------------------------
# 4. MAKE: street parking
# ---------------------------------------------------------------

# Street cleaning on your block happens Monday and Thursday. No parking then.
# Write can_park(day) with a list constant and `in` (or `not in`).
#   "Monday"   --> False
#   "Tuesday"  --> True
#   "Thursday" --> False

# print(can_park("Monday"))
# print(can_park("Tuesday"))
# print(can_park("Thursday"))

# The city adds Saturday cleaning. What do you change? Change it, then test "Saturday".


# ---------------------------------------------------------------
# 5. BACK TO TODAY: the area-code check from validate.py
# ---------------------------------------------------------------

# Goal: an area code can't start with "0" or "1".
#   "7185550142" --> True,  "0185550142" --> False,  "1185550142" --> False

def area_code_ok(digits):
    if digits[0] == "0" or "1":
        return False
    return True


print(area_code_ok("7185550142"))
print(area_code_ok("0185550142"))
print(area_code_ok("1185550142"))
# Actual:
# Explanation (same bug as can_deliver):

# Fix it the way you fixed can_deliver: a list constant and `in`. Run again.
