# 12) HashMap

### 1) What it does

A HashMap stores data in **key-value pairs**.
Each key is associated with a value, allowing you to find the value using its key.
Keys must be unique, but values can be duplicated.
In Python, the equivalent data structure is a **dictionary (`dict`)**.
For example, a student's roll number can be the key and their name can be the value.

### 2) Diagram

```text
       HashMap
   ┌────────┬─────────┐
   │  Key   │  Value  │
   ├────────┼─────────┤
   │  101   │ Akshat  │
   │  102   │ Rahul   │
   │  103   │ Aman    │
   └────────┴─────────┘

   Key: 102
      |
      ▼
   Value: Rahul
```

### 3) Unique Python line

Python dictionaries use hashing to find values by key. **If you assign a new value to an existing key, the old value is replaced.**

```python
students = {101: "Akshat", 102: "Rahul"}

students[102] = "Aman"

print(students[102])  # Aman
```

### 4) Why we use it / Main purpose

The main purpose is to **store and retrieve information quickly using keys**.
Looking up, inserting, and deleting entries typically takes **O(1) average time**.
It is useful for counting frequencies, storing user details, and mapping product IDs to product information.
In DSA interviews, HashMaps are especially important for problems involving duplicates, counting, and fast lookups.
