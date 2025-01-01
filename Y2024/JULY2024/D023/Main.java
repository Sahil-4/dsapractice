import java.util.Arrays;

class Main {
    public static int findContentChildren(int[] childsGreed, int[] cookies) {
        Arrays.sort(childsGreed);
        Arrays.sort(cookies);

        int n = childsGreed.length, m = cookies.length;
        int p1 = 0, p2 = 0;

        while (p1 < n && p2 < m) {
            if (cookies[p2] >= childsGreed[p1])
                p1++;
            p2++;
        }

        return p1;

        // Complexity analysis
        // Time : O(n * log(n) + m * log(m) + max(n, m))
        // Space : O(1)
    }

    public static void p1() {
        // Problem 1 : Leetcode 455. Assign Cookies -
        // https://leetcode.com/problems/assign-cookies/description/
        // Geeksforgeeks - https://www.geeksforgeeks.org/problems/assign-cookies/0

        int[] childsGreed = { 1, 2, 3 };
        int[] cookies = { 1, 1 };

        int c = findContentChildren(childsGreed, cookies);
        System.out.println(c);
    }

    public static void main(String[] args) {
        // Day 23

        p1();
    }
}