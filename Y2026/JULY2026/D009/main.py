class Solution1:
    def pathExistenceQueries(
        self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]
    ) -> list[bool]:

        # connected component of every index
        component = [0] * n

        current_component = 0

        for index in range(1, n):
            if nums[index] - nums[index - 1] > maxDiff:
                current_component += 1

            component[index] = current_component

        answer = []

        for source, destination in queries:
            answer.append(component[source] == component[destination])

        return answer

        # Complexity analysis
        # Time : O(N + Q)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3532. Path Existence Queries in a Graph I - https://leetcode.com/problems/path-existence-queries-in-a-graph-i/description/?envType=daily-question&envId=2026-07-09

    testcase = [
        [
            2,
            [1, 3],
            1,
            [[0, 0], [0, 1]],
            [True, False],
        ],
        [
            4,
            [2, 5, 6, 8],
            2,
            [[0, 1], [0, 2], [1, 3], [2, 3]],
            [False, False, True, True],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.pathExistenceQueries(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countKdivPairs(self, arr: list[int], k: int) -> int:
        # code here

        remainder_frequency = dict()
        for e1 in arr:
            modded = e1 % k

            if modded not in remainder_frequency:
                remainder_frequency[modded] = 0

            remainder_frequency[modded] += 1

        count = 0

        for remainder, frequency in remainder_frequency.items():
            complement = (-remainder) % k

            if complement not in remainder_frequency:
                continue

            if remainder == complement:
                count += frequency * (frequency - 1) // 2

            elif remainder < complement:
                count += frequency * remainder_frequency[complement]

        return count

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count Pairs Divisible By K - https://www.geeksforgeeks.org/problems/count-pairs-in-array-divisible-by-k/1

    testcase = [
        [[2, 2, 1, 7, 5, 3], 4, 5],
        [[5, 9, 36, 74, 52, 31, 42], 3, 7],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.countKdivPairs(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 9 of July 2026

    p1()

    p2()
