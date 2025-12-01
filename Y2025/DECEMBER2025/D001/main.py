from typing import List


class Solution1:
    def answer_possible(self, n: int, batteries: List[int], mid: int) -> bool:
        target = mid * n
        possible = 0

        for health in batteries:
            possible += min(mid, health)
            if possible >= target:
                return True

        return False

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        low = min(batteries)
        high = sum(batteries) // n

        ans = 1

        while low <= high:
            mid = int(low + (high - low) / 2)
            if self.answer_possible(n, batteries, mid):
                low = mid + 1
                ans = mid
            else:
                high = mid - 1

        return ans

        # Complexity analysis
        # Time : O(N * Log(T))
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2141. Maximum Running Time of N Computers - https://leetcode.com/problems/maximum-running-time-of-n-computers/description/?envType=daily-question&envId=2025-12-01

    testcase = [
        [2, [3, 3, 3], 4],
        [2, [1, 1, 1, 1], 2],
    ]

    for line in testcase:
        [n, batteries, expected] = line
        s1 = Solution1()
        result = s1.maxRunTime(n, batteries)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class TrieNode:
    def __init__(self):
        self.child = [None, None]
        self.count = 0


class Solution2:
    def insert(self, root, num):
        node = root
        for i in range(15, -1, -1):
            bit = (num >> i) & 1
            if not node.child[bit]:
                node.child[bit] = TrieNode()
            node = node.child[bit]
            node.count += 1

    def countSmallerXor(self, root, num, k):
        node = root
        total = 0

        for i in range(15, -1, -1):
            if not node:
                break

            xbit = (num >> i) & 1
            kbit = (k >> i) & 1

            if kbit == 1:
                if node.child[xbit]:
                    total += node.child[xbit].count

                node = node.child[1 - xbit]

            else:
                node = node.child[xbit]

        return total

    def cntPairs(self, arr, k):
        root = TrieNode()
        ans = 0

        for num in arr:
            # count valid earlier nums
            ans += self.countSmallerXor(root, num, k)

            # insert current num
            self.insert(root, num)

        return ans

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD GeeksforgeeksXOR Pairs less than K - https://www.geeksforgeeks.org/problems/count-pairs-having-bitwise-xor-less-than-k/1

    testcase = [
        [[1, 2, 3, 5], 5, 4],
        [[3, 5, 6, 8], 7, 3],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        result = s2.cntPairs(arr, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 1 of December 2025

    p1()

    p2()
