from typing import List


class Solution1:
    def processStr(self, s: str) -> str:
        result = []

        for character in s:
            if character >= "a" and character <= "z":
                result.append(character)
            elif character == "*":
                if result:
                    result.pop()
            elif character == "#":
                result = result + result
            elif character == "%":
                result = result[::-1]

        return "".join(result)

        # Complexity analysis
        # Time : O(N * N)
        # Space : O(N * N)


def p1():
    # Problem 1 : POTD Leetcode 3612. Process String with Special Operations I - https://leetcode.com/problems/process-string-with-special-operations-i/description/?envType=daily-question&envId=2026-06-16

    testcase = [
        ["a#b%*", "ba"],
        ["z*#", ""],
    ]

    for line in testcase:
        [s, expected] = line
        s1 = Solution1()
        result = s1.processStr(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def constructList(self, queries: List[List[int]]) -> List[int]:
        # code here
        result = [0]
        cumulative_xor = 0

        for t, x in queries:
            if t == 0:
                result.append(x ^ cumulative_xor)
            else:
                cumulative_xor ^= x

        for i in range(len(result)):
            result[i] ^= cumulative_xor

        result.sort()

        return result


def p2():
    # Problem 2 : POTD Geeksforgeeks Construct List using XOR Queries - https://www.geeksforgeeks.org/problems/construct-list-using-given-q-xor-queries/1

    testcase = [
        [5, [[0, 6], [0, 3], [0, 2], [1, 4], [1, 5]], [1, 2, 3, 7]],
        [3, [[0, 2], [1, 3], [0, 5]], [1, 3, 5]],
    ]

    for line in testcase:
        [_, queries, expected] = line
        s2 = Solution2()
        result = s2.constructList(queries)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 16 of June 2026

    p1()

    p2()
