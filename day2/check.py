"""
Independent check: work alone, no AI, no notes. Write your prediction on paper first.

Step	Task
1. Predict the output.
2. Debug (make both functions do what their comments say, for any ".pdf" receipt).
3. Adjust (write receipt_month(filename) that returns the year and month:
   "receipt_2026-11.pdf" -> "2026-11").
4. Test (change the file to "receipt_2027-01.pdf", then to "taxes.pdf". Predict, then run).
"""

# The file name without ".pdf": "receipt_2026-11.pdf" -> "receipt_2026-11"
def file_base(filename):
    return filename[:-3]


# The extension: "receipt_2026-11.pdf" -> "pdf"
def extension(filename):
    return filename[-3:-1]


print(file_base("receipt_2026-11.pdf"))
print(extension("receipt_2026-11.pdf"))
