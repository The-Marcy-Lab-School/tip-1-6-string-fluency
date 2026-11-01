"""
Independent check: work alone, no AI, no notes. Write your prediction on paper first.

Step	Task
1. Predict the output.
2. Debug (make first_digit do what its comment says, for any address line).
3. Adjust (write unit(address) that returns everything from the first digit to
   the end: "Apt 4B" -> "4B". Use first_digit.)
4. Test (change the address to "Apt B". Predict, then run).
"""

# Position of the first digit in an address line, or -1 if there is none:
# "Apt 4B" -> 4
def first_digit(address):
    for i in range(len(address)):
        if address[i].isdigit():
            return i
        else:
            return -1


print(first_digit("Apt 4B"))
