class Solution1:
    def minimumPushes(self, word: str) -> int:
        # min push = 1
        # max push = 4
        # sort characters in word by DESC of frequency
        # keep the highest frequency characters on push = 1 (button 2)
        # second highest on next push = 1 (button 3)
        # this will go circular 2 -> ... -> 9 -> 2
        # and count total push

        def character_index(ch: str) -> int:
            return ord(ch) - ord("a")

        ordered_chars = [[chr(ord("a") + i), 0] for i in range(26)]

        for character in word:
            index = character_index(character)
            ordered_chars[index][1] += 1

        ordered_chars.sort(key=lambda x: x[1], reverse=True)

        total_pushes = 0

        for i in range(len(ordered_chars)):
            if ordered_chars[i][1] == 0:
                break

            # buttons are 2-9, so 8 buttons, each button can have 4 characters
            # the push count for each character is determined by its position in the ordered list
            push_count = (i // 8) + 1
            total_pushes += ordered_chars[i][1] * push_count

        return total_pushes

        # Complexity Analysis
        # Time : O(N * Log(N))
        # Space : O(26)


def p1():
    # Problem 1 : POTD Leetcode 3014. Minimum Number of Pushes to Type Word I - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/description/?envType=daily-question&envId=2026-07-30

    testcase = [
        ["abcde", 5],
        ["xycdefghij", 12],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minimumPushes(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxSubsetXOR(self, arr: list[int]) -> int:
        # code here

        N = len(arr)
        index = 0

        for bit in range(31, -1, -1):
            if index >= N:
                break

            max_index = index

            # find an element having current bit set
            for i in range(index, N):
                if (arr[i] & (1 << bit)) and arr[i] > arr[max_index]:
                    max_index = i

            # no pivot found for this bit
            if (arr[max_index] & (1 << bit)) == 0:
                continue

            # place the pivot at the current index
            arr[index], arr[max_index] = arr[max_index], arr[index]

            # eliminate the current bit
            for i in range(N):
                if i != index and (arr[i] & (1 << bit)):
                    arr[i] ^= arr[index]

            index += 1

        ans = 0

        for num in arr:
            ans ^= num

        return ans

        # Complexity Analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Maximum Subset XOR - https://www.geeksforgeeks.org/problems/maximum-subset-xor/1

    testcase = [
        [[2, 4, 5], 7],
        [[9, 8, 5], 13],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maxSubsetXOR(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 30 of July 2026

    p1()

    p2()
