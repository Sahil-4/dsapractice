from functools import cmp_to_key


class Solution1:
    @staticmethod
    def _cmp(a, b):
        # a and b are event lists like ["MESSAGE","2","HERE"] or ["OFFLINE","2","1"]
        ta, tb = int(a[1]), int(b[1])
        if ta != tb:
            return ta - tb
        # for equal timestamps: ensure OFFLINE comes before MESSAGE
        if a[0] == b[0]:
            return 0
        if a[0] == "OFFLINE" and b[0] == "MESSAGE":
            return -1
        if a[0] == "MESSAGE" and b[0] == "OFFLINE":
            return 1
        # fallback to lexicographic to be deterministic
        return -1 if a[0] < b[0] else 1

    @staticmethod
    def _solve(s: str):
        ids = []
        cur = ""
        for c in s:
            if c in ("i", "d"):  # original C++ skipped 'i' and 'd' characters
                continue
            if c == " ":
                if cur:
                    ids.append(int(cur))
                    cur = ""
            else:
                cur += c
        if cur:
            ids.append(int(cur))
        return ids

    def countMentions(self, numberOfUsers, events):
        online = [1] * numberOfUsers
        ans = [0] * numberOfUsers
        timestamp = [-1] * numberOfUsers

        events_sorted = sorted(events, key=cmp_to_key(self._cmp))

        for e in events_sorted:
            etype = e[0]
            time = int(e[1])

            # Bring users back online if 60+ seconds passed
            for i in range(numberOfUsers):
                if not online[i] and time - timestamp[i] >= 60:
                    online[i] = 1

            if etype == "MESSAGE":
                target = e[2]
                if target == "ALL":
                    for i in range(numberOfUsers):
                        ans[i] += 1
                elif target == "HERE":
                    for i in range(numberOfUsers):
                        if online[i]:
                            ans[i] += 1
                else:
                    ids = self._solve(target)
                    for uid in ids:
                        ans[uid] += 1
            else:  # OFFLINE event
                uid = int(e[2])
                online[uid] = 0
                timestamp[uid] = time

        return ans


def p1():
    # P1 POTD Leetcode 3433. Count Mentions Per User - https://leetcode.com/problems/count-mentions-per-user/?envType=daily-question&envId=2025-12-12

    testcase = [
        [
            2,
            [
                ["MESSAGE", "10", "id1 id0"],
                ["OFFLINE", "11", "0"],
                ["MESSAGE", "71", "HERE"],
            ],
            [2, 2],
        ],
        [
            2,
            [
                ["MESSAGE", "10", "id1 id0"],
                ["OFFLINE", "11", "0"],
                ["MESSAGE", "12", "ALL"],
            ],
            [2, 2],
        ],
        [
            2,
            [["OFFLINE", "10", "0"], ["MESSAGE", "12", "HERE"]],
            [0, 1],
        ],
        [
            3,
            [
                ["MESSAGE", "2", "HERE"],
                ["OFFLINE", "2", "1"],
                ["OFFLINE", "1", "0"],
                ["MESSAGE", "61", "HERE"],
            ],
            [1, 0, 2],
        ],
    ]

    for line in testcase:
        [numberOfUsers, events, expected] = line
        s1 = Solution1()
        result = s1.countMentions(numberOfUsers, events)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def transpose(self, mat):
        # code here
        # basically we have to change matrix[i][j] to matrix[j][i]
        # and matrix[j][i] to matrix[i][j]

        n = len(mat)

        for i in range(0, n):
            for j in range(i, n):
                temp = mat[i][j]
                mat[i][j] = mat[j][i]
                mat[j][i] = temp

        return mat

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(1)


def p2():
    # P2 POTD Geeksforgeeks Transpose of Matrix - https://www.geeksforgeeks.org/problems/transpose-of-matrix-1587115621/1

    testcase = [
        [
            [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]],
            [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
        ],
        [
            [[1, 2], [9, -2]],
            [[1, 9], [2, -2]],
        ],
    ]

    for line in testcase:
        [mat, expected] = line
        s2 = Solution2()
        result = s2.transpose(mat)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 12 of December 2025

    p1()

    p2()
