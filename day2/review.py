# Day 2 review and Investigate C. Write a prediction before each run.

# ==================== REVIEW ====================
# Before you run: which two lines print the same character?

d = "7185550142"
print(d[0])                    # Prediction:
print(d[-1])                   # Prediction:
print(d[len(d) - 1])           # Prediction:


# ==================== INVESTIGATE C ====================
# The [ ] show where each result starts and ends, so you can see an empty one.

d = "7185550142"
print("[" + d[3:6] + "]")         # Prediction:
print("[" + d[6:] + "]")          # Prediction:
print("[" + d[-4:] + "]")         # Prediction:
print("[" + d[:3] + d[3:] + "]")  # Prediction:
print("[" + d[10:] + "]")         # Prediction:
