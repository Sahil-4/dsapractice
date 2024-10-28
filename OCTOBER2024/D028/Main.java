import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Disjoint set data structure
 */
class DisjointSet {
    int[] parent;
    int[] rank;
    int[] size;

    DisjointSet(int N) {
        parent = new int[N + 1];
        rank = new int[N + 1];
        size = new int[N + 1];

        for (int i = 0; i < N + 1; i++) {
            size[i] = 1;
            rank[i] = 0;
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
        // Day 28 of October

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Leetcode 2316. Count Unreachable Pairs of Nodes in an Undirected
        // Graph -
        // https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

        int N = 12;
        int[][] edges = {};

        long ps = countPairs(N, edges);
        System.out.println(ps);
    }

    static long countPairs(int N, int[][] edges) {
        // create components
        DisjointSet ds = new DisjointSet(N);
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            ds.unionBySize(u, v);
        }

        // get each component size
        List<Integer> componentSizes = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            if (ds.findParent(i) == i) {
                componentSizes.add(ds.size[i]);
            }
        }

        // count unreachable pairs
        long unreachablePairs = 0;
        long remainingNodes = N;
        for (int componentSize : componentSizes) {
            unreachablePairs += (componentSize * (remainingNodes - (long) componentSize));
            remainingNodes -= (long) componentSize;
        }

        return unreachablePairs;

        // Complexity analysis
        // Time : O(N) + O(E) + O(N) + O(N)
        // Space : O(3N) + O(N)
    }

    static void p2() {
        // Problem 2 : Geeksforgeeks Detect Cycle using DSU -
        // https://www.geeksforgeeks.org/problems/detect-cycle-using-dsu/1

        int V = 6;
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        adj.add(new ArrayList<>(Arrays.asList(5, 5)));
        adj.add(new ArrayList<>(Arrays.asList(0, 2)));
        adj.add(new ArrayList<>(Arrays.asList(0, 3)));
        adj.add(new ArrayList<>(Arrays.asList(0, 4)));
        adj.add(new ArrayList<>(Arrays.asList(1, 3)));
        adj.add(new ArrayList<>(Arrays.asList(2, 4)));

        int cycle = detectCycle(V, adj);
        System.out.println(cycle);
    }

    // Function to detect cycle using DSU in an undirected graph.
    static int detectCycle(int V, ArrayList<ArrayList<Integer>> adj) {
        // Code here
        DisjointSet ds = new DisjointSet(V);

        for (int u = 0; u < V; u++) {
            for (int v : adj.get(u)) {
                if (v >= u) {
                    continue;
                }

                int pu = ds.findParent(u);
                int pv = ds.findParent(v);

                if (pu != pv) {
                    ds.unionBySize(u, v);
                } else {
                    return 1;
                }
            }
        }

        return 0;

        // Complexity analysis
        // Time : O(V) + O(V * 4ALPHA)
        // Space : O(3V)
    }
}
