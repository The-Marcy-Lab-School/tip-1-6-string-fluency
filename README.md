# String Fluency

**Time:** one week, five 60-minute sessions · **Type:** spiral (strings, deeper) · **Goal:** GCF fluency

You've seen every one of these string tools before. This week you use them together, quickly, to build the small functions real programs are full of: name badges, contact cards, sign-up forms, order numbers. GCF Q1 and Q2 problems are built from the same moves.

## The week

| Day | You build | Skills it combines | Practice on your own | Working habit focus | If there's time |
| --- | --------- | ------------------ | -------------------- | ------------------- | --------------- |
| 1 | `initials`: name badges, `"Marcy Lab School"` → `"MLS"` | `len()`, indexing, negative indexes, a loop over positions | `monogram`: jacket monograms | Predict vs observe | double spaces |
| 2 | `format_phone`, `mask_phone`, `parse_phone`: contact cards and receipts | slicing, `[:end]`, `[start:]`, negative slices | `us_date`: dates on a sign-up sheet | Trace | `[::-1]`; `word[10]` crashes but `word[10:]` doesn't |
| 3 | `only_phone_chars`, `area_code_ok`, `is_valid_phone`: a sign-up form | comparison, `in`, `or`, returning early | `is_valid_email` | Hypothesize | |
| 4 | `first_bad_char`: point to the character that doesn't belong | the "find the first index" algorithm, building a new string | `find_at` and `username`: the @ by hand | Trace each iteration | |
| 5 | Cleaning pasted input with string methods | `strip`, `replace`, `find`, `lower`, `isdigit` | `clean_email` and `domain`: the email list | Test one change | `signups.py`: the whole sign-up list |

## What you're learning (come back to this table all week)

| # | Skill | Real job | Try it in the REPL | The idea |
| - | ----- | -------- | ------------------ | -------- |
| 1 | Indexing | The first letter of each word on a name badge | `name = "Marcy Lab School"` · `name[0]` → `'M'` · `name[len(name) - 1]` → `'l'` | Positions start at 0, so the last one is the length minus 1. The length itself is never a position. |
| 2 | Negative indexes | The last word's initial, found by searching from the end | `name[-1]` → `'l'` · `name[-6]` → `'S'` | Every character has a second address counted from the end, starting at -1. |
| 3 | Slicing | A contact card: `"7185550142"` → `"(718) 555-0142"` | `d = "7185550142"` · `d[3:6]` → `'555'` · `d[-4:]` → `'0142'` | A slice takes a run of characters and leaves the end position out, so `d[:3] + d[3:]` is the whole string. |
| 4 | Comparison and `in` | Only digits and `( ) - . +` and space are allowed on the form | `"7" in "01"` → `False` · `"7" == "0" or "1"` → `'1'` | `in` checks a piece against a whole set. Each side of `or` is its own check, and non-empty text counts as true. |
| 5 | Returning early | Answer "not valid" as soon as one character fails | `return False` inside the loop, `return True` after it | You can say "no" the moment you find a problem, but "yes" only after checking everything. |
| 6 | Find the first index | Point to the bad character: `"718-555-0142 cell"` → `13` | `"718-555-0142 cell".find("c")` → `13` | Loop over positions and return the first match. If the loop finishes, there wasn't one: return -1. |
| 7 | Building a new string | Keep only the digits: `"(718) 555-0142"` → `"7185550142"` | `d = ""` · `d += "7"` · `d` → `'7'` | Strings can't change in place, so cleaning means growing a new string from what you keep. |
| 8 | Looking up a string method | Clean what people paste: `" (718) 555-0142 "` | `" 00482 ".strip()` → `'00482'` · `"Lab".find("z")` → `-1` | A method gives back a new string. The original doesn't change unless you assign the result. |

## Working habit: Trace, predict, explain

Before you run code, work out what it will do. After you run it, compare. Each day adds one step and keeps the ones before.

| Step | What you do | Where it goes |
| ---- | ----------- | ------------- |
| Trace | track each name's value, line by line or iteration by iteration | the trace under each print |
| Predict | commit to the exact output | `# Prediction:` |
| Observe | compare to the actual output, exactly | `# Actual:` |
| Hypothesize | when they differ, name the line and what you believed | `# Explanation:` ("I thought ___, but Python ___") |
| Test | change one thing, predict, run again | Modify |

Every Predict section starts with a **goal**: what the code is supposed to do. Judge each print against it. The first trace is done for you as a model; the others start with `iteration 1/?` (work out how many iterations really run) or `1.` (number the steps).

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

**Every day:** Predict & run 12 · Investigate 8 · Modify 12 · Make 13 · Independent check 10 · buffer 5. The independent check is handed out by your instructor: work alone, with no AI and no notes, and write your prediction on paper before you run anything.

---

## Day 1: Indexing (`day1/`)

| File | Used in |
| ---- | ------- |
| `day1/initials.py` | Predict & run, Modify |
| `day1/make_monogram.py` | Make |

### Review

You've written loops like this before. In the REPL:

```python
name = "Marcy Lab School"
for i in range(len(name)):
    print(i, name[i])
```

Before you run it: how many lines print, and what's on the last one? (16 lines; the last is `15 l`.)

### Predict & run

Open `day1/initials.py`. The goal is at the top: initials for name badges.

1. Fill in the bottom row of the position ruler: the positions counted from the end.
2. For each print, A to E: write the trace, then your prediction. The trace for A is the model.
3. Run `python3 initials.py` and fill in every `# Actual:` and `# Explanation:`.

Self-check: A and C should match the goal. If your trace for D didn't predict a space in the result, trace iterations 6 and 7 again.

**Swap with a partner** and compare explanations for D and E.

🙋 **Ask for help if:** you can't say which value of `i` makes E crash.

### Investigate

**A) Break it down.** For E (`"Marcy Lab School "`, with a space at the end), fill in the table for the iteration that crashes:

| Expression | Value |
| ---------- | ----- |
| `len(name)` | |
| `i` | |
| `name[i]` | |
| `i + 1` | |
| `name[i + 1]` | |

**B) Compare.** `initials` worked for both `"Marcy Lab School"` and `"Industry City"` without any change. Why would `name[0] + name[6] + name[10]` work for only one of them?

**C) Run these in the REPL:**

```python
name = "Marcy Lab School"
name[-1]
name[-6]
name[len(name) - 1]
name[-0]
"marcy".upper()
```

✅ **Checkpoint:** Show an instructor your table, and say which position E's loop should stop before.

### Modify

The three exercises are at the bottom of `initials.py`: stop the loop before it looks past the end, capital letters for the badge printer, and `last_initial` with a negative position.

Self-check: after exercise 2, A, B and E all print `MLS`. `last_initial` gives `S` for `"Marcy Lab School"` and `C` for `"Industry City"`.

### Make: jacket monograms

Open `day1/make_monogram.py`. A jacket is embroidered with the first letter of the first name and the first letter of the last name.

**Requirements**

1. `monogram(name)` returns the two letters: `"Ana Ruiz"` → `"AR"`.
2. A middle name is skipped: `"Priya Anne Shah"` → `"PS"`.
3. A one-word name gives just its first letter: `"Cher"` → `"C"`.
4. Don't type a position that only fits one name.
5. The program must run without crashing.

**Check your output:**

```
AR
PS
C
```

✅ **Checkpoint:** Show an instructor your output, and point to the line that finds the last name.

### If there's time

D gave `M LS` for `"Marcy  Lab School"` (two spaces). Make `initials` skip the extra space so D prints `MLS`.

---

## Day 2: Slicing (`day2/`)

| File | Used in |
| ---- | ------- |
| `day2/format_phone.py` | Predict & run, Modify |
| `day2/make_dates.py` | Make |

### Review

From Day 1: positions start at 0, and -1 is the last character. In the REPL:

```python
d = "7185550142"
d[0]
d[-1]
d[len(d) - 1]
```

Before you run it: which two lines give the same character?

### Predict & run

Open `day2/format_phone.py`. The goal: a contact card and a masked receipt.

1. For each print, A to E: write the trace (number the steps), then your prediction. A is the model.
2. Run `python3 format_phone.py` and fill in every `# Actual:` and `# Explanation:`.

Self-check: A and B match the goal. Before you move on, compare C and D: both got the same 11 digits.

**Swap with a partner** and compare explanations for C and D.

🙋 **Ask for help if:** you can't explain why D still works when C doesn't.

### Investigate

**A) Break it down** for C, `format_phone("17185550142")`:

| Expression | Value |
| ---------- | ----- |
| `digits[:3]` | |
| `digits[3:6]` | |
| `digits[6:]` | |
| the whole result | |

**B) Compare.** Why does `mask_phone` still give the right last 4 digits when there's a country code, but `format_phone` doesn't?

**C) Run these in the REPL:**

```python
d = "7185550142"
d[3:6]
d[6:]
d[-4:]
d[:3] + d[3:]
d[10:]
```

✅ **Checkpoint:** Show an instructor your table and your answer to B.

### Modify

The three exercises are at the bottom of `format_phone.py`: drop a leading country code, `parse_phone` with a negative slice, and `same_last_four`.

Self-check: C now prints `(718) 555-0142`. `parse_phone("3475550199")` gives `{'area': '347', 'exchange': '555', 'line': '0199'}`. `same_last_four` gives `True`, then `False`.

### Make: dates on a sign-up sheet

Open `day2/make_dates.py`. The database stores dates as `"YYYY-MM-DD"`; the printed sheet shows them the US way.

**Requirements**

1. `us_date(date)` returns `"MM/DD/YYYY"`.
2. `short_date(date)` returns `"MM/DD/YY"`.
3. Get the day with a negative slice.
4. The program must run without crashing.

**Check your output:**

```
11/02/2026
11/02/26
01/15/2027
```

✅ **Checkpoint:** Show an instructor your output, and point to your negative slice.

### If there's time

Predict, then run in the REPL: `"7185550142"[::-1]`. Then `"7185550142"[10]` and `"7185550142"[10:]`. Why does one crash and the other doesn't?

---

## Day 3: Comparison and `in` (`day3/`)

| File | Used in |
| ---- | ------- |
| `day3/validate.py` | Predict & run, Modify |
| `day3/make_email.py` | Make |

### Review

In the REPL:

```python
"Cell" == "cell"
"555" in "7185550142"
"7185550142" == "(718) 555-0142"
```

Before you run it: which is `True`? The last one is why we clean before we compare.

### Predict & run (code review)

Open `day3/validate.py`. A teammate wrote two helpers. The goal at the top says what each one *should* do, and each test has a comment with the value it *should* give back. **Don't run it yet.**

1. Under each test, write the trace: the value of `ch` on each iteration, what each check gives, and when the function returns. The first trace is the model. For `area_code_ok`, number the steps.
2. Write your prediction for each test.
3. Run `python3 validate.py`, fill in each `# Actual:`, then write one sentence per helper explaining what's wrong ("I thought ___, but Python ___").

**Swap with a partner** and compare explanations.

🙋 **Ask for help if:** you and your partner can't agree on why `only_phone_chars("")` prints `None`.

### Investigate

**A) Break it down** for `area_code_ok("7185550142")`:

| Expression | Value |
| ---------- | ----- |
| `digits[0]` | |
| `digits[0] == "0"` | |
| `digits[0] == "0" or "1"` | |

**B) Compare.** `only_phone_chars("(718) 555-0142")` gave the right answer. Why didn't that prove the function was right?

**C) Run these in the REPL:**

```python
d = "7"
d == "0" or "1"
d in "01"
"0" in "01"
```

✅ **Checkpoint:** Show an instructor your fixed helpers and tell them, in one sentence each, what the two bugs were.

### Modify

1. Fix `only_phone_chars` so it checks every character and answers "yes" only after the loop.
2. Fix `area_code_ok` with one `in` check, not an `or` chain.
3. Fill in `# In:` and `# Out:`, then write `is_valid_phone(raw)` using `normalize_phone` and your two fixed helpers. Uncomment the six tests.

Self-check: all six helper tests and all six validator tests match their expected values. Then answer as a comment: why does `"718-555-0142 cell"` need the character check, when cleaning would turn it into 10 good digits?

### Make: is this an email address?

Open `day3/make_email.py`.

**Requirements**

1. It must have an `@` and no spaces.
2. It can't start with `@`, or end with `@` or `.`.
3. An empty entry is not valid.
4. Use `in` for the `@` and the space, and indexes for the first and last characters.
5. The program must run without crashing.

**Check your output:**

```
True
False
False
False
False
False
```

✅ **Checkpoint:** Show an instructor your output, and point to where you answer "no" early.

---

## Day 4: Find the first index (`day4/`)

| File | Used in |
| ---- | ------- |
| `day4/first_bad_char.py` | Predict & run, Modify |
| `day4/make_find_at.py` | Make |

### Review

From Day 3: answer "no" as soon as you find a problem, and "yes" only after the loop. Today you return a **position** instead of yes or no. In the REPL:

```python
s = "718-555-0142 cell"
s.find("-")
s.find("x")
```

Before you run it: what does `find` give back when there's no match?

### Predict & run

Open `day4/first_bad_char.py`. The goal: point to the first character that doesn't belong.

1. For each print, A to E: write the trace, then your prediction. A is the model. C, D and E are a teammate's versions, each one change away from A.
2. Run `python3 first_bad_char.py` and fill in every `# Actual:` and `# Explanation:`.

Self-check: A and B match the goal. For C, D and E, your explanation names the one change and what it does to the loop.

**Swap with a partner** and compare explanations for C, D and E.

🙋 **Ask for help if:** your trace for C runs more than one iteration.

### Investigate

**A) Break it down.** For D, fill in `bad` after each iteration where it changes:

| Iteration | `i` | `raw[i]` | `bad` |
| --------- | --- | -------- | ----- |
| | | | |

**B) Compare.** A and D both find bad characters. Why does A give `13` and D give `16`? Which one does the form need?

**C) Run these in the REPL:**

```python
s = "718-555-0142 cell"
s.find("c")
s[13]
s[s.find("c"):]
```

✅ **Checkpoint:** Show an instructor your table for D and your answer to B.

### Modify

The three exercises are at the bottom of `first_bad_char.py`: the form's error message, why `.find()` can't replace `first_bad_char`, and `normalize_phone` from memory.

Self-check: the message is `Unexpected "c" at position 13`, or `Looks good` for `"(718) 555-0142"`. `normalize_phone("(718) 555-0142")` gives `7185550142`.

### Make: find the @ by hand

Open `day4/make_find_at.py`.

**Requirements**

1. `find_at(email)` returns the position of the first `@`, or `-1`. Write the loop yourself.
2. `username(email)` returns everything before the `@`, using `find_at`. With no `@`, it returns the whole email.
3. Check `find_at` against `email.find("@")` for all three emails.
4. The program must run without crashing.

**Check your output:**

```
8
2
-1
ana.ruiz
no-at-sign.com
```

✅ **Checkpoint:** Show an instructor your output, and the line that makes `username` safe when there's no `@`.

---

## Day 5: Looking up string methods (`day5/`)

| File | Used in |
| ---- | ------- |
| `day5/clean_methods.py` | Predict & run, Modify |
| `day5/make_emails.py` | Make |
| `day5/signups.py` | If there's time |

### Review

On Day 4 you kept only the digits with a loop. Today you look up methods that do parts of that job. Before you start, look up `strip`, `replace` and `find` in the [Python string methods documentation](https://docs.python.org/3/library/stdtypes.html#string-methods). For each one, write: what goes in, and what comes back.

### Predict & run

Open `day5/clean_methods.py`. The goal: clean a pasted phone number with methods. Each print puts `[ ]` around the result so you can see spaces at the edges.

1. For each print, A to E: write the trace (number the steps), then your prediction. A is the model.
2. Run `python3 clean_methods.py` and fill in every `# Actual:` and `# Explanation:`.

Self-check: A and C match the goal. If E surprised you, compare its first line with A's print.

**Swap with a partner** and compare explanations for E.

🙋 **Ask for help if:** you can't say why E still has spaces.

### Investigate

**A) Break it down** for C, one method at a time:

| Expression | Value |
| ---------- | ----- |
| `raw.replace(" ", "")` | |
| `.replace("(", "")` | |
| `.replace(")", "")` | |
| `.replace("-", "")` | |

**B) Compare.** A and E both call `strip()`. Why did A's output change but E's didn't?

**C) Run these in the REPL:**

```python
" 00482 ".strip()
"ORD-1".lower()
"a-b-c".replace("-", "")
"Lab".find("b")
"Lab".find("z")
"7a".isdigit()
```

✅ **Checkpoint:** Show an instructor your table and your answer to B.

### Modify

The three exercises are at the bottom of `clean_methods.py`: fix E, test C on two new inputs, and `area_code` with `.find()`.

Self-check: E prints `[(718) 555-0142]`. `area_code(" (718) 555-0142 ")` gives `718`.

### Make: the email list

Open `day5/make_emails.py`.

**Requirements**

1. `clean_email(email)` removes the edge spaces and makes it lowercase.
2. `domain(email)` returns everything after the `@`. Use `find`.
3. Print the domain of every cleaned email in the list, then how many are `gmail.com`.
4. The program must run without crashing.

**Check your output:**

```
ana.ruiz@gmail.com
gmail.com
gmail.com
marcylabschool.org
gmail.com
yahoo.com
gmail.com: 2
```

✅ **Checkpoint:** Show an instructor your output, and point to each method you looked up.

### If there's time: the whole sign-up list

Open `day5/signups.py` and read the docstring: a food pantry's text-alert sign-up list, with people who signed up twice and entries that aren't phone numbers. Build `signup_report(entries)` with the working functions in the file, counting with a dict keyed by the **clean** number. The expected output is in the docstring.
