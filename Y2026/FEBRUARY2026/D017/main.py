from typing import List


class Solution1:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []

        for hour in range(0, 12):
            for minutes in range(0, 60):
                if hour.bit_count() + minutes.bit_count() == turnedOn:
                    minutes_str = minutes if minutes > 9 else f"0{minutes}"
                    time_str = f"{hour}:{minutes_str}"
                    result.append(time_str)

        return result

        # Complexity analysis
        # Time : O(1)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 401. Binary Watch - https://leetcode.com/problems/binary-watch/description/?envType=daily-question&envId=2026-02-17

    testcase = [
        [
            1,
            [
                "0:01",
                "0:02",
                "0:04",
                "0:08",
                "0:16",
                "0:32",
                "1:00",
                "2:00",
                "4:00",
                "8:00",
            ],
        ],
        [
            2,
            [
                "0:03",
                "0:05",
                "0:06",
                "0:09",
                "0:10",
                "0:12",
                "0:17",
                "0:18",
                "0:20",
                "0:24",
                "0:33",
                "0:34",
                "0:36",
                "0:40",
                "0:48",
                "1:01",
                "1:02",
                "1:04",
                "1:08",
                "1:16",
                "1:32",
                "2:01",
                "2:02",
                "2:04",
                "2:08",
                "2:16",
                "2:32",
                "3:00",
                "4:01",
                "4:02",
                "4:04",
                "4:08",
                "4:16",
                "4:32",
                "5:00",
                "6:00",
                "8:01",
                "8:02",
                "8:04",
                "8:08",
                "8:16",
                "8:32",
                "9:00",
                "10:00",
            ],
        ],
        [9, []],
    ]

    for line in testcase:
        [turnedOn, expected] = line
        s1 = Solution1()
        result = s1.readBinaryWatch(turnedOn)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def overlapInt(self, arr):
        # code here
        intervals = []

        for time in arr:
            [start, end] = time
            intervals.append([start, 0])
            intervals.append([end, 1])

        intervals.sort()

        max_overlapping = 0
        overlapping = 0

        for interval in intervals:
            if interval[1] == 0:
                overlapping += 1
            else:
                overlapping -= 1

            max_overlapping = max(max_overlapping, overlapping)

        return max_overlapping

        # Complexity analysis
        # Time : O(N * Log(N)) + O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Maximum number of overlapping Intervals - https://www.geeksforgeeks.org/problems/intersecting-intervals/1

    testcase = [
        [[[1, 2], [2, 4], [3, 6]], 2],
        [[[1, 8], [2, 5], [5, 6], [3, 7]], 4],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.overlapInt(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 17 of February 2026

    p1()

    p2()
