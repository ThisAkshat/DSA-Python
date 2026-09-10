class RecentCounter(object):

    def __init__(self):
        self.requests = []
        

    def ping(self, t):
        self.requests.append(t)

        while self.requests[0] < t - 3000:
            self.requests.pop(0)
        
        return len(self.requests)

  """
# 933. Number of Recent Calls
# https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter(object):
    def __init__(self):
        self.requests = []

    def ping(self, t):
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.pop(0)
        return len(self.requests)


# ============================================================
# DRY RUN
# ============================================================
#
# Calls: ping(1), ping(100), ping(3001), ping(3002)
#
# ------------------------------------------------------------
# Constructor: RecentCounter()
# ------------------------------------------------------------
# self.requests = []
#
# ------------------------------------------------------------
# Call 1: ping(1)
# ------------------------------------------------------------
# Append              -> self.requests.append(1)
#                        self.requests = [1]
# Window start        -> t - 3000 = 1 - 3000 = -2999
# While check         -> self.requests[0] < -2999  ->  1 < -2999  -> False
#                        loop does not run
# Return              -> len(self.requests) = 1
#
# Output: 1   (expected: 1)  MATCH
#
# ------------------------------------------------------------
# Call 2: ping(100)
# ------------------------------------------------------------
# Append              -> self.requests.append(100)
#                        self.requests = [1, 100]
# Window start        -> t - 3000 = 100 - 3000 = -2900
# While check         -> self.requests[0] < -2900  ->  1 < -2900  -> False
#                        loop does not run
# Return              -> len(self.requests) = 2
#
# Output: 2   (expected: 2)  MATCH
#
# ------------------------------------------------------------
# Call 3: ping(3001)
# ------------------------------------------------------------
# Append              -> self.requests.append(3001)
#                        self.requests = [1, 100, 3001]
# Window start        -> t - 3000 = 3001 - 3000 = 1
# While check         -> self.requests[0] < 1  ->  1 < 1  -> False
#                        (range is inclusive, so 1 still counts)
#                        loop does not run
# Return              -> len(self.requests) = 3
#
# Output: 3   (expected: 3)  MATCH
#
# ------------------------------------------------------------
# Call 4: ping(3002)
# ------------------------------------------------------------
# Append              -> self.requests.append(3002)
#                        self.requests = [1, 100, 3001, 3002]
# Window start        -> t - 3000 = 3002 - 3000 = 2
# While check #1      -> self.requests[0] < 2  ->  1 < 2  -> True
#                        1 has expired, remove it
# Pop                 -> self.requests.pop(0)
#                        self.requests = [100, 3001, 3002]
# While check #2      -> self.requests[0] < 2  ->  100 < 2  -> False
#                        loop stops
# Return              -> len(self.requests) = 3
#
# Output: 3   (expected: 3)  MATCH
#
# ------------------------------------------------------------
# SUMMARY TABLE
# ------------------------------------------------------------
# Call          | List after append          | Expired | Final list           | Return
# --------------|-----------------------------|---------|-----------------------|-------
# ping(1)       | [1]                         | none    | [1]                   | 1
# ping(100)     | [1, 100]                    | none    | [1, 100]              | 2
# ping(3001)    | [1, 100, 3001]              | none    | [1, 100, 3001]        | 3
# ping(3002)    | [1, 100, 3001, 3002]        | 1       | [100, 3001, 3002]     | 3
#
# ------------------------------------------------------------
# CORE MECHANISM
# ------------------------------------------------------------
# Every call appends the new timestamp, then the while loop removes any
# entries from the front of the list that fall outside the [t-3000, t]
# window (a sliding window pattern). The remaining count is the answer.
  """
