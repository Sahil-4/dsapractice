from typing import List


class Solution1:
    def hasAllCodes(self, s: str, k: int) -> bool:
        LIMIT = 1 << k
        N = len(s)

        codes = set()

        for i in range(k, N + 1):
            codes.add(s[i - k : i])
            if len(codes) == LIMIT:
                break

        return len(codes) == LIMIT

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1461. Check If a String Contains All Binary Codes of Size K - https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/?envType=daily-question&envId=2026-02-23

    testcase = [
        ["00110110", 2, True],
        ["0110", 1, True],
        ["0110", 2, False],
    ]

    for line in testcase:
        [s, k, expected] = line
        s1 = Solution1()
        result = s1.hasAllCodes(s, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findUnion(self, a: List[int], b: List[int]) -> List[int]:
        # code here
        return list(set([*a, *b]))

        # Complexity analysis
        # Time : O(2 * (N+M))
        # Space : O(N+M)


def p2():
    # Problem 2 : POTD Geeksforgeeks Union of Arrays with Duplicates - https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1

    testcase = [
        [[1, 2, 3, 2, 1], [3, 2, 2, 3, 3, 2], [1, 2, 3]],
        [[1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]],
        [[1, 2, 1, 1, 2], [2, 2, 1, 2, 1], [1, 2]],
    ]

    for line in testcase:
        [a, b, expected] = line
        s2 = Solution2()
        result = s2.findUnion(a, b)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 23 of February 2026

    p1()

    p2()
