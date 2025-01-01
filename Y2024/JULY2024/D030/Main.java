import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        List<int[]> arr = new ArrayList<>();
        int prev[] = intervals[0];

        for (int i = 1; i < intervals.length; i++) {
            int interval[] = intervals[i];

            if (prev[1] < interval[0]) {
                arr.add(prev);
                prev = interval;
            } else {
                prev[1] = Math.max(prev[1], interval[1]);
            }
        }
        arr.add(prev);

        return arr.toArray(int[][]::new);

        // Complexity analysis
        // Space : O(n), to store answer
        // Time : O(n)
    }

    static void p1() {
        // Problem 1 : Leetcode 56. Merge Intervals -
        // https://leetcode.com/problems/merge-intervals/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/overlapping-intervals--170633/1

        int[][] intervals = {};
        int[][] intervalsPost = merge(intervals);
        for (int[] interval : intervalsPost) {
            System.out.println(interval[0] + ", " + interval[1]);
        }
    }

    public static void main(String[] args) {
        // Day 30 - Day 10 of greedy 

        p1();
    }
}