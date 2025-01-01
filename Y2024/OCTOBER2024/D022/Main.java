
import java.util.Comparator;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

class CustomSort implements Comparator<int[]> {
    @Override
    public int compare(int[] a1, int[] a2) {
        for (int i = 0; i < 3; i++) {
            if (a1[i] != a2[i]) {
                return a1[i] - a2[i];
            }
        }
        return 0;
    }
}

class Pair {
    int result;
    int steps;

    Pair(int r, int s) {
        this.result = r;
        this.steps = s;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 22 of October

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Leetcode 1631. Path With Minimum Effort -
        // https://leetcode.com/problems/path-with-minimum-effort/

        int[][] heights = { { 8, 3, 2, 5, 2, 10, 7, 1, 8, 9 },
                { 1, 4, 9, 1, 10, 2, 4, 10, 3, 5 },
                { 4, 10, 10, 3, 6, 1, 3, 9, 8, 8 },
                { 4, 4, 6, 10, 10, 10, 2, 10, 8, 8 },
                { 9, 10, 2, 4, 1, 2, 2, 6, 5, 7 },
                { 2, 9, 2, 6, 1, 4, 7, 6, 10, 9 },
                { 8, 8, 2, 10, 8, 2, 3, 9, 5, 3 },
                { 2, 10, 9, 3, 5, 1, 7, 4, 5, 6 },
                { 2, 3, 9, 2, 5, 10, 2, 7, 1, 8 },
                { 9, 10, 4, 10, 7, 4, 9, 3, 1, 6 } };

        int minEff = minimumEffortPath(heights);
        System.out.println(minEff);
    }

    static int MAXE = (int) 1e9;

    static int[] DROWS = { -1, 0, +1, 0 };
    static int[] DCOLS = { 0, -1, 0, +1 };

    static boolean isValidIndex(int r, int c, int rs, int cs) {
        return (r >= 0 && r < rs) && (c >= 0 && c < cs);
    }

    static int bfs(int[][] heights) {
        int rows = heights.length;
        int cols = heights[0].length;

        int[][] result = new int[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result[i][j] = MAXE;
            }
        }

        // { cost, row, col }
        PriorityQueue<int[]> pq = new PriorityQueue<>(new CustomSort());

        // start - effort to reach to source
        result[0][0] = 0;
        pq.add(new int[] { 0, 0, 0 });

        while (!pq.isEmpty()) {
            int[] top = pq.remove();

            int eff = top[0];
            int r = top[1];
            int c = top[2];

            for (int i = 0; i < 4; i++) {
                int nrow = r + DROWS[i];
                int ncol = c + DCOLS[i];

                if (!isValidIndex(nrow, ncol, rows, cols)) {
                    continue;
                }

                int aeff = Math.abs(heights[r][c] - heights[nrow][ncol]);
                int neff = Math.max(eff, aeff);

                if (result[nrow][ncol] <= neff) {
                    continue;
                }

                result[nrow][ncol] = neff;
                pq.add(new int[] { neff, nrow, ncol });
            }
        }

        return result[rows - 1][cols - 1];
    }

    static int minimumEffortPath(int[][] heights) {
        return bfs(heights);
    }

    static void p2() {
        // Problem 2 : Geeksforgeeks Minimum Multiplications to reach End -
        // https://www.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1

        int[] arr = { 20, 14, 1, 4, 20 };
        int start = 8;
        int end = 4288;
        int steps = minimumMultiplications(arr, start, end);
        System.out.println(steps);
    }

    static int MODO = (int) 100000;

    static int minimumMultiplications(int[] arr, int start, int end) {
        // Your code here
        if (start == end) {
            return 0;
        }

        int n = arr.length;

        int[] steps = new int[MODO];
        for (int i = 0; i < MODO; i++) {
            steps[i] = MAXE;
        }

        Queue<Pair> que = new LinkedList<>();

        que.add(new Pair(start, 0));
        steps[start] = 0;

        while (!que.isEmpty()) {
            Pair top = que.remove();

            int cres = top.result;
            int cstp = top.steps;

            for (int i = 0; i < n; i++) {
                if (arr[i] == 0 || arr[i] == 1) {
                    continue;
                }

                int nres = (cres * arr[i]) % MODO;
                int nstp = cstp + 1;

                if (steps[nres] <= nstp) {
                    continue;
                }
                if (nres == end) {
                    return nstp;
                }

                steps[nres] = nstp;
                que.add(new Pair(nres, nstp));
            }
        }

        return -1;
    }
}
