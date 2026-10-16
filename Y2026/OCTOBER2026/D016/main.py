class Solution1:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 1000000007
        N = len(nums)

        # fenwick trees supporting range add, range sum over cnt[l] (1-indexed);
        # cnt[l] = distinct elements in nums[l..r] for the current right end r
        tree1 = [0] * (N + 2)
        tree2 = [0] * (N + 2)

        def range_add(l: int, r: int):
            # cnt[l..r] += 1
            i = l
            while i <= N:
                tree1[i] += 1
                tree2[i] += l - 1
                i += i & -i

            i = r + 1
            while i <= N:
                tree1[i] -= 1
                tree2[i] -= r
                i += i & -i

        def prefix_sum(x: int) -> int:
            # sum of cnt[1..x]
            s1 = 0
            s2 = 0
            i = x
            while i > 0:
                s1 += tree1[i]
                s2 += tree2[i]
                i -= i & -i

            return s1 * x - s2

        last_seen = {}

        # sum of cnt[l] ^ 2 over l in [1..r]
        squares_sum = 0
        answer = 0

        for r in range(1, N + 1):
            prev = last_seen.get(nums[r - 1], 0)

            # for l in (prev, r] the distinct count grows by one: (c + 1)^2 - c^2 = 2c + 1
            # cnt[r] is still 0 before this step, so it needs no special handling
            window_sum = prefix_sum(r) - prefix_sum(prev)
            squares_sum += 2 * window_sum + (r - prev)

            range_add(prev + 1, r)
            last_seen[nums[r - 1]] = r

            answer = (answer + squares_sum) % MOD

        return answer

        # Complexity analysis
        # Time : O(N log N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 2916. Subarrays Distinct Element Sum of Squares II - https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/description/?envType=daily-question&envId=2026-10-16

    testcase = [
        [[1, 2, 1], 15],
        [[2, 2], 3],
        [[7], 1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.sumCounts(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countAlwaysFound(self, arr: list[int]):
        # code here

        N = len(arr)

        # arr[i] is found for every possible pivot sequence only if every pivot
        # sends the search towards i: all elements on the left are smaller,
        # all elements on the right are larger
        min_right = [0] * N
        min_right[N - 1] = arr[N - 1]
        for i in range(N - 2, -1, -1):
            min_right[i] = min(arr[i], min_right[i + 1])

        count = 0
        max_left = 0

        for i in range(N):
            right_ok = i == N - 1 or arr[i] < min_right[i + 1]
            left_ok = i == 0 or arr[i] > max_left

            if left_ok and right_ok:
                count += 1

            max_left = max(max_left, arr[i])

        return count

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Successful Binary Searches Irrespective of Pivot - https://www.geeksforgeeks.org/problems/count-always-found/1

    testcase = [
        [[3, 7, 9, 8, 15], 3],
        [[1], 1],
        [[1, 2, 3], 3],
        [[5, 4, 3, 2, 1], 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.countAlwaysFound(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)

        longest = 0

        for num in num_set:
            # only start counting from the beginning of a sequence
            if num - 1 in num_set:
                continue

            length = 1
            while num + length in num_set:
                length += 1

            longest = max(longest, length)

        return longest

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 128. Longest Consecutive Sequence - https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[100, 4, 200, 1, 3, 2], 4],
        [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9],
        [[1, 0, 1, 2], 3],
        [[], 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.longestConsecutive(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 16 of October 2026

    p1()

    p2()

    p3()
