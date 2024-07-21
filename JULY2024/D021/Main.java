import java.util.Arrays;

class Main {
    private static void swapAdjacent(int[] arr) {
        for (int i = 0; i < arr.length; i += 2) {
            if (i + 1 == arr.length)
                break;

            arr[i] = arr[i] ^ arr[i + 1];
            arr[i + 1] = arr[i] ^ arr[i + 1];
            arr[i] = arr[i] ^ arr[i + 1];
        }
    }

    public static int[] numberGame(int[] nums) {
        Arrays.sort(nums);
        swapAdjacent(nums);

        return nums;
    }

    public static void p1() {
        // Problem 1 : Leetcode 2974. Minimum Number Game -
        // https://leetcode.com/problems/minimum-number-game/

        int arr[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        int arr2[] = numberGame(arr);

        for (int i = 0; i < arr2.length; i++)
            System.out.println(arr2[i]);
    }

    public static boolean canJump(int[] nums, int n) {
        boolean possibility = true;
        n = n - 1;
        int reached = 0;

        for (int i = 0; i <= n; i++) {
            if (i > reached)
                return false;

            int can_reach = i + nums[i];
            reached = Math.max(reached, can_reach);
            if (reached == n)
                break;
        }

        return possibility;
    }

    public static int jump(int[] arr, int n) {
        // your code here
        int jumps = 0;
        int l = 0, r = 0;

        while (r < n - 1) {
            int farthest = 0;
            for (int i = l; i <= r; i++) {
                farthest = Math.max(farthest, i + arr[i]);
            }

            l = r + 1;
            r = farthest;
            jumps = jumps + 1;
        }

        return jumps;
    }

    static int minJumps(int[] arr, int n) {
        // your code here
        if (!canJump(arr, n))
            return -1;
        return jump(arr, n);
    }

    public static void p2() {
        // Problem 2 : Leetcode 45 Jump Game II -
        // https://leetcode.com/problems/jump-game-ii/description/
        // Geeksforgeeks -
        // https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1

        int arr[] = { 1, 2, 0, 4, 1 };
        int n = 5;
        int j = minJumps(arr, n);
        System.out.println(j);
    }

    public static void main(String[] args) {
        // Day 21

        p1();

        p2();
    }
}