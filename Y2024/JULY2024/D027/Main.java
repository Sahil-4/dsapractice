import java.util.Arrays;

public class Main {
    static int solve(int bt[]) {
        // code here
        Arrays.sort(bt);

        int N = bt.length;
        int start_time = 0;
        int total_wt = 0;

        for (int i = 0; i < N; i++) {
            total_wt += start_time;
            start_time += bt[i];
        }

        return total_wt / N;
    }

    static void p1() {
        // Problem 1 : GeeksForGeeks Shortest Job first -
        // https://www.geeksforgeeks.org/problems/shortest-job-first/1

        int bt[] = { 1, 2, 3, 4 };
        int wt = solve(bt);
        System.out.println(wt);
    }

    public static int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (int a[], int b[]) -> a[1] - b[1]);

        int deleteCount = 0;

        int startTime = Integer.MIN_VALUE;
        for (int[] interval : intervals) {
            if (startTime <= interval[0]) {
                startTime = interval[1];
            } else {
                deleteCount++;
            }
        }

        return deleteCount;
    }

    static void p2() {
        // Problem 2 : Leetcode 435. Non-overlapping Intervals -
        // https://leetcode.com/problems/non-overlapping-intervals/description/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/non-overlapping-intervals/0

        int intervals[][] = { { 1, 2 }, { 2, 3 }, { 3, 4 }, { 1, 3 } };
        int d = eraseOverlapIntervals(intervals);
        System.out.println(d);
    }

    public static void main(String[] args) {
        // Day 27 - Day 7 of greedy

        p1();

        p2();
    }
}