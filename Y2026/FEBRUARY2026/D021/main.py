from typing import List


class Solution1:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # prime set
        primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])

        # count of nums having prime set bits
        count = 0

        # try all num in [left, right] incl
        for num in range(left, right + 1):
            # if bit count is prime
            if num.bit_count() in primes:
                count += 1

        return count

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 762. Prime Number of Set Bits in Binary Representation - https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/?envType=daily-question&envId=2026-02-21

    testcase = [
        [6, 10, 4],
        [10, 15, 5],
    ]

    for line in testcase:
        [left, right, expected] = line
        s1 = Solution1()
        result = s1.countPrimeSetBits(left, right)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def hIndex(self, citations: List[int]) -> int:
        # code here
        # there are h papers with h citations
        # if h is 1 then there is 1 paper with citations 1
        # if h is 2 then there are 2 papers with citations 2
        # if h is 3 then there are 3 papers with citations 3
        # we have to find the maximum h
        # can be solved using binary search (on H, where H can be in [0, N])
        # efficient solution is to use counting sort

        N = len(citations)

        counting_bucket = [0] * (N + 1)

        # citation count - fill bucket
        for citation in citations:
            if citation >= N:
                counting_bucket[N] += 1
            else:
                counting_bucket[citation] += 1

        # return max possible H
        count = 0
        for i in range(N, -1, -1):
            count += counting_bucket[i]
            if count >= i:
                return i

        return 0

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Find H-Index - https://www.geeksforgeeks.org/problems/find-h-index--165609/1

    testcase = [
        [[3, 0, 5, 3, 0], 3],
        [[5, 1, 2, 4, 1], 2],
        [[0, 0], 0],
    ]

    for line in testcase:
        [citations, expected] = line
        s2 = Solution2()
        result = s2.hIndex(citations)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 21 of February 2026

    p1()

    p2()
