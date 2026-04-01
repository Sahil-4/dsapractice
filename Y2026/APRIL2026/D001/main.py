from typing import List


class Solution1:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        n = len(positions)

        # 0, 1, ..., n-1
        indices = list(range(n))

        # sort indices based on positions
        indices.sort(key=lambda i: positions[i])

        stack = []

        for currentIndex in indices:
            if directions[currentIndex] == "R":
                stack.append(currentIndex)
            else:
                while stack and healths[currentIndex] > 0:
                    topIndex = stack.pop()

                    if healths[topIndex] > healths[currentIndex]:
                        healths[topIndex] -= 1
                        healths[currentIndex] = 0
                        stack.append(topIndex)

                    elif healths[topIndex] < healths[currentIndex]:
                        healths[currentIndex] -= 1
                        healths[topIndex] = 0

                    else:
                        healths[currentIndex] = 0
                        healths[topIndex] = 0

        # collect survivors
        result = []
        for i in range(n):
            if healths[i] > 0:
                result.append(healths[i])

        return result

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 2751. Robot Collisions - https://leetcode.com/problems/robot-collisions/description/?envType=daily-question&envId=2026-04-01

    testcase = [
        [
            [5, 4, 3, 2, 1],
            [2, 17, 9, 15, 10],
            "RRRRR",
            [2, 17, 9, 15, 10],
        ],
        [
            [3, 5, 2, 6],
            [10, 10, 15, 12],
            "RLRL",
            [14],
        ],
        [
            [1, 2, 5, 6],
            [10, 10, 11, 11],
            "RLRL",
            [],
        ],
    ]

    for line in testcase:
        [positions, healths, directions, expected] = line
        s1 = Solution1()
        result = s1.survivedRobotsHealths(positions, healths, directions)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def memoization(self, n, last_used, memo):
        if n == 0:
            return 1

        if memo[n][last_used] != -1:
            return memo[n][last_used]

        # pick 0
        zero = self.memoization(n - 1, 0, memo)

        # pick 1
        one = self.memoization(n - 1, 1, memo) if last_used != 1 else 0

        memo[n][last_used] = zero + one

        return memo[n][last_used]

        # Complexity analysis
        # Time : O(2 ^ N)
        # Space : O(N) stack space

    def tabulation(self, N):
        curr_state = [1, 1]

        for n in range(1, N):
            next_state = [0, 0]

            for last_used in range(2):
                # pick 0
                zero = curr_state[0]

                # pick 1
                one = curr_state[1] if last_used != 1 else 0

                next_state[last_used] = zero + one

            curr_state = next_state

        return curr_state[0] + curr_state[1]

        # Complexity analysis
        # Time : O(2 * N)
        # Space : O(1)

    def countStrings(self, n):
        # code here

        # memo0 = [[-1 for _ in range(2)] for _ in range(n)]
        # memo1 = [[-1 for _ in range(2)] for _ in range(n)]
        # return self.memoization(n - 1, 0, memo0) + self.memoization(n - 1, 1, memo1)

        return self.tabulation(n)


def p2():
    # Problem 2 : POTD Geeksforgeeks Consecutive 1's not allowed - https://www.geeksforgeeks.org/problems/consecutive-1s-not-allowed1912/1

    testcase = [
        [3, 5],
        [2, 3],
        [1, 2],
    ]

    for line in testcase:
        [n, expected] = line
        s2 = Solution2()
        result = s2.countStrings(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 1 of April 2026

    p1()

    p2()
