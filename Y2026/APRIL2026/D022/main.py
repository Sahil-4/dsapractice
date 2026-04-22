from typing import List


class Solution1:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        # find word in queries such that
        # distance(word, dictionary[u]) <= 2
        # distance returns the number of indexes having different characters
        # and 0 <= u < dictionary.length

        answer = []

        for word in queries:
            for dictionary_word in dictionary:
                distance = 0
                for i in range(len(word)):
                    if word[i] != dictionary_word[i]:
                        distance += 1

                if distance <= 2:
                    answer.append(word)
                    break

        return answer

        # Complexity analysis
        # Time : O(N * M)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2452. Words Within Two Edits of Dictionary - https://leetcode.com/problems/words-within-two-edits-of-dictionary/description/?envType=daily-question&envId=2026-04-22

    testcase = [
        [
            ["word", "note", "ants", "wood"],
            ["wood", "joke", "moat"],
            ["word", "note", "wood"],
        ],
        [
            ["yes"],
            ["not"],
            [],
        ],
    ]

    for line in testcase:
        [queries, dictionary, expected] = line
        s1 = Solution1()
        result = s1.twoEditWords(queries, dictionary)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def findMean(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # code here

        N = len(arr)
        M = len(queries)

        prefix_sum = [0] * (N + 1)

        for i in range(N):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]

        mean_array = [0] * M

        for i in range(M):
            [l, r] = queries[i]

            mean_array[i] = (prefix_sum[r + 1] - prefix_sum[l]) // (r - l + 1)

        return mean_array

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Mean of range in array - https://www.geeksforgeeks.org/problems/mean-of-range-in-array2123/1

    testcase = [
        [[1, 2, 3, 4, 5], [[0, 2], [1, 3], [0, 4]], [2, 3, 3]],
        [[6, 7, 8, 10], [[0, 3], [1, 2]], [7, 7]],
        [[1, 2, 3, 4, 5], [[0, 4]], [3]],
    ]

    for line in testcase:
        [arr, queries, expected] = line
        s2 = Solution2()
        result = s2.findMean(arr, queries)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 22 of April 2026

    p1()

    p2()
