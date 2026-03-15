class Solution1:
    def minPartitions(self, n: str) -> int:
        # 32 = 10 + 11 + 11 = 32
        # 9999 = 1111 ... (9 times)
        # 9898 = 1111 ... (8 times) + 1010 total 9 times

        return int(max(n))

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers - https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/description/?envType=daily-question&envId=2026-03-01

    testcase = [
        ["32", 3],
        ["82734", 8],
        ["27346209830709182346", 9],
    ]

    for line in testcase:
        [n, expected] = line
        s1 = Solution1()
        result = s1.minPartitions(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def pushZerosToEnd(self, arr):
        insert_pos = 0  # place next non-zero element

        for i in range(len(arr)):
            if arr[i] != 0:
                # swap current element with insert_pos
                arr[i], arr[insert_pos] = arr[insert_pos], arr[i]
                insert_pos += 1

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Move All Zeroes to End - https://www.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1

    testcase = [
        [
            [1, 2, 0, 4, 3, 0, 5, 0],
            [1, 2, 4, 3, 5, 0, 0, 0],
        ],
        [
            [10, 20, 30],
            [10, 20, 30],
        ],
        [
            [0, 0],
            [0, 0],
        ],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        s2.pushZerosToEnd(arr)
        result = arr
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 1 of March 2026

    p1()

    p2()
