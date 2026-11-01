# Day 4 review and Investigate C. Write a prediction before each run.

# ==================== REVIEW ====================
# Before you run: what does find give back when there's no match?

s = "718-555-0142 cell"
print(s.find("-"))           # Prediction:
print(s.find("x"))           # Prediction:


# ==================== INVESTIGATE C ====================

s = "718-555-0142 cell"
print(s.find("c"))           # Prediction:
print(s[13])                 # Prediction:
print(s[s.find("c"):])       # Prediction:
