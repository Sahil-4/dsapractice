import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Set;
import java.util.TreeMap;

class Pair {
    String variable;
    double value;

    Pair(String var, double val) {
        variable = var;
        value = val;
    }
}

class Pair2 {
    int cost;
    int node;

    Pair2(int c, int n) {
        cost = c;
        node = n;
    }
}

class CustomComparator implements Comparator<Pair2> {
    @Override
    public int compare(Pair2 p1, Pair2 p2) {
        if (p1.cost != p2.cost) {
            return p1.cost - p2.cost;
        }

        return p1.node - p2.node;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 6 of October

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Leetcode 399. Evaluate Division -
        // https://leetcode.com/problems/evaluate-division/

        double[] values = {};
        List<List<String>> equations = new ArrayList<>();
        List<List<String>> queries = new ArrayList<>();

        double[] answers = calcEquation(equations, values, queries);
        System.out.println(Arrays.toString(answers));
    }

    static void dfs(TreeMap<String, List<Pair>> adj, String src, String dest, Set<String> visited, double[] _prod_ans) {
        if (src.equals(dest)) {
            _prod_ans[1] = _prod_ans[0];
            return;
        }
        if (visited.contains(src)) {
            return;
        }

        visited.add(src);

        for (Pair p : adj.get(src)) {
            String nextSrc = p.variable;
            double cost = p.value;

            _prod_ans[0] *= cost;
            dfs(adj, nextSrc, dest, visited, _prod_ans);
            _prod_ans[0] /= cost;
        }
    }

    static double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        int eSize = equations.size();
        TreeMap<String, List<Pair>> adj = new TreeMap<>();
        for (int i = 0; i < eSize; i++) {
            String e1 = equations.get(i).get(0);
            String e2 = equations.get(i).get(1);

            double val = values[i];

            if (!adj.containsKey(e1)) {
                adj.put(e1, new ArrayList<>());
            }
            if (!adj.containsKey(e2)) {
                adj.put(e2, new ArrayList<>());
            }

            adj.get(e1).add(new Pair(e2, val));
            adj.get(e2).add(new Pair(e1, 1.0 / val));
        }

        int qSize = queries.size();
        double[] answers = new double[qSize];
        for (int i = 0; i < qSize; i++) {
            String src = queries.get(i).get(0);
            String dest = queries.get(i).get(1);

            Set<String> visited = new HashSet<>();
            double[] _prod_ans = new double[2];
            _prod_ans[0] = 1.0;
            _prod_ans[1] = -1.0;

            if (adj.containsKey(src)) {
                dfs(adj, src, dest, visited, _prod_ans);
            }

            answers[i] = _prod_ans[1];
        }

        return answers;

        // Complexity analysis
        // Time : O(n) + O(2m)
        // Space : O(2n)
        // n = equations.size()
        // m = queries.size()
    }

    static void p2() {
        // Problem 2 : GeeksForGeeks Minimum Spanning Tree -
        // https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1

        int V = 0;
        int E = 0;
        List<List<int[]>> adj = new ArrayList<>();
        int mst = spanningTree(V, E, adj);
        System.out.println(mst);
    }

    static int spanningTree(int V, int E, List<List<int[]>> adj) {
        // Code Here.
        int mstCost = 0;

        boolean[] visited = new boolean[V];

        PriorityQueue<Pair2> pq = new PriorityQueue<>(new CustomComparator());
        pq.add(new Pair2(0, 0));

        while (!pq.isEmpty()) {
            Pair2 top = pq.remove();

            int cost = top.cost;
            int node = top.node;

            if (visited[node])
                continue;

            visited[node] = true;

            mstCost += cost;

            for (int[] list : adj.get(node)) {
                int adjNode = list[0];
                int edgeCost = list[1];

                if (!visited[adjNode]) {
                    pq.add(new Pair2(edgeCost, adjNode));
                }
            }
        }

        return mstCost;

        // Complexity analysis
        // Time : O(E * Log(E)) + O(2E)
        // Space : O(V) + O(2E)
    }
}
