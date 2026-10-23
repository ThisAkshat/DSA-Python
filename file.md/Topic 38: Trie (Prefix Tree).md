# Topic 38: Trie (Prefix Tree) 🌳🔤

## 1. What It Does

* A **Trie** is a tree-based data structure designed to store and search words.
* Each path represents characters that form a word or part of a word.
* Words with the same starting characters share the same path.
* Trie is especially useful for **prefix searching**, such as finding all words that start with `"app"`.

## 2. Diagram 📊

Suppose we store these words: `CAR`, `CAT`, `CAN`, `DOG`.

```text
             Root
            /    \
           C      D
           |      |
           A      O
         / | \    |
        R  T  N   G
        ✓  ✓  ✓   ✓

Words: CAR, CAT, CAN, DOG
```

**How it works:**

* `CAR`, `CAT`, and `CAN` share the path `C → A`.
* After `CA`, the path branches into `R`, `T`, and `N`.
* `DOG` follows a separate path.
* A marker identifies where a complete word ends.

## 3. Unique Point 💡

* Trie searching depends mainly on the **length of the word**, not the total number of stored words.
* Searching for a word of length `L` takes approximately `O(L)` time.
* Unlike a HashMap, a Trie can efficiently find words that share a prefix.

## 4. Main Purpose 🎯

* **Autocomplete:** Suggest words while typing.
* **Prefix Search:** Find all words beginning with specific letters.
* **Spell Checking:** Check words against a stored vocabulary.
* **Dictionary Search:** Store and retrieve words by their characters.

## 5. Real-World Apps 🌍

**1. Google Search:** Prefix-based data structures can help power autocomplete suggestions as users type.

**2. Mobile Keyboards:** Suggest words based on the letters already entered.

**3. Spell Checkers:** Search a vocabulary to check words and support prefix-based suggestions.

---
