"""
Independent check: work alone, no AI, no notes. Write your prediction on paper first.

Step	Task
1. Predict the output (look at the [ ] edges).
2. Debug (make clean_order_id do what its comment says).
3. Adjust (staff also type the prefix in capitals: " ORD-00482" should give "00482" too).
4. Test (change the input to "Ord-00517 ". Predict, then run).
"""

# Order IDs are typed by staff: " ord-00482 " -> "00482"
def clean_order_id(raw):
    raw.strip()
    return raw.replace("ord-", "")


print("[" + clean_order_id(" ord-00482 ") + "]")
