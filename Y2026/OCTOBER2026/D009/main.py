from collections import Counter
import heapq


class Solution1:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        need_close = 0

        for c in s:
            if c == "(":
                if need_close & 1:
                    # odd:
                    # need one more ")"
                    # to make "())"
                    insertions += 1
                    need_close -= 1

                # need "))" for this "("
                need_close += 2

            else:
                need_close -= 1

                if need_close < 0:
                    # "(" was not available so have to insert
                    insertions += 1
                    need_close += 2  # - 1 + 2 = 1 (current included)

        return insertions + need_close

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1541. Minimum Insertions to Balance a Parentheses String - https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/description/?envType=daily-question&envId=2026-10-09

    testcase = [
        ["(()))", 1],
        ["())", 0],
        ["))())(", 3],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minInsertions(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def minOperation(self, n: int) -> int:
        # code here

        # def solve(i: int) -> int:
        #     if i == n:
        #         return 1

        #     if i > n:
        #         return n

        #     ops = n

        #     # add 1
        #     ops = min(ops, solve(i + 1))

        #     # double
        #     ops = min(ops, solve(i * 2))

        #     return 1 + ops

        # return solve(1)

        # 0 -> 1 -> 2 -> 4 -> 8
        # 0 -> 1 -> 2 -> 4 -> 5 -> 6 -> 7

        # ops = 1
        # i = 1

        # while i != n:
        #     if i * 2 <= n:
        #         i = i * 2
        #     else:
        #         i = i + 1

        #     ops += 1

        # return ops

        # 8 -> 4 -> 2 -> 1 -> 0
        # 7 -> 6 -> 3 -> 2 -> 1 -> 0

        ops = 0

        while n > 0:
            if n % 2 == 0:
                n //= 2
            else:
                n -= 1

            ops += 1

        return ops

        # Complexity analysis
        # Time : O(Log(N))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Minimum Operations to Reach n - https://www.geeksforgeeks.org/problems/find-optimum-operation4504/1

    testcase = [
        [8, 4],
        [7, 5],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.minOperation(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        mp = Counter(tasks)

        pq = [-count for count in mp.values()]
        heapq.heapify(pq)

        time = 0

        while pq:
            temp = []
            # first n + 1 intervals
            for _ in range(n + 1):
                if pq:
                    val = heapq.heappop(pq)
                    # val is negative, so val + 1 reduces the remaining count
                    temp.append(val + 1)

            for rem in temp:
                if rem < 0:
                    heapq.heappush(pq, rem)

            if not pq:  # all processes finished
                time += len(temp)
            else:
                time += n + 1  # completed a full round of n + 1 intervals

        return time

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 621. Task Scheduler - https://leetcode.com/problems/task-scheduler/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [["A", "A", "A", "B", "B", "B"], 2, 8],
        [["A", "C", "A", "B", "D", "B"], 1, 6],
        [["A", "A", "A", "B", "B", "B"], 3, 10],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.leastInterval(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 9 of October 2026

    p1()

    p2()

    p3()
