from typing import List


class Solution1:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids_copy = asteroids.copy()
        planet_mass = mass

        asteroids_copy.sort()

        for asteroid in asteroids_copy:
            if asteroid > planet_mass:
                return False

            planet_mass += asteroid

        return True

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 2126. Destroying Asteroids - https://leetcode.com/problems/destroying-asteroids/description/?envType=daily-question&envId=2026-05-31

    testcase = [
        [10, [3, 9, 19, 5, 21], True],
        [5, [4, 9, 23, 4], False],
    ]

    for line in testcase:
        [mass, asteroids, expected] = line
        s1 = Solution1()
        result = s1.asteroidsDestroyed(mass, asteroids)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def isSumOfConsecutive(self, n: int) -> bool:
        # code here
        # a number can be written as the sum of consecutive positive numbers if it is not a power of 2
        # Sum(k consecutive) = k(2a + k - 1) / 2 = n
        # -> k(2a + k - 1) = 2n
        # if k % 2 == 0, then k is even and (k-1) is odd. even + odd = odd. Thus one should be even and the other should be odd
        # Every odd number n
        # -> n = (2m + 1) = m + (m+1) *sum of two consecutive

        if n == 1:
            return False

        return bool(n & (n - 1))

        # Complexity analysis
        # Time : O(1)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Express as Consecutive Number Sum - https://www.geeksforgeeks.org/problems/consecutive-numbers-for-sum3132/1

    testcase = [
        [10, True],
        [8, False],
        [24, True],
    ]

    for line in testcase:
        [n, expected] = line
        s2 = Solution2()
        result = s2.isSumOfConsecutive(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 31 of May 2026

    p1()

    p2()
