import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
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

class EquationComparator implements Comparator<String> {
    @Override
    public int compare(String e1, String e2) {
        String opr1 = e1.substring(1, 3);
        String opr2 = e2.substring(1, 3);

        if (opr1.equals(opr2)) {
            return 0;
        }

        if (opr1.equals("==")) {
            return -1;
        }

        return 1;
    }
}

class ArrayComparator implements Comparator<int[]> {
    @Override
    public int compare(int[] a, int[] b) {
        for (int i = 0; i < 2; i++) {
            if (a[i] != b[i]) {
                return a[i] - b[i];
            }
        }
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 30 of October

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Leetcode 990. Satisfiability of Equality Equations -
        // https://leetcode.com/problems/satisfiability-of-equality-equations/

        String[] equations = { "a==b", "b!=a" };
        boolean check = equationsPossible(equations);
        System.out.println(check);
    }

    static boolean equationsPossible(String[] equations) {
        Arrays.sort(equations, new EquationComparator());

        Map<Character, Integer> variables = new HashMap<>();
        int counter = 0;

        for (String eq : equations) {
            char v1 = eq.charAt(0);
            char v2 = eq.charAt(3);

            if (!variables.containsKey(v1)) {
                variables.put(v1, counter++);
            }
            if (!variables.containsKey(v2)) {
                variables.put(v2, counter++);
            }
        }

        DisjointSet ds = new DisjointSet(counter);

        for (String eq : equations) {
            char v1 = eq.charAt(0);
            char v2 = eq.charAt(3);

            int vi1 = variables.get(v1);
            int vi2 = variables.get(v2);

            String opr = eq.substring(1, 3);

            if (opr.equals("==")) {
                ds.unionBySize(vi1, vi2);
            } else {
                int pv1 = ds.findParent(vi1);
                int pv2 = ds.findParent(vi2);

                if (pv1 == pv2) {
                    return false;
                }
            }
        }

        return true;

        // Complexity analysis
        // Time : O(N * LOG(N)) + O(N) + O(N) + O(N * 4ALPHA)
        // Space : O(2N) + O(3 * 2N)
    }

    static void p2() {
        // Problem 2 : Geeksforgeeks Shortest Path in Weighted undirected graph -
        // https://www.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1

        int N = 5;
        int m = 23;
        int edges[][] = {};
        List<Integer> path = shortestPath(N, m, edges);
        System.out.println(path);
    }

    static int MAXD = (int) 1e9;

    static List<Integer> shortestPath(int N, int m, int edges[][]) {
        // Code Here.

        // create adjacency list
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];

            adj.get(u).add(new int[] { v, w });
            adj.get(v).add(new int[] { u, w });
        }

        // perform dijkstra
        PriorityQueue<int[]> pq = new PriorityQueue<>(new ArrayComparator());

        int[] distances = new int[N + 1];
        int[] parent = new int[N + 1];

        for (int i = 0; i <= N; i++) {
            distances[i] = MAXD;
            parent[i] = i;
        }

        distances[1] = 0;

        // { cost, node }
        pq.add(new int[] { 0, 1 });

        while (!pq.isEmpty()) {
            int[] top = pq.remove();

            int cost = top[0];
            int node = top[1];

            for (int[] next : adj.get(node)) {
                int nnode = next[0];
                int ncost = next[1] + cost;

                if (distances[nnode] > ncost) {
                    distances[nnode] = ncost;
                    parent[nnode] = node;
                    pq.add(new int[] { ncost, nnode });
                }
            }
        }

        if (distances[N] == MAXD) {
            return new ArrayList<>(Arrays.asList(-1));
        }

        List<Integer> path = new ArrayList<>();
        int c = N;
        while (parent[c] != c) {
            path.add(0, c);
            c = parent[c];
        }
        path.add(0, 1);
        path.add(0, distances[N]);

        return path;
    }
}
