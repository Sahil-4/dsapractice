import java.util.HashSet;
import java.util.Set;

/**
 * Disjoint set data structure
 */
class DisjointSet {
    int[] parent;
    int[] size;

    DisjointSet(int N) {
        parent = new int[N];
        size = new int[N];

        for (int i = 0; i < N; i++) {
            size[i] = 1;
            parent[i] = i;
        }
    }

    int findParent(int node) {
        if (parent[node] != node) {
            parent[node] = findParent(parent[node]);
        }

        return parent[node];
    }

    void unionBySize(int u, int v) {
        int pu = findParent(u);
        int pv = findParent(v);

        if (pu == pv) {
            return;
        }

        int spu = size[pu];
        int spv = size[pv];

        if (spu < spv) {
            parent[pu] = pv;
            size[pv] += size[pu];
        } else {
            parent[pv] = pu;
            size[pu] += size[pv];
        }
    }

    int getSize(int node) {
        int parent = findParent(node);
        return size[parent];
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 14 of October

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 827. Making A Large Island -
        // https://leetcode.com/problems/making-a-large-island/
        // Geeksforgeeks -
        // https://www.geeksforgeeks.org/problems/making-a-large-island/1
        // Geeksforgeeks -
        // https://www.geeksforgeeks.org/problems/maximum-connected-group/1

        int[][] grid = {
                { 1, 1 },
                { 0, 1 }
        };

        int size = largestIsland(grid);
        System.out.println(size);
    }

    static int[] __DROWS = { -1, 0, 1, 0 };
    static int[] __DCOLS = { 0, -1, 0, 1 };

    static int getNodeNumber(int r, int c, int m) {
        return (r * m) + c;
    }

    static boolean isValidIndex(int r, int c, int m) {
        return ((r >= 0 && r < m) && (c >= 0 && c < m));
    }

    static int largestIsland(int[][] grid) {
        int __ROWS = grid.length;

        int N = __ROWS * __ROWS;

        DisjointSet ds = new DisjointSet(N);

        // step 1 - connect and make components
        for (int r = 0; r < __ROWS; r++) {
            for (int c = 0; c < __ROWS; c++) {
                // if 0 no need to make connections
                if (grid[r][c] == 0) {
                    continue;
                }

                // current node
                int nodeA = getNodeNumber(r, c, __ROWS);

                // connect all 4 directions
                for (int d = 0; d < 4; d++) {
                    int __row = __DROWS[d] + r;
                    int __col = __DCOLS[d] + c;

                    // skip invalid index
                    if (!isValidIndex(__row, __col, __ROWS)) {
                        continue;
                    }

                    // dont connect 0 - skip 0
                    if (grid[__row][__col] == 0) {
                        continue;
                    }

                    // adjacent node - to connect
                    int nodeB = getNodeNumber(__row, __col, __ROWS);
                    ds.unionBySize(nodeA, nodeB);
                }
            }
        }

        int largestIslandSize = 0;

        // step 2 - trying converting 0 to 1 and find largest island
        for (int r = 0; r < __ROWS; r++) {
            for (int c = 0; c < __ROWS; c++) {
                // skip 1s
                if (grid[r][c] == 1) {
                    continue;
                }

                // store components - parents
                Set<Integer> components = new HashSet<>();

                // add all 4 directions
                for (int d = 0; d < 4; d++) {
                    int __row = __DROWS[d] + r;
                    int __col = __DCOLS[d] + c;

                    // skip invalid index
                    if (!isValidIndex(__row, __col, __ROWS)) {
                        continue;
                    }

                    // skip 0
                    if (grid[__row][__col] == 0) {
                        continue;
                    }

                    // adding component parent
                    int node = getNodeNumber(__row, __col, __ROWS);
                    int parent = ds.findParent(node);
                    components.add(parent);
                }

                int __size = 0;
                for (Integer parent : components) {
                    __size += ds.getSize(parent);
                }

                largestIslandSize = Math.max(largestIslandSize, __size + 1);
            }
        }

        // step 3 - ensure case where all are 1s
        for (int node = 0; node < N; node++) {
            int parent = ds.findParent(node);
            int cSize = ds.getSize(parent);
            largestIslandSize = Math.max(largestIslandSize, cSize);
        }

        return largestIslandSize;

        // Complexity analysis
        // Time : O(N * 4 * 4ALPHA) + O(N * 4 * 4ALPHA) + O(N * 4ALPHA)
        // Space : O(2N) + O(4)
    }
}
