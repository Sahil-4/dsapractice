from typing import List


class Solution1:
    def minJumps(self, arr: List[int]) -> int:
        N = len(arr)

        steps = 0

        if N == 1:
            return steps

        next_index_map = {}
        for i in range(N):
            if arr[i] not in next_index_map:
                next_index_map[arr[i]] = []
            next_index_map[arr[i]].append(i)

        source = 0
        destination = N - 1

        queue = []
        visited = [False] * N

        queue.append(source)
        visited[source] = True

        while queue:
            lsize = len(queue)

            for _ in range(lsize):
                curr_index = queue.pop(0)

                if curr_index == destination:
                    return steps

                if curr_index - 1 >= 0 and not visited[curr_index - 1]:
                    queue.append(curr_index - 1)
                    visited[curr_index - 1] = True

                if curr_index + 1 < N and not visited[curr_index + 1]:
                    queue.append(curr_index + 1)
                    visited[curr_index + 1] = True

                for j in next_index_map[arr[curr_index]]:
                    if not visited[j]:
                        queue.append(j)
                        visited[j] = True

                next_index_map[arr[curr_index]] = []

            steps += 1

        return N

        # Complexity analysis
        # Time : O(2N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1345. Jump Game IV - https://leetcode.com/problems/jump-game-iv/description/?envType=daily-question&envId=2026-05-18

    testcase = [
        [[100, -23, -23, 404, 100, 23, 23, 23, 3, 404], 3],
        [[7], 0],
        [[7, 6, 9, 6, 9, 6, 9, 7], 1],
        [[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 11], 2],
        [[-53, 97, 65, -78, -84, -56, -53, -78, 65, -62, -81, 11, 67, -53], 1],
    ]

    for line in testcase:
        [arr, expected] = line
        s1 = Solution1()
        result = s1.minJumps(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxSum(self, n: int) -> int:
        # code here

        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1

        # p1 = self.maxSum(n // 2)
        # p2 = self.maxSum(n // 3)
        # p3 = self.maxSum(n // 4)
        # psum = p1 + p2 + p3

        # return max(n, psum)

        dp = [-1] * (n + 1)

        if n >= 0:
            dp[0] = 0
        if n >= 1:
            dp[1] = 1

        for i in range(2, n + 1):
            p1 = dp[i // 2]
            p2 = dp[i // 3]
            p3 = dp[i // 4]
            dp[i] = max(i, p1 + p2 + p3)

        return dp[n]

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Maximum Sum Problem - https://www.geeksforgeeks.org/problems/maximum-sum-problem2211/1

    testcase = [[0, 0], [1, 1], [10, 10], [12, 13], [15, 15], [21, 22], [37, 41]]

    for line in testcase:
        [n, expected] = line
        s2 = Solution2()
        result = s2.maxSum(n)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 18 of May 2026

    p1()

    p2()
