class Solution1:
    def sumCounts(self, nums: list[int]) -> int:
        N = len(nums)

        answer = 0

        for i in range(N):
            st = set()
            for j in range(i, N):
                st.add(nums[j])

                st_len = len(st)
                answer += st_len * st_len

        return answer

        # Complexity analysis
        # Time : O(N*N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2913. Subarrays Distinct Element Sum of Squares I - https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/?envType=daily-question&envId=2026-10-15

    testcase = [
        [[1, 2, 1], 15],
        [[1, 1], 3],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.sumCounts(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxValue(self, n: int) -> int:
        consecutive_ones = 0

        # Since n <= 10^9 < 2^30,
        # checking bits from 31 down to 0 covers all set bits
        for i in range(31, -1, -1):
            if (n >> i) & 1:
                consecutive_ones += 1

                if consecutive_ones == 3:
                    # Turn off the 3rd consecutive set bit
                    n &= ~(1 << i)
                    consecutive_ones = 0

            else:
                consecutive_ones = 0

        return n

        # Complexity analysis
        # Time : O(1)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Maximum Without 3 Consecutive Set Bits - https://www.geeksforgeeks.org/problems/geek-hates-too-many-1s--170647/1

    testcase = [
        [2, 2],
        [7, 6],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maxValue(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


from collections import deque


class Solution3:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            curr_word, steps = queue.popleft()

            if curr_word == endWord:
                return steps

            # Try mutating each character (L * 26 possibilities)
            for i in range(len(curr_word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    next_word = curr_word[:i] + ch + curr_word[i + 1 :]

                    if next_word in words and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, steps + 1))

        return 0

        # Complexity analysis
        # Time : O(N * L * L)
        # Space : O(N * L)


def p3():
    # Problem 3 : NC150 Leetcode 127. Word Ladder - https://leetcode.com/problems/word-ladder/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5],
        ["hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.ladderLength(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 15 of October 2026

    p1()

    p2()

    p3()
