import math
from typing import List


class Solution1:
    def check(self, mid: int, workerTimes: List[int], mh: int) -> bool:
        h = 0

        for t in workerTimes:
            h += int(math.sqrt(2.0 * mid / t + 0.25) - 0.5)

            if h >= mh:
                return True

        return h >= mh

    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        result = 0

        maxT = max(workerTimes)

        l = 1
        r = maxT * mountainHeight * (mountainHeight + 1) / 2

        while l <= r:
            mid = int((l + r) // 2)

            if self.check(mid, workerTimes, mountainHeight):
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result

        # Complexity analysis
        # Time : O(N * Log(tmax * H * H))
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3296. Minimum Number of Seconds to Make Mountain Height Zero - https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/description/?envType=daily-question&envId=2026-03-13

    testcase = [
        [4, [2, 1, 1], 3],
        [10, [3, 2, 2, 4], 12],
        [5, [1], 15],
    ]

    for line in testcase:
        [mountainHeight, workerTimes, expected] = line
        s1 = Solution1()
        result = s1.minNumberOfSeconds(mountainHeight, workerTimes)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    result: List[str] = []

    def is_valid_ip(self, address_str: str) -> bool:
        if address_str[0] == "0":
            return False
        return int(address_str) <= 255

    def generate_ips(
        self, s: str, curr_index: int, part: int, address_str: str
    ) -> None:
        if curr_index == self.N and part == 4:
            self.result.append(str(address_str[0:-1]))

        for i in range(1, 4):
            if curr_index + i > self.N:
                break

            if i == 1 or self.is_valid_ip(s[curr_index : curr_index + i]):
                self.generate_ips(
                    s,
                    curr_index + i,
                    part + 1,
                    address_str + s[curr_index : curr_index + i] + ".",
                )

    def generateIp(self, s: str) -> List[str]:
        # Code here
        self.result = []
        self.N = len(s)

        if self.N > 12:
            return self.result

        self.generate_ips(s, 0, 0, "")

        return self.result

        # Complexity analysis
        # Time : O(3^4)
        # Space : O(K)


def p2():
    # Problem 2 : POTD Geeksforgeeks Generate IP Addresses - https://www.geeksforgeeks.org/problems/generate-ip-addresses/1

    testcase = [
        ["255678166", ["25.56.78.166", "255.6.78.166", "255.67.8.166", "255.67.81.66"]],
        ["25505011535", []],
    ]

    for line in testcase:
        [s, expected] = line
        s2 = Solution2()
        result = s2.generateIp(s)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 13 of March 2026

    p1()

    p2()
