# Topic 30: Intervals 📏

## 1. What It Does

* An **Interval** represents a range between a starting value and an ending value.
* Example: `[2, 6]` represents a range from 2 to 6.
* Intervals help us identify overlapping ranges, merge ranges, and find gaps.
* They are commonly used in scheduling and range-related problems.
* Example: If one meeting runs from 9 AM to 11 AM and another from 10 AM to 12 PM, their time intervals overlap.

## 2. Diagram

```text
Interval A:  [1──────3]
Interval B:     [2────────6]
Interval C:                  [8────10]

A and B overlap.

Merge A and B:
             [1──────────6]

Final: [[1, 6], [8, 10]]
```

**How it works:**

* Interval A covers `1–3`.
* Interval B covers `2–6`.
* Because they overlap, we merge them into `[1, 6]`.
* Interval C does not overlap with the merged interval, so it stays separate.

## 3. Unique Point 💡

* Intervals are commonly stored as pairs: `[start, end]`.
* A popular technique is to **sort intervals by their starting values**.
* After sorting, we compare each interval with the previous interval.
* If they overlap, we merge them; otherwise, we keep them separate.
* Sorting usually takes `O(n log n)` time, while checking and merging takes `O(n)` time.
* Important: Whether two intervals that touch at an endpoint overlap depends on the problem's rules.

## 4. Main Purpose

The main purpose of intervals is to manage ranges without checking every individual value.

They help us:

* **Merge ranges:** Combine overlapping intervals.
* **Find conflicts:** Detect overlapping meetings or bookings.
* **Find gaps:** Identify free time between events.
* **Manage schedules:** Organise events by start and end times.
* **Reduce unnecessary work:** Process entire ranges instead of checking every value individually.

## 5. Real-World Apps 🌍

**1. Google Calendar**

* Each meeting has a start time and an end time.
* Intervals help identify conflicting meetings and available time slots.

**2. Booking.com**

* A hotel reservation has check-in and check-out dates.
* Date intervals help determine whether a room is already reserved during the requested stay.

**3. Google Maps**

* Road closures and traffic conditions can be represented over specific time periods.
* These intervals help systems determine when a road restriction or traffic condition applies.

---
