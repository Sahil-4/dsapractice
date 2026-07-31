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
    # Problem 1 : POTD Leetcode 3016. Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/?envType=daily-question&envId=2026-07-31

    testcase = [
        ["abcde", 5],
        ["xyzxyzxyzxyz", 12],
        ["aabbccddeeffgghhiiiiii", 24],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.minimumPushes(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def countSubsets(self, arr: list[int]) -> int:
        # code here

        MOD = 10**9 + 7

        def power(a: int, b: int) -> int:
            result = 1

            while b:
                if b & 1:
                    result = (result * a) % MOD

                a = (a * a) % MOD
                b >>= 1

            return result

        def getMask(num: int) -> int:
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
            N = len(primes)

            mask = 0

            for i in range(N):
                p = primes[i]
                cnt = 0

                while num % p == 0:
                    cnt += 1
                    num //= p

                if cnt > 1:
                    return -1

                if cnt == 1:
                    mask |= 1 << i

            return mask

        freq = [0] * 31
        for x in arr:
            freq[x] += 1

        ones = freq[1]

        dp = [0] * 1024
        dp[0] = 1

        for num in range(2, 31):

            if freq[num] == 0:
                continue

            currMask = getMask(num)

            if currMask == -1:
                continue

            for mask in range(1023, -1, -1):

                if (mask & currMask) != 0:
                    continue

                dp[mask | currMask] = (dp[mask | currMask] + dp[mask] * freq[num]) % MOD

        ans = 0
        T = 2**10

        for mask in range(1, T):
            ans = (ans + dp[mask]) % MOD

        ans = (ans * power(2, ones)) % MOD

        return ans

        # Complexity Analysis
        # Time : O(30 * 2^10)
        # Space : O(2^10)


def p2():
    # Problem 2 : POTD Geeksforgeeks Subsets with Products of Distinct Primes - https://www.geeksforgeeks.org/problems/game-of-subsets/1

    testcase = [
        [[1, 2, 3, 4], 6],
        [[2, 2, 3], 5],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.countSubsets(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 31 of July 2026

    p1()

    p2()
