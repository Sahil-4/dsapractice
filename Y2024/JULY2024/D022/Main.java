import java.util.Arrays;

class Main {
    public static int maxProduct(int[] nums) {
        int n = nums.length;

        if (n == 0)
            return 0;
        if (n == 1)
            return nums[0];

        Arrays.sort(nums);
        return (nums[n - 1] - 1) * (nums[n - 2] - 1);
        // return nums[n - 1] * nums[n - 2];
    }

    public static void p1() {
        // Problem 1 : Leetcode 1464. Maximum Product of Two Elements in an Array -
        // https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
        // Geeksforgeeks -
        // https://www.geeksforgeeks.org/problems/maximum-product-of-two-numbers2730/0

        int arr[] = {1,5,7,2};
        int prod = maxProduct(arr);
        System.out.println(prod);
    }

    public static void main(String[] args) {
        // Day 22

        p1();
    }
}