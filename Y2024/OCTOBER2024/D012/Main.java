import java.util.Map;
import java.util.TreeMap;

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
}

public class Main {
    public static void main(String[] args) {
        // Day 12 of October

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Leetcode 1319. Number of Operations to Make Network Connected -
        // https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/
        // Geeksforgeeks -
        // https://www.geeksforgeeks.org/problems/minimize-connections/0

        int N = 4;
        int[][] connections = { { 0, 1 }, { 0, 2 }, { 1, 2 } };

        int e = makeConnected(N, connections);
        System.out.println(e);
    }

    static int makeConnected(int N, int[][] connections) {
        DisjointSet ds = new DisjointSet(N);

        int extraEdges = 0;

        for (int[] connection : connections) {
            int u = connection[0];
            int v = connection[1];

            if (ds.findParent(u) == ds.findParent(v)) {
                extraEdges++;
            } else {
                ds.unionBySize(u, v);
            }
        }

        int components = 0;
        for (int i = 0; i < N; i++) {
            if (ds.findParent(i) == i) {
                components++;
            }
        }

        int edgesNeeded = components - 1;

        return edgesNeeded <= extraEdges ? edgesNeeded : -1;

        // Complexity analysis
        // Time : O(E * 4ALPHA) + O(N * 4ALPHA)
        // Space : O(2N)
    }

    static void p2() {
        // Problem 2 : Leetcode 947. Most Stones Removed with Same Row or Column -
        // https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/
        // Geeksforgeeks -
        // https://www.geeksforgeeks.org/problems/maximum-stone-removal-1662179442/1

        int[][] stones = { { 0, 0 }, { 0, 1 }, { 1, 0 }, { 1, 2 }, { 2, 1 }, { 2, 2 } };
        int rs = removeStones(stones);
        System.out.println(rs);
    }

    static int removeStones(int[][] stones) {
        // using disjoint set

        int E = stones.length;

        int rowN = 0;
        int colN = 0;
        for (int[] stone : stones) {
            rowN = Math.max(rowN, stone[0]);
            colN = Math.max(colN, stone[1]);
        }

        int N = rowN + colN + 1;
        DisjointSet ds = new DisjointSet(N + 1);
        Map<Integer, Integer> map = new TreeMap<>();

        for (int[] stone : stones) {
            int r = stone[0];
            int c = stone[1] + rowN + 1;

            ds.unionBySize(r, c);

            map.put(r, 1);
            map.put(c, 1);
        }

        int components = 0;
        for (Map.Entry<Integer, Integer> e : map.entrySet()) {
            if (ds.findParent(e.getKey()) == e.getKey()) {
                components++;
            }
        }

        return E - components;

        // Complexity analysis
        // Time : O(E) + O(E * (4ALPHA + log(N))) + O(E * 4ALPHA)
        // Space : O(2N) + (N)
    }
}
