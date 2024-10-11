
/**
 * Disjoint set data structure
 */
class DisjointSet {
    int[] parent;
    int[] rank;
    int[] size;

    DisjointSet(int N) {
        parent = new int[N];
        rank = new int[N];
        size = new int[N];

        for (int i = 0; i < N; i++) {
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

    void unionByRank(int u, int v) {
        int pu = findParent(u);
        int pv = findParent(v);

        if (pu == pv) {
            return;
        }

        int rpu = rank[pu];
        int rpv = rank[pv];

        if (rpu < rpv) {
            parent[pu] = pv;
        } else if (rpu > rpv) {
            parent[pv] = pu;
        } else {
            parent[pv] = pu;
            rank[pu] = rank[pu] + 1;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 11 of October

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Geeksforgeeks Disjoint set (Union-Find) -
        // https://www.geeksforgeeks.org/problems/disjoint-set-union-find/1

        int[] Parent = { 0, 1, 2, 3, 4, 5 };

        System.out.println("parent of 1::" + find(Parent, 1));
        System.out.println("parent of 3::" + find(Parent, 3));
        unionSet(Parent, 3, 1);
        System.out.println("parent of 1::" + find(Parent, 1));
        System.out.println("parent of 3::" + find(Parent, 3));
    }

    static int find(int Parent[], int X) {
        // add code here.
        if (Parent[X] != X) {
            // Path compression
            Parent[X] = find(Parent, Parent[X]);
        }

        return Parent[X];
    }

    static void unionSet(int Parent[], int X, int Z) {
        // add code here.
        int rootX = find(Parent, X);
        int rootZ = find(Parent, Z);

        if (rootX != rootZ) {
            Parent[rootX] = rootZ; // join
        }
    }

    static void p2() {
        // Problem 2 : Leetcode 547. Number of Provinces -
        // https://leetcode.com/problems/number-of-provinces/description/
        // Geeksforgeeks -
        // https://www.geeksforgeeks.org/problems/number-of-provinces/1

        int[][] graph = {
                { 1, 1, 0 },
                { 1, 1, 0 },
                { 0, 0, 1 },
        };

        int compos = findCircleNum(graph);
        System.out.println(compos);
    }

    static int findCircleNum(int[][] graph) {
        // Using Disjoint Set

        int V = graph.length;

        DisjointSet ds = new DisjointSet(V);
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (graph[i][j] == 1) {
                    ds.unionByRank(i, j);
                }
            }
        }

        int components = 0;

        for (int i = 0; i < V; i++) {
            if (ds.findParent(i) == i) {
                components++;
            }
        }

        return components;
    }
}
