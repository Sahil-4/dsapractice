class Solution1:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        N = len(nums)

        if N < 3:
            return N

        return 1 << N.bit_length()

        # Complexity analysis
        # Time : O(1)
        # Space: O(1)


def p1():
    # Problem 1 : POTD Leetcode 3513. Number of Unique XOR Triplets I - https://leetcode.com/problems/number-of-unique-xor-triplets-i/description/?envType=daily-question&envId=2026-07-23

    testcase = [
        [[1, 2], 2],
        [[3, 1, 2], 4],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.uniqueXorTriplets(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def canRepresentBST(self, arr: list[int]) -> bool:
        # code here
        stack = []
        lower_bound = float("-inf")

        for x in arr:
            if x < lower_bound:
                return False

            while stack and x > stack[-1]:
                lower_bound = stack.pop()

            stack.append(x)

        return True

        # Complexity analysis
        # Time : O(N)
        # Space: O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Check Preorder of BST - https://www.geeksforgeeks.org/problems/preorder-traversal-and-bst4006/1

    testcase = [
        [[2, 4, 3], True],
        [[2, 4, 1], False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.canRepresentBST(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 23 of July 2026

    p1()

    p2()
