from collections import deque


class Solution1:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        # suffix automaton over the array : every state stands for a group of substrings
        # that share the same set of end positions, with lengths (len[link] + 1 .. len[state])
        transitions = [{}]
        link = [-1]
        length = [0]
        count = [0]  # number of occurrences of the substrings of the state
        last = 0

        for value in nums:
            current = len(length)
            transitions.append({})
            link.append(-1)
            length.append(length[last] + 1)
            count.append(1)

            p = last
            while p != -1 and value not in transitions[p]:
                transitions[p][value] = current
                p = link[p]

            if p == -1:
                link[current] = 0
            else:
                q = transitions[p][value]

                if length[p] + 1 == length[q]:
                    link[current] = q
                else:
                    clone = len(length)
                    transitions.append(dict(transitions[q]))
                    link.append(link[q])
                    length.append(length[p] + 1)
                    count.append(0)

                    while p != -1 and transitions[p].get(value) == q:
                        transitions[p][value] = clone
                        p = link[p]

                    link[q] = clone
                    link[current] = clone

            last = current

        # propagate occurrence counts from the longest states to their suffix links
        for state in sorted(range(1, len(length)), key=lambda s: -length[s]):
            count[link[state]] += count[state]

        # a state with exactly one occurrence holds only unique substrings,
        # the shortest of them has length len[link] + 1
        answer = len(nums)
        for state in range(1, len(length)):
            if count[state] == 1:
                answer = min(answer, length[link[state]] + 1)

        return answer

        # Complexity analysis
        # Time : O(N Log(N)) for the length ordering, the automaton itself is O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3934. Smallest Unique Subarray - https://leetcode.com/problems/smallest-unique-subarray/description/?envType=daily-question&envId=2026-11-25

    testcase = [
        [[3, 3, 3], 3],
        [[2, 1, 2, 3, 3], 1],
        [[1, 1, 2, 2, 1], 2],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.smallestUniqueSubarray(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minTime(self, a: int, b: int, d: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        # Geek always moves at 1 unit per second, so the time to first reach position x
        # is x + 2 * b * k(x), where k(x) is the number of full (forward a, backward b)
        # cycles needed before the forward leg of cycle k reaches x :
        #   k(x) = 0 for x <= a, otherwise ceil((x - a) / (a - b))
        # With jump length j the answer is f(d - j) + 1, which is never worse than
        # walking to d (the step before first reaching d is at d - 1, so f(d - 1) + 1 <= f(d))
        gain = a - b

        def sum_k(n: int) -> int:
            # sum of k(x) for x = 1..n
            M = n - a

            if M <= 0:
                return 0

            # sum of ceil(m / gain) for m = 1..M = M + sum of floor(t / gain) for t = 0..M-1
            q, rem = divmod(M, gain)

            return M + gain * q * (q - 1) // 2 + q * rem

        low, high = d - r, d - l  # positions x = d - j, for j = r .. l
        count = high - low + 1

        position_sum = (low + high) * count // 2
        cycles = sum_k(high) - sum_k(low - 1)

        return (position_sum + 2 * b * cycles + count) % MOD

        # Complexity analysis
        # Time : O(1)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Geek's Destination with Special Jump - https://www.geeksforgeeks.org/problems/geek-and-her-destination--145724/1

    testcase = [
        [2, 1, 5, 3, 4, 5],
        [4, 2, 8, 2, 4, 26],
        [5, 2, 60, 3, 40, 3249],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minTime(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # window : indices of a decreasing sequence of values, the front is the window maximum
        window = deque()
        answer = []

        for i, value in enumerate(nums):
            # smaller values behind the new one can never be a maximum again
            while window and nums[window[-1]] <= value:
                window.pop()

            window.append(i)

            # drop the front when it slides out of the window
            if window[0] <= i - k:
                window.popleft()

            if i >= k - 1:
                answer.append(nums[window[0]])

        return answer

        # Complexity analysis
        # Time : O(N)
        # Space : O(K)


def p3():
    # Problem 3 : NC150 Leetcode 239. Sliding Window Maximum - https://leetcode.com/problems/sliding-window-maximum/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]],
        [[1], 1, [1]],
        [[9, 8, 7, 6], 2, [9, 8, 7]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.maxSlidingWindow(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 25 of November 2026

    p1()

    p2()

    p3()
