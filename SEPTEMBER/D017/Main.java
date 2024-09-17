import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) {
        // Day 9 of Heaps

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 378. Kth Smallest Element in a Sorted Matrix -
        // https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/kth-element-in-matrix/1

        int[][] matrix = {
                { 2, 5, 13, 18 },
                { 5, 8, 17, 19 },
                { 8, 8, 17, 22 },
                { 13, 16, 22, 28 },
        };
        int k = 5;

        int e = kthSmallest(matrix, k);
        System.out.println(e);
    }

    static int smallerThen(int[][] matrix, int target) {
        int c = 0;
        int n = matrix.length;
        int i = n - 1;
        int j = 0;

        while (i >= 0 && j < n) {
            if (matrix[i][j] > target) i--;
            else { j++; c += i + 1; }
        }
        
        return c;
    }

    static int kthSmallest(int[][] matrix, int k) {
        /* 
            [ 1  5  9]
            [ 8  9 12]
            [10 11 13]
            [12 13 15] 
        */
        int n = matrix.length;
        int low = matrix[0][0];
        int high = matrix[n - 1][n - 1];

        while (low < high) {
            int mid = low + (high - low) / 2;

            int c = smallerThen(matrix, mid);
            if (c < k) low = mid + 1;
            else high = mid;
        }

        return low;

        // Complexity analysis 
        // Time : O(log(n^2)) + O(n) 
        // Space : O(1) 
    }

    static int kthSmallest_Solution1(int[][] matrix, int k) {
        /*
         * [ 1 5 9]
         * [ 8 9 12]
         * [10 11 13]
         * [12 13 15]
         */
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int[] rows : matrix) {
            for (int c : rows) {
                pq.add(c);
                if (pq.size() > k) pq.poll();
            }
        }

        return pq.poll();

        // Complexity analysis
        // Time : O(n * n * log(k))
        // Space : O(k)
    }
}
