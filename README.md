# String Fluency

**Time:** one week, five 60-minute sessions · **Type:** spiral (strings, deeper) · **Goal:** GCF fluency

You already know how to loop over a string. This week you get fast and accurate with everything else a string can do, the way GCF Q1 and Q2 problems expect.

## The week

| Day | You'll learn | Working habit focus | If there's time |
| --- | ------------ | ------------------- | --------------- |
| 1 | `len()`, indexing, negative indexes | Predict vs observe | |
| 2 | slicing | Trace | `[::-1]`; `word[10]` crashes but `word[10:]` doesn't; the empty string |
| 3 | comparison, `in` | Hypothesize | |
| 4 | iteration, the "find the first index" algorithm | Trace each iteration | building a new string; returning too early from inside a loop |
| 5 | looking up a string method (`isdigit`, `lower`, `find`, `replace`, `strip`) | Test one change | `int("7")` and `str(7)` |

## What you're learning (come back to this table all week)

| # | Skill | What it does | Example | Day |
| - | ----- | ------------ | ------- | --- |
| 1 | `len()` | counts the characters | `len("Brooklyn")` → `8` | 1 |
| 2 | Indexing | gets the one character at a position; positions start at 0 | `"Brooklyn"[0]` → `'B'`, `"Brooklyn"[7]` → `'n'` | 1 |
| 3 | Negative indexes | counts positions from the end; -1 is the last character | `"Brooklyn"[-1]` → `'n'` | 1 |
| 4 | Slicing | gets a run of characters; the end position is left out | `"Brooklyn"[0:5]` → `'Brook'` | 2 |
| 5 | Comparison | asks whether two whole strings are exactly the same | `"brooklyn" == "Brooklyn"` → `False` | 3 |
| 6 | `in` | asks whether one string appears inside another | `"lyn" in "Brooklyn"` → `True` | 3 |
| 7 | Iteration | visits each character, or each position, in order | `for i in range(len(word)):` | 4 |
| 8 | Find the first index | loops until the first match, then stops | first `"o"` in `"Brooklyn"` → `2` | 4 |
| 9 | Looking up a string method | finds the tool someone already wrote | `"  Brooklyn ".strip()` → `'Brooklyn'`, `"Brooklyn".find("o")` → `2` | 5 |

**If there's time**

| Skill | Example | Day |
| ----- | ------- | --- |
| Reversing with a slice | `"Brooklyn"[::-1]` → `'nylkoorB'` | 2 |
| A position that doesn't exist | `"Brooklyn"[10]` → `IndexError`, but `"Brooklyn"[10:]` → `''` | 2 |
| Building a new string | `word[0] = "b"` → `TypeError`, so build a new string with `+=` | 4 |
| Digits as text vs numbers | `int("7") + 1` → `8` | 5 |

## Working habit: Trace, predict, explain

Before you run code, work out what it will do. After you run it, compare. Each day adds one step and keeps the ones before.

| Step | What you do | Where it goes |
| ---- | ----------- | ------------- |
| Trace | track each name's value, line by line | the trace under each snippet |
| Predict | commit to the exact output | `# Prediction:` |
| Observe | compare to the actual output, exactly | `# Actual:` |
| Hypothesize | when they differ, name the line and what you believed | `# Explanation:` ("I thought ___, but Python ___") |
| Test | change one thing, predict, run again | Modify |

A wrong prediction isn't a failure. It shows you exactly which idea to look at next.

## How this week works

### When you're stuck

Raise your hand when either of these is true:

- You've been stuck on one step for **5 minutes**, or
- You've tried **two different things** and neither worked.

Look for the 🙋 symbol in this guide. It marks the places where fellows most often get stuck, and asking for help there is the right move.

**When you ask for help, come with:**

1. The line of code you're stuck on
2. What you predicted
3. What actually happened
4. What you've tried so far

The ✅ symbol marks a checkpoint where you show an instructor your work before moving on.

---

## Day 1: Indexing (every character has two addresses)

**Time:** review 5 · predict & run 10 · investigate 8 · modify 12 · make 10 · independent check 10 · buffer 5

**Files for today**

| File | Used in |
| ---- | ------- |
| `day1_review.py` | Review |
| `day1_indexing.py` | Predict & run, Investigate, Modify |
| `day1_make.py` | Make |

**Coding habit:** use the position that works for any string: `[0]` for the first character, `[-1]` for the last. Switch only if you get a **runtime error** (a crash with a message) or a **logic error** (it runs, but the output isn't what you meant).

**Working habit (today): predict vs observe.** Write the exact output before you run, then compare it character for character. A wrong prediction tells you which idea to look at.

### Review (5 minutes)

You've seen these before. Run `day1_review.py`:

```python
word = "Lab School"
print(len(word))
print(word[0])
print(word[len(word) - 1])
```

```
10
L
l
```

Answer in `day1_review.py`:

1. "Lab School" has 9 letters. Why does `len(word)` print `10`?
2. Add `print(word[3])`. Predict, then run. What is at position 3?
3. Add `print(word[len(word)])`. Predict, then run. Why does it crash when the line above it works?

### Today's ideas

| # | Idea | Try it in the REPL |
| - | ---- | ------------------ |
| 4 | Positions can also be counted from the end, starting at -1 for the last character. | `"Lab"[-1]` |
| 5 | Every character has two addresses, one from the front and one from the end, and they're exactly the length apart. | `"Lab"[0]`, `"Lab"[-3]` |
| 6 | A position can be worked out while the program runs, so one expression works for a string of any length. | `word = "Lab"`, `word[len(word) - 1]`, then `word = "Marcy"` and run it again |
| 7 | Counting from the end also has a limit: it can't go past the first character. | `"Lab"[-4]` |

### Predict & run (10 minutes)

Open `day1_indexing.py`. The goal is at the top: the school's initials, `"MLS"`.

1. Fill in the data types and the bottom row of the position ruler (the positions counted from the end).
2. For each print, A to E: write the trace under it, then your prediction. The trace for A is done for you as a model.
3. Run `python3 day1_indexing.py` and fill in every `# Actual:` and `# Explanation:`.

Self-check: the length line and A should match your ruler. If B doesn't, check your bottom row.

**Swap with a partner** and compare explanations. Ask an instructor if you can't agree on one.

🙋 **Ask for help if:** your bottom row doesn't end at `-1` under the last `l`.

### Investigate (8 minutes)

**A) Break it down.** Fill in this table for `school[len(school) - 1]`, one row per step, in the order Python works it out:

| Expression | Value | Data type |
| ---------- | ----- | --------- |
| `len(school)` | | |
| `len(school) - 1` | | |
| `school[len(school) - 1]` | | |

**B) Compare.** Why do `school[0]` and `school[-16]` both work, but `school[16]` and `school[-17]` crash? Use ideas 5 and 7.

**C) Run these in the REPL** and write what each one shows:

```python
len("")
"Lab"[-3]
"Lab"[-0]
word = "Queens"
word[len(word) - 1]
word[-1]
word = "Marcy"
word[-len(word)]
```

✅ **Checkpoint:** Show an instructor your table and your answer to B.

### Modify (12 minutes)

At the bottom of `day1_indexing.py`. Change one thing at a time.

1. **Fix E** so it prints the last letter.
2. **Change the school** to `"Industry City"`. Predict A and B, then run. Why does A print a word you didn't expect, and why does B crash?
3. **Trace:** predict `school[-len(school)] + school[-1]` for `"Marcy Lab School"`, then trace it step by step.

🙋 **Ask for help if:** your exercise 2 explanation doesn't say what the positions were written for.

### Make (10 minutes)

Open `day1_make.py`. A café prints a pickup code on each order.

**Requirements**

1. Print the customer's first letter and last letter. Use a negative position for at least one.
2. Print the length of the name.
3. Print the pickup code: first letter + last letter + length.
4. Change the name to `"Sam"` and run again. The code must still be right, and the only line you change is the name.
5. The program must run without crashing.

**Check your output** for `name = "Jordan"`:

```
First: J
Last: n
Length: 6
Pickup code: Jn6
```

For `"Sam"` the code is `Sm3`.

✅ **Checkpoint:** Show an instructor both runs, and point to the line that makes requirement 4 work.

### Independent check (10 minutes)

Your instructor will hand this out. Work alone, with no AI and no notes, and write your prediction on paper before you run anything.

### If there's time

Loop over a word from the end:

```python
word = "Marcy"
for i in range(len(word)):
    print(word[-1 - i])
```

Predict the output first. Which positions does `-1 - i` visit?
