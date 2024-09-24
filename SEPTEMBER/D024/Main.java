import java.util.LinkedList;
import java.util.Queue;

class Index2D {
    int i;
    int j;

    Index2D(int i, int j) {
        this.i = i;
        this.j = j;
    }
}

class Pair {
    Index2D index;
    int time;

    Pair(Index2D i, int t) {
        this.index = i;
        this.time = t;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 24

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Leetcode 994. Rotting Oranges -
        // https://leetcode.com/problems/rotting-oranges/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/rotten-oranges2536/1

        int[][] grid = {
                { 2, 1, 1 },
                { 1, 1, 0 },
                { 0, 1, 1 },
        };
        int t = orangesRotting(grid);
        System.out.println(t);
    }

    static void rot(Queue<Pair> rottenOranges, Index2D index, int t, int[][] visited, int[][] grid, int n, int m) {
        int[] rows = { 1, 0, -1, 0 };
        int[] cols = { 0, 1, 0, -1 };

        for (int a = 0; a < 4; a++) {
            int i = index.i + rows[a];
            int j = index.j + cols[a];

            // valid index + not visited + fresh orange
            if ((i >= 0 && i < n && j >= 0 && j < m) && (visited[i][j] == 0) && (grid[i][j] == 1)) {
                visited[i][j] = 2;
                rottenOranges.offer(new Pair(new Index2D(i, j), t + 1));
            }
        }
    }

    static int orangesRotting(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;

        // for visited cells
        int[][] visited = new int[n][m];

        // find oranges that are rotten
        Queue<Pair> rottenOranges = new LinkedList<>();
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 2) {
                    visited[i][j] = 2;
                    rottenOranges.offer(new Pair(new Index2D(i, j), 0));
                }
            }
        }

        // holds time (output)
        int time = 0;

        // rot all neighbour oranges
        while (!rottenOranges.isEmpty()) {
            Index2D index = rottenOranges.peek().index;
            int t = rottenOranges.poll().time;

            time = Math.max(time, t);

            rot(rottenOranges, index, t, visited, grid, n, m);
        }

        // lastly check whether re able to rot all oranges
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // was a fresh orange but not rotten
                if (visited[i][j] != 2 && grid[i][j] == 1) {
                    return -1;
                }
            }
        }

        return time;

        // Complexity analysis
        // Time : O(n * m) + O(n * m) + O(n * m)
        // Space : O(2 * n * m)
    }

    static void p2() {
        // Problem 2 : Leetcode 733. Flood Fill -
        // https://leetcode.com/problems/flood-fill/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/flood-fill-algorithm1856/1

        int[][] image = {
            { 2, 1, 1 },
            { 1, 1, 0 },
            { 0, 1, 1 },
        };
        int sr = 1;
        int sc = 1;
        int color = 2;

        int[][] newImage = floodFill(image, sr, sc, color);
        for (int[] arr : newImage) {
            for (int p : arr) {
                System.out.print(p);
            }
            System.out.println("");
        }
    }

    static void flood(Queue<Index2D> queue, int[][] newImage, int[][] image, int[][] visited, Index2D index, int n, int m, int color) {
        int[] rows = { 1, 0, -1, 0 };
        int[] cols = { 0, 1, 0, -1 };

        for (int a = 0; a < 4; a++) {
            int i = index.i;
            int j = index.j;

            int ni = i + rows[a];
            int nj = j + cols[a];

            // valid index && not visited && same color
            if ((ni >= 0 && ni < n && nj >= 0 && nj < m) && (visited[ni][nj] != 1) && (image[i][j] == image[ni][nj])) {
                newImage[ni][nj] = color;
                visited[ni][nj] = 1;
                queue.add(new Index2D(ni, nj));
            }
        }
    }

    static int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int n = image.length;
        int m = image[0].length;

        int[][] newImage = new int[n][m];
        int[][] visited = new int[n][m];
        for (int i = 0; i < n; i++) {
            System.arraycopy(image[i], 0, newImage[i], 0, m);
        }

        Queue<Index2D> queue = new LinkedList<>();
        queue.offer(new Index2D(sr, sc));
        newImage[sr][sc] = color;
        visited[sr][sc] = 1;

        while (!queue.isEmpty()) {
            flood(queue, newImage, image, visited, queue.poll(), n, m, color);
        }

        return newImage;

        // Complexity analysis
        // Time : O(n * m) + O(n * m)
        // Space : O(n * m) + O(n * m) + O(n * m)
    }
}