class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        valid_categories =["electronics","grocery","pharmacy","restaurant"]
        valid_coupons =[]
        for i in range(len(code)):
            if len(code[i]) == 0:
                continue
            is_code_ok = all(ch.isalnum() or ch == '_' for ch in code[i])
            if not is_code_ok:
                continue
            if businessLine[i] not in valid_categories:
                continue
            if not isActive[i]:
                continue
            valid_coupons.append((code[i], businessLine[i]))
        order = {"electronics":0, "grocery":1, "pharmacy":2, "restaurant":3}
        valid_coupons.sort(key=lambda x: (order[x[1]], x[0]))

        return [c[0] for c in valid_coupons]

"""
3606. Coupon Code Validator
You are given three arrays of length n that describe the properties of n coupons: code, businessLine, and isActive. The ith coupon has:

code[i]: a string representing the coupon identifier.
businessLine[i]: a string denoting the business category of the coupon.
isActive[i]: a boolean indicating whether the coupon is currently active.
A coupon is considered valid if all of the following conditions hold:

code[i] is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
businessLine[i] is one of the following four categories: "electronics", "grocery", "pharmacy", "restaurant".
isActive[i] is true.
Return an array of the codes of all valid coupons, sorted first by their businessLine in the order: "electronics", "grocery", "pharmacy", "restaurant", and then by code in lexicographical (ascending) order within each category.
 

Example 1:
Input: code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [true,true,true,true]
Output: ["PHARMA5","SAVE20"]
Explanation:
First coupon is valid.
Second coupon has empty code (invalid).
Third coupon is valid.
Fourth coupon has special character @ (invalid).

Example 2:
Input: code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [false,true,true]
Output: ["ELECTRONICS_50"]

Explanation:
First coupon is inactive (invalid).
Second coupon is valid.
Third coupon has invalid business line (invalid).

"""

"""
INPUT:
code         = ["SAVE20", "", "PHARMA5", "SAVE@20"]
businessLine = ["restaurant", "grocery", "pharmacy", "restaurant"]
isActive     = [True, True, True, True]

MAIN LOOP:
+---+-------------+-------------+------------------+------------------+------------+-------------------------------------+------------------------------------------------------+
| i | code[i]     | Check1: len | Check2: alnum/_  | Check3: category | Check4:    | Action                               | valid_coupons (after)                                 |
|   |             | !=0 ?       | valid?           | valid?           | isActive?  |                                       |                                                        |
+---+-------------+-------------+------------------+------------------+------------+-------------------------------------+------------------------------------------------------+
| 0 | "SAVE20"    | Pass (6)    | Pass (all True)  | Pass (restaurant)| Pass       | Append ("SAVE20","restaurant")       | [("SAVE20","restaurant")]                             |
| 1 | ""          | FAIL (0)    | -- continue --   | --               | --         | Skipped                              | [("SAVE20","restaurant")]                             |
| 2 | "PHARMA5"   | Pass (7)    | Pass (all True)  | Pass (pharmacy)  | Pass       | Append ("PHARMA5","pharmacy")        | [("SAVE20","restaurant"), ("PHARMA5","pharmacy")]     |
| 3 | "SAVE@20"   | Pass (7)    | FAIL ('@' bad)   | --               | --         | Skipped                              | [("SAVE20","restaurant"), ("PHARMA5","pharmacy")]     |
+---+-------------+-------------+------------------+------------------+------------+-------------------------------------+------------------------------------------------------+

CHAR-LEVEL CHECK for i=0 "SAVE20":
+-----+---------------+------------+------------+
| ch  | ch.isalnum()  | ch == '_'  | or result  |
+-----+---------------+------------+------------+
| S   | True          | False      | True       |
| A   | True          | False      | True       |
| V   | True          | False      | True       |
| E   | True          | False      | True       |
| 2   | True          | False      | True       |
| 0   | True          | False      | True       |
+-----+---------------+------------+------------+
=> all(...) = True  =>  is_code_ok = True

CHAR-LEVEL CHECK for i=3 "SAVE@20":
+-----+---------------+------------+------------+
| ch  | ch.isalnum()  | ch == '_'  | or result  |
+-----+---------------+------------+------------+
| S   | True          | False      | True       |
| A   | True          | False      | True       |
| V   | True          | False      | True       |
| E   | True          | False      | True       |
| @   | False         | False      | False  <-- |
+-----+---------------+------------+------------+
=> all(...) = False  =>  is_code_ok = False  =>  continue

SORTING PHASE:
order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}

+----------------------------+---------------+----------------+-------------+----------------------+
| Tuple                      | x[1]          | order[x[1]]    | x[0]        | Sort key             |
+----------------------------+---------------+----------------+-------------+----------------------+
| ("SAVE20","restaurant")     | "restaurant"  | 3              | "SAVE20"    | (3, "SAVE20")        |
| ("PHARMA5","pharmacy")      | "pharmacy"    | 2              | "PHARMA5"   | (2, "PHARMA5")       |
+----------------------------+---------------+----------------+-------------+----------------------+

Compare: (2,"PHARMA5") < (3,"SAVE20")  =>  pharmacy comes first

After sort: [("PHARMA5","pharmacy"), ("SAVE20","restaurant")]

FINAL EXTRACTION:
+------------------------------+----------+
| c (tuple)                    | c[0]     |
+------------------------------+----------+
| ("PHARMA5","pharmacy")        | "PHARMA5"|
| ("SAVE20","restaurant")       | "SAVE20" |
+------------------------------+----------+

OUTPUT: ["PHARMA5", "SAVE20"]   ✅ matches expected

"""
