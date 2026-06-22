class Solution1:
    def maxNumberOfBalloons(self, text: str) -> int:
        character_frequency = [0] * 26
        character_ratio = {1: 1, 0: 1, 11: 2, 14: 2, 13: 1}  # balloon

        for ch in text:
            character_frequency[ord(ch) - ord("a")] += 1

        ballon_count = len(text)
        for chi, rt in character_ratio.items():
            ballon_count = min(ballon_count, character_frequency[chi] // rt)

        return ballon_count

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 1189. Maximum Number of Balloons - https://leetcode.com/problems/maximum-number-of-balloons/description/?envType=daily-question&envId=2026-06-22

    testcase = [
        ["nlaebolko", 1],
        ["loonbalxballpoon", 2],
        ["leetcode", 0],
        ["balon", 0],
        ["ballon", 0],
    ]

    for line in testcase:
        [text, expected] = line
        s1 = Solution1()
        result = s1.maxNumberOfBalloons(text)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxArea(self, height: list[int]) -> int:
        # code here
        m_area = 0

        left, right = 0, len(height) - 1

        while left < right:
            m_area = max(m_area, min(height[left], height[right]) * (right - left - 1))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return m_area

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Maximum Area Between Bars - https://www.geeksforgeeks.org/problems/dam-of-candies--141631/1

    testcase = [
        [[2, 5, 4, 3, 7], 10],
        [[1, 3, 4], 1],
        [[5, 5, 5, 5], 10],
        [[1, 2, 3, 4, 5], 4],
        [[100, 1, 1, 1, 100], 300],
    ]

    for line in testcase:
        [height, expected] = line
        s2 = Solution2()
        result = s2.maxArea(height)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 22 of June 2026

    p1()

    p2()
