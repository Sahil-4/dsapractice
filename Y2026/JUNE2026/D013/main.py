from typing import List


class Solution1:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        def reverse_mapping(index) -> str:
            # z-0 = z
            # z-1 = y
            # z-index -> out
            return chr(ord("z") - index)

        def get_word_weight(word: str) -> int:
            weight = 0

            for ch in word:
                index = ord(ch) - ord("a")
                weight += weights[index]

            return weight

        final_answer = []

        for word in words:
            weight = get_word_weight(word)
            mod_weight = weight % 26
            final_answer.append(reverse_mapping(mod_weight))

        return "".join(final_answer)

        # Complexity analysis
        # Time : O(N * W)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3838. Weighted Word Mapping - https://leetcode.com/problems/weighted-word-mapping/description/?envType=daily-question&envId=2026-06-13

    testcase = [
        [
            ["abcd", "def", "xyz"],
            [
                5,
                3,
                12,
                14,
                1,
                2,
                3,
                2,
                10,
                6,
                6,
                9,
                7,
                8,
                7,
                10,
                8,
                9,
                6,
                9,
                9,
                8,
                3,
                7,
                7,
                2,
            ],
            "rij",
        ],
        [
            ["a", "b", "c"],
            [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
            "yyy",
        ],
        [
            ["abcd"],
            [
                7,
                5,
                3,
                4,
                3,
                5,
                4,
                9,
                4,
                2,
                2,
                7,
                10,
                2,
                5,
                10,
                6,
                1,
                2,
                2,
                4,
                1,
                3,
                4,
                4,
                5,
            ],
            "g",
        ],
    ]

    for line in testcase:
        [words, weights, expected] = line
        s1 = Solution1()
        result = s1.mapWordWeights(words, weights)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def computeValue(self, n: int) -> int:
        MOD = 10**9 + 7

        factorial_n = 1
        factorial_2n = 1

        for i in range(1, 2 * n + 1):
            factorial_2n = (factorial_2n * i) % MOD
            if i == n:
                factorial_n = factorial_2n

        inverse_fact_n = pow(factorial_n, MOD - 2, MOD)

        return (factorial_2n * inverse_fact_n % MOD) * inverse_fact_n % MOD

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Binary Strings with Equal Sum of Two Halves - https://www.geeksforgeeks.org/problems/count-even-length1907/1

    testcase = [
        [2, 6],
        [1, 2],
    ]

    for line in testcase:
        [n, expected] = line
        s2 = Solution2()
        result = s2.computeValue(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 13 of June 2026

    p1()

    p2()
