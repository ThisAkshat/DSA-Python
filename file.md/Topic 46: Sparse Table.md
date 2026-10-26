# Topic 46: Sparse Table

## 1. What It Does

* Array ki range mein minimum, maximum ya GCD find karta hai.
* Pehle se range ke answers calculate karke store karta hai.
* Range query ka answer `O(1)` time mein de sakta hai.
* Jab array change nahi hota, tab sabse useful hota hai.

## 2. Diagram

**Array:**

```text
Index:   0   1   2   3   4
Array:  [4] [2] [7] [1] [5]
```

**Find minimum in range `[1, 4]`:**

```text
        [2] [7] [1] [5]
         └───┘   └───┘
        Range 1  Range 2

        Min = 2   Min = 1
             \     /
              min()
                |
              Answer
                1
```

## 3. Unique Point

* Minimum query mein overlapping ranges bhi use kar sakta hai.
* Overlap se answer galat nahi hota, kyunki `min(x, x) = x`.
* Array update karne par stored answers outdated ho sakte hain.

## 4. Main Purpose

* **Problem:** Baar-baar range ka minimum nikalne ke liye har baar saare elements check karna slow hai.
* **Solution:** Pehle hi chhoti aur badi ranges ke answers store kar lo.
* **Result:** Baad mein minimum query `O(1)` mein answer ho sakti hai.

## 5. Real-World Apps

1. **Weather Data:** Fixed historical data mein kisi period ka minimum temperature find karna.
2. **Competitive Programming:** Bahut saari range-minimum queries efficiently solve karna.
3. **Terrain Analysis:** Fixed elevation data mein kisi range ki minimum height find karna.

---
