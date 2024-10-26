import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

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

class Edge {
    int weight;
    int source;
    int destination;

    Edge(int w, int s, int d) {
        this.weight = w;
        this.source = s;
        this.destination = d;
    }
}

class EdgeComparator implements Comparator<Edge> {
    @Override
    public int compare(Edge e1, Edge e2) {
        if (e1.weight != e2.weight) {
            return e1.weight - e2.weight;
        } else if (e1.source != e2.source) {
            return e1.source - e2.source;
        }
        return e1.destination - e2.destination;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 26 of October

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Geeksforgeeks Minimum Spanning Tree -
        // https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1

        int V = 0;
        int E = 0;
        List<List<int[]>> adj = new ArrayList<>();

        int mstSum = spanningTree(V, E, adj);
        System.out.println(mstSum);
    }

    static int spanningTree(int V, int E, List<List<int[]>> adj) {
        // Code Here.

        // ---- kruskal's ----
        // sort the edges according to their weight
        // initially all vertices will be independent -- in disjoint set
        // all vertices will be parent of themselves
        // pick edges one by one check u, and v of edge
        // if they are in same component i.e. having same ultimate parent then discard
        // this edge
        // else add this edge in MST and and add u and v into same component

        PriorityQueue<Edge> pq = new PriorityQueue<>(new EdgeComparator());
        for (int src = 0; src < V; src++) {
            for (int[] edge : adj.get(src)) {
                int dest = edge[0];
                int weight = edge[1];
                pq.add(new Edge(weight, src, dest));
            }
        }

        int mstSum = 0;
        List<Edge> mst = new ArrayList<>();

        DisjointSet ds = new DisjointSet(V);

        while (!pq.isEmpty()) {
            Edge top = pq.remove();

            int w = top.weight;
            int u = top.source;
            int v = top.destination;

            if (ds.findParent(u) != ds.findParent(v)) {
                mstSum += w;
                mst.add(top);
                ds.unionBySize(u, v);
            }
        }

        return mstSum;

        // Complexity analysis
        // Time : O(E) + O(V) + O(E * (log(E) + 4ALPHA))
        // Space : O(E) + O(3V)
    }

    static void p2() {
        // Problem 2 : Leetcode 1319. Number of Operations to Make Network Connected -
        // https://leetcode.com/problems/number-of-operations-to-make-network-connected/

        int N = 6;
        int[][] connections = { { 0, 1 }, { 0, 2 }, { 0, 3 }, { 1, 2 }, { 1, 3 } };

        int ecs = makeConnected(N, connections);
        System.out.println(ecs);
    }

    static int makeConnected(int N, int[][] connections) {
        DisjointSet ds = new DisjointSet(N);

        int extraCables = 0;

        // check how many computers we can connect and save cables by not adding
        // redundant cables
        for (int[] conn : connections) {
            int u = conn[0];
            int v = conn[1];

            if (ds.findParent(u) == ds.findParent(v)) {
                extraCables++;
            } else {
                ds.unionBySize(u, v);
            }
        }

        // check how many computers are not connected and can we connect them by using
        // extra cables
        int networks = 0;
        for (int i = 0; i < N; i++) {
            if (ds.findParent(i) == i) {
                networks++;
            }
        }

        int notConnected = networks - 1;
        if (notConnected > extraCables) {
            return -1;
        }

        return notConnected;

        // Complexity analysis
        // Time : O(N) + O(E) + O(N * 4ALPHA)
        // Space : O(3N)
    }
}
