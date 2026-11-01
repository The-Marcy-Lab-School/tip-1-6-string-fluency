# String Fluency: instructor solutions

Hand out each day's `check.py` at the start of the independent check. Every output below was run.

---

## Day 1: Indexing

### Predict & run

```
A: MLS
B: mls
C: IC
D: M LS
Traceback (most recent call last):
  File "initials.py", line 88, in <module>
    print("E:", initials("Marcy Lab School "))
  File "initials.py", line 23, in initials
    result += name[i + 1]
IndexError: string index out of range
```

- Ruler, bottom row: `-16 -15 … -1`.
- **B:** the function copies whatever letter follows each space; it never changes case.
- **C:** positions are worked out while the loop runs, so the same function fits a 13-character name.
- **D:** at `i = 5` the next character is the second space, so a space is added; at `i = 6` it adds `L`.
- **E:** on the last iteration `i = 16` is the trailing space, and `name[17]` doesn't exist (the last position is 16).

### Investigate

- **A:** `len(name)` → `17` · `i` → `16` · `name[i]` → `' '` · `i + 1` → `17` · `name[i + 1]` → `IndexError`.
- **B:** 6 and 10 were counted for one string; in `"Industry City"` they land on `r` and `i`. The loop finds the spaces wherever they are.
- **C:** `'l'` · `'S'` · `'l'` · `'M'` (-0 is just 0) · `'MARCY'`.

### Modify

```python
def initials(name):
    result = name[0]
    for i in range(len(name) - 1):
        if name[i] == " ":
            result += name[i + 1]
    return result.upper()


def last_initial(name):
    for i in range(1, len(name)):
        if name[-i] == " ":
            return name[-i + 1]
    return name[0]
```

`initials`: A, B, E → `MLS`; C → `IC`; D → `M LS`. `last_initial`: `S`, `C`.

### Make

```python
def monogram(name):
    last_space = -1
    for i in range(len(name)):
        if name[i] == " ":
            last_space = i
    if last_space == -1:
        return name[0]
    return name[0] + name[last_space + 1]
```

Output: `AR`, `PS`, `C`. A version that searches from the end with negative positions (like `last_initial`) also counts.

### Independent check (`day1/check.py`)

| Step | Solution | Output |
| ---- | -------- | ------ |
| 1. Predict | Crashes: `code[len(code)]` is one past the end. | `IndexError: string index out of range` |
| 2. Debug | `return code[-1]`; `return code[0] + check_letter(code)` | `QK` |
| 3. Adjust | `code[0] + code[-2] + check_letter(code)` | `Q4K` |
| 4. Test | `"AB12C"` | `AC`, `A2C` |

**Success:** predicts the crash and why, fixes both lines with positions that fit any length, and the Test runs. Partial: corrected after running, with a *because* about the last position.

| Fellow's answer | Missing | Go to |
| --------------- | ------- | ----- |
| Predicts `XK` or `QK`, no crash | the last position is length minus 1 | Investigate A |
| Keeps `code[1]` | positions start at 0 | Day 1 review |
| Uses `code[6]`, and the Test crashes | positions worked out from the length | Investigate B |

---

## Day 2: Slicing

### Predict & run

```
A: (718) 555-0142
B: (***) ***-0142
C: (171) 855-50142
D: (***) ***-0142
E: (718)  55-5 0142
```

- **C:** every slice is counted from the front, so the extra `1` shifts every part.
- **D:** `[-4:]` counts from the end, so a country code at the front doesn't matter.
- **E:** the slices count spaces as characters: clean before you parse.

### Investigate

- **A:** `'171'` · `'855'` · `'50142'` · `(171) 855-50142`.
- **B:** `mask_phone` only needs the end, and negative positions count from the end.
- **C:** `'555'` · `'0142'` · `'0142'` · `'7185550142'` · `''`.

### Modify

```python
def format_phone(digits):
    if len(digits) == 11 and digits[0] == "1":
        digits = digits[1:]
    return "(" + digits[:3] + ") " + digits[3:6] + "-" + digits[6:]


def parse_phone(digits):
    return {"area": digits[:3], "exchange": digits[3:6], "line": digits[-4:]}


def same_last_four(a, b):
    return a[-4:] == b[-4:]
```

### Make

```python
def us_date(date):
    return date[5:7] + "/" + date[-2:] + "/" + date[:4]


def short_date(date):
    return date[5:7] + "/" + date[-2:] + "/" + date[2:4]
```

### Independent check (`day2/check.py`)

| Step | Solution | Output |
| ---- | -------- | ------ |
| 1. Predict | `[:-3]` keeps the dot; `[-3:-1]` leaves out the last character. | `receipt_2026-11.` then `pd` |
| 2. Debug | `filename[:-4]`, `filename[-3:]` | `receipt_2026-11`, `pdf` |
| 3. Adjust | `return filename[-11:-4]` | `2026-11` |
| 4. Test | `"receipt_2027-01.pdf"`, then `"taxes.pdf"` | `receipt_2027-01`, `pdf`, `2027-01`; then `taxes`, `pdf` |

| Fellow's answer | Missing | Go to |
| --------------- | ------- | ----- |
| Predicts `receipt_2026-11` | the end of a slice is left out | Investigate C |
| Uses `filename[16:19]` for the extension, and `taxes.pdf` gives `''` | negative slices fit any length | Investigate B |

---

## Day 3: Comparison and `in`

### Predict & run

```
True
True
False
None
False
False
```

- **`only_phone_chars`:** it returns on the first character, so it only ever checks one. `""` never enters the loop and reaches the end with no `return`, so it gives `None`.
- **`area_code_ok`:** `digits[0] == "0" or "1"` is `False or "1"`, which is `"1"`, and non-empty text counts as true, so every area code is rejected.

### Investigate

- **A:** `'7'` · `False` · `'1'` (truthy).
- **B:** one passing test doesn't prove a function: it passed because the first character happened to be allowed.

### Modify

```python
def only_phone_chars(raw):
    for ch in raw:
        if not (ch.isdigit() or ch in ALLOWED):
            return False
    return True


def area_code_ok(digits):
    if digits[0] in "01":
        return False
    return True


def is_valid_phone(raw):
    if not only_phone_chars(raw):
        return False
    digits = normalize_phone(raw)
    if len(digits) != 10:
        return False
    return area_code_ok(digits)
```

Helper tests, in order: `True, False, False, True, True, False`. Validator tests: `True, True, False, False, False, False`.

### Make

```python
def is_valid_email(email):
    if email == "":
        return False
    if "@" not in email or " " in email:
        return False
    if email[0] == "@" or email[-1] == "@" or email[-1] == ".":
        return False
    return True
```

### Independent check (`day3/check.py`)

The ZIP code check from the original lesson: `or "-"` is always true, and the loop returns on the first character. Predict → `True`. Debug → return `False` for any non-digit inside the loop, `True` after it, and check `len(zip_code) == 5`. Adjust → accept 10 characters with `-` at position 5. Test → `"1137A"` gives `False`.

---

## Day 4: Find the first index

### Predict & run

```
A: 13
B: -1
C: -1
D: 16
E: c
```

- **C:** `return -1` in the `else` runs on the first allowed character, so the loop never gets past position 0.
- **D:** no early return, so `bad` keeps being overwritten: it ends at the *last* bad position.
- **E:** `for ch in raw` gives characters, not positions, so it returns `"c"`.

### Investigate

- **A:** `bad` changes at `i = 13` (`c`), 14 (`e`), 15 (`l`), 16 (`l`) → `16`.
- **B:** A returns the first match and stops; D keeps going. The form needs the first.
- **C:** `13` · `'c'` · `'cell'`.

### Modify

```python
pos = first_bad_char(raw)
if pos == -1:
    print("Looks good")
else:
    print('Unexpected "' + raw[pos] + '" at position ' + str(pos))
```

`.find()` looks for one character you name; `first_bad_char` looks for *any* character that isn't allowed (`"718-555-0142 ext 12".find("c")` → `-1`, but `first_bad_char` → `13`).

```python
def normalize_phone(raw):
    digits = ""
    for ch in raw:
        if ch.isdigit():
            digits += ch
    return digits
```

### Make

```python
def find_at(email):
    for i in range(len(email)):
        if email[i] == "@":
            return i
    return -1


def username(email):
    pos = find_at(email)
    if pos == -1:
        return email
    return email[:pos]
```

### Independent check (`day4/check.py`)

| Step | Solution | Output |
| ---- | -------- | ------ |
| 1. Predict | The `else` returns -1 on `A`, the first character. | `-1` |
| 2. Debug | Move `return -1` after the loop. | `4` |
| 3. Adjust | `pos = first_digit(address)`; return `""` if `pos == -1`, else `address[pos:]` | `4B` |
| 4. Test | `"Apt B"` | `-1`, and `unit` gives `''` |

The Test exposes a fix that skips the `-1` check: `address[-1:]` gives `'B'`, a unit that doesn't exist.

---

## Day 5: Looking up string methods

### Predict & run

```
A: [(718) 555-0142]
B: [ (718) 5550142 ]
C: [7185550142]
D: 5
E: [ (718) 555-0142 ]
```

- **B:** `replace` removes every `-` but leaves the edge spaces.
- **D:** the leading space is position 0, so `)` is at 5.
- **E:** `strip()` gave back a new string, and nothing kept it; `raw` didn't change.

### Investigate

- **A:** `'(718)555-0142'` · `'718)555-0142'` · `'718555-0142'` · `'7185550142'`.
- **B:** A printed the new string `strip()` gave back. E threw it away and printed the unchanged `raw`.
- **C:** `'00482'` · `'ord-1'` · `'abc'` · `2` · `-1` · `False`.

### Modify

1. `raw = raw.strip()` → `E: [(718) 555-0142]`.
2. `"718.555.0142"` → `[718.555.0142]`; `"718-555-0142 cell"` → `[7185550142cell]`. C only removes what you list; `normalize_phone` keeps only digits, whatever else was typed.
3. ```python
   def area_code(raw):
       raw = raw.strip()
       return raw[raw.find("(") + 1:raw.find(")")]
   ```

### Make

```python
def clean_email(email):
    return email.strip().lower()


def domain(email):
    return email[email.find("@") + 1:]


gmail = 0
for email in emails:
    d = domain(clean_email(email))
    print(d)
    if d == "gmail.com":
        gmail += 1
print("gmail.com:", gmail)
```

### Independent check (`day5/check.py`)

| Step | Solution | Output |
| ---- | -------- | ------ |
| 1. Predict | `raw.strip()` is thrown away. | `[ 00482 ]` |
| 2. Debug | `raw = raw.strip()` | `[00482]` |
| 3. Adjust | `raw = raw.strip().lower()` | `[00482]` for `" ORD-00482"` |
| 4. Test | `"Ord-00517 "` | `[00517]` |

The Test exposes a fix that adds `.replace("ORD-", "")` instead of `lower()`: `"Ord-00517 "` gives `[Ord-00517]`.
