
import java.util.Comparator;
import java.util.PriorityQueue;

class Index2D {
    int row;
    int col;

    Index2D(int r, int c) {
        this.row = r;
        this.col = c;
    }
}

class Pair {
    int cost;
    Index2D index;

    Pair(int c, Index2D i) {
        this.cost = c;
        this.index = i;
    }
}

class PairComparator implements Comparator<Pair> {
    @Override
    public int compare(Pair p1, Pair p2) {
        if (p1.cost != p2.cost) {
            return p1.cost - p2.cost;
        }
        if (p1.index.row != p2.index.row) {
            return p1.index.row - p2.index.row;
        }
        return p1.index.col - p2.index.col;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 7 of October

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 1631. Path With Minimum Effort -
        // https://leetcode.com/problems/path-with-minimum-effort/description/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/path-with-minimum-effort/1

        int[][] heights = {
                { 1, 2, 1, 1, 1 },
                { 1, 2, 1, 2, 1 },
                { 1, 2, 1, 2, 1 },
                { 1, 2, 1, 2, 1 },
                { 1, 1, 1, 2, 1 }
        };

        int eff = minimumEffortPath(heights);
        System.out.println(eff);
    }

    static int MAXIMUM = (int) 1e9;

    static int[] DROWS = { -1, 0, 0, +1 };
    static int[] DCOLS = { 0, -1, +1, 0 };

    static boolean isValidIndex(int r, int c, int n, int m) {
        return ((r >= 0 && r < n) && (c >= 0 && c < m));
    }

    static int minimumEffortPath(int[][] heights) {
        // dijkstra

        int ROWS = heights.length;
        int COLS = heights[0].length;

        int[][] result = new int[ROWS][COLS];
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                result[r][c] = MAXIMUM;
            }
        }

        PriorityQueue<Pair> pq = new PriorityQueue<>(new PairComparator());

        // update cost to reach at Index [0][0]
        result[0][0] = 0;
        pq.add(new Pair(0, new Index2D(0, 0)));

        while (!pq.isEmpty()) {
            Pair top = pq.remove();

            int cost = top.cost;
            int row = top.index.row;
            int col = top.index.col;

            for (int i = 0; i < 4; i++) {
                int nrow = row + DROWS[i];
                int ncol = col + DCOLS[i];

                if (isValidIndex(nrow, ncol, ROWS, COLS)) {
                    int absCost = Math.abs(heights[row][col] - heights[nrow][ncol]);
                    int maxCost = Math.max(cost, absCost);

                    if (result[nrow][ncol] > maxCost) {
                        result[nrow][ncol] = maxCost;
                        pq.add(new Pair(maxCost, new Index2D(nrow, ncol)));
                    }
                }
            }
        }

        return result[ROWS - 1][COLS - 1];

        // Complexity analysis
        // Time : O(ROWS * COLS) + O(log(E)), E = elements in priority queue
        // Time : O(ROWS * COLS) + O(E)
    }
}
