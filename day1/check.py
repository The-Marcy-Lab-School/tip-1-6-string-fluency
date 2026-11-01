"""
Independent check: work alone, no AI, no notes. Write your prediction on paper first.

Step	Task
1. Predict the output.
2. Debug (make both functions do what their comments say, for any code).
3. Adjust (the front desk also wants the character just before the check letter:
   "QX7204K" -> "Q4K").
4. Test (change the code to "AB12C". Predict, then run).
"""

# A confirmation code's last character is its check letter: "QX7204K" -> "K"
def check_letter(code):
    return code[len(code)]


# The first character and the check letter: "QX7204K" -> "QK"
def first_and_check(code):
    return code[1] + check_letter(code)


print(first_and_check("QX7204K"))
