# Day 1 review and Investigate C. Write a prediction before each run.

# ==================== REVIEW ====================
# Before you run: how many lines print, and what's on the last one?
# Prediction:

name = "Marcy Lab School"
for i in range(len(name)):
    print(i, name[i])

# Actual:


# ==================== INVESTIGATE C ====================
# Predict each line, then run. (Comment out the review loop above if the output gets long.)

name = "Marcy Lab School"
print(name[-1])                # Prediction:
print(name[-6])                # Prediction:
print(name[len(name) - 1])     # Prediction:
print(name[-0])                # Prediction:
print("marcy".upper())         # Prediction:
