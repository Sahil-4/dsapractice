class Solution1:
    def sortableIntegers(self, nums: list[int]) -> int:
        N = len(nums)

        def is_sortable(k: int) -> bool:
            prev_max = -1

            for start in range(0, N, k):
                drops = 0

                block_min = nums[start]
                block_max = nums[start]

                for j in range(k):
                    curr = nums[start + j]
                    nxt = nums[start + (j + 1) % k]

                    if curr > nxt:
                        drops += 1
                        if drops > 1:
                            return False

                    if curr < block_min:
                        block_min = curr
                    if curr > block_max:
                        block_max = curr

                # previous block's maximum must not exceed the current block's minimum
                if prev_max != -1 and prev_max > block_min:
                    return False

                prev_max = block_max

            return True

        # find all divisors of N
        divisors = []
        d = 1
        while d * d <= N:
            if N % d == 0:
                divisors.append(d)
                if d * d != N:
                    divisors.append(N // d)
            d += 1

        total_sum = 0
        for k in divisors:
            if is_sortable(k):
                total_sum += k

        return total_sum

        # Complexity analysis
        # Time : O(d(N) * N)
        # Space : O(d(N))


def p1():
    # Problem 1 : POTD Leetcode 3886. Sum of Sortable Integers - https://leetcode.com/problems/sum-of-sortable-integers/description/?envType=daily-question&envId=2026-10-20

    testcase = [
        [[3, 1, 2], 3],
        [[7, 6, 5], 0],
        [[5, 8], 3],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.sortableIntegers(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def lexicographicallyLargest(self, arr: list[int]) -> list[int]:
        # code here

        N = len(arr)
        i = 0

        # for each maximal contiguous subarray having the same parity
        while i < N:
            # find end of this group
            j = i + 1
            while j < N and arr[j] % 2 == arr[j - 1] % 2:
                j += 1

            # sort them in descending order
            arr[i:j] = sorted(arr[i:j], reverse=True)

            i = j

        return arr

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Largest with Same Parity Adjacent Swaps - https://www.geeksforgeeks.org/problems/even-swap/1

    testcase = [
        [[1, 3, 5], [5, 3, 1]],
        [[1, 3, 4, 2], [3, 1, 4, 2]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.lexicographicallyLargest(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)

        # answer not possible
        if total_cost > total_gas:
            return -1

        N = len(gas)

        fuel_tank = 0
        si = 0

        for i in range(N):
            fuel_tank += gas[i]
            fuel_tank -= cost[i]

            # reset if chosen index was wrong, did not give answer
            if fuel_tank < 0:
                si = i + 1
                fuel_tank = 0

        return si

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p3():
    # Problem 3 : NC150 Leetcode 134. Gas Station - https://leetcode.com/problems/gas-station/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3],
        [[2, 3, 4], [3, 4, 3], -1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.canCompleteCircuit(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 20 of October 2026

    p1()

    p2()

    p3()
