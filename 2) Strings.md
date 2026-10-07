# 2) Strings

### 1) What it does

A string is a sequence of characters used to store text.
Examples: `"Hello"`, `"Akshat"`, `"Python"`.
Each character has an index starting from `0`.
You can access characters using their index.
Strings are commonly used for names, sentences, passwords, IDs, and text processing.

### 2) Diagram

```text
String:  "PYTHON"
Index:      0 1 2 3 4 5
            ↓ ↓ ↓ ↓ ↓ ↓
Character:  P Y T H O N

"PYTHON"[2] → 'T'
```

### 3) Unique Python line

In Python, **strings are immutable** — you cannot directly change one character inside an existing string.

```python
s = "Python"
s[0] = "J"      # ❌ Error
```

Instead, Python creates a new string:

```python
s = "J" + s[1:] # "Jython"
```

### 4) Why we use it / Main purpose

The main purpose is **working with text and characters**.
Strings are heavily used in search, pattern matching, data validation, and text processing.
Many DSA problems involve reversing, comparing, counting, or searching characters.
Common operations include slicing, concatenation, searching, and sorting.
