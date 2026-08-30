class Solution1:
    def minimumDeletions(self, nums: list[int]) -> int:
        N = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # make min_idx the smaller index
        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # case 1 - remove both from the front
        front = right + 1

        # case 2 - remove both from the back
        back = N - left

        # case 3 - remove left from front and right from back
        both_sides = (left + 1) + (N - right)

        return min(front, back, both_sides)

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2091. Removing Minimum and Maximum From Array - https://leetcode.com/problems/removing-minimum-and-maximum-from-array/description/?envType=daily-question&envId=2026-08-30

    testcase = [
        [[2, 10, 7, 5, 4, 1, 8, 6], 5],
        [[0, -4, 19, 1, 8, -2, -3, 5], 3],
        [[101], 1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minimumDeletions(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def getMarks(self, l: list[int], r: list[int], rank: list[int]) -> list[int]:
        """Return the mark corresponding to each requested rank."""

        # keep original positions so we can restore the required order
        queries = sorted(enumerate(rank), key=lambda x: x[1])

        result = [0] * len(rank)

        interval_idx = 0
        first_rank = 1

        for original_idx, requested_rank in queries:

            # find interval containing requested_rank
            while True:
                interval_size = r[interval_idx] - l[interval_idx] + 1
                last_rank = first_rank + interval_size - 1

                if requested_rank <= last_rank:
                    break

                first_rank = last_rank + 1
                interval_idx += 1

            # find position inside the current interval
            position = requested_rank - first_rank

            # convert position to the actual mark
            mark = l[interval_idx] + position

            result[original_idx] = mark

        return result

        # Complexity analysis
        # Time : O(L * Log(L) + L + K)
        # Space : O(K)


def p2():
    # Problem 2 : POTD Geeksforgeeks Marks from Ranks - https://www.geeksforgeeks.org/problems/find-marks-from-ranks/1

    testcase = [
        [[1, 6, 14], [3, 9, 15], [2, 5, 8], [2, 7, 14]],
        [[5, 10], [7, 12], [1, 4, 6], [5, 10, 12]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.getMarks(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 30 of August 2026

    p1()

    p2()
