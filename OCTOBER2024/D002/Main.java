import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        // Day 2 of October

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : GeeksForGeeks Topological sort -
        // https://www.geeksforgeeks.org/problems/topological-sort/1

        int V = 4;

        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        ArrayList<Integer> ls1 = new ArrayList<>();
        ls1.add(3);
        ls1.add(0);
        ArrayList<Integer> ls2 = new ArrayList<>();
        ls2.add(1);
        ls2.add(0);
        ArrayList<Integer> ls3 = new ArrayList<>();
        ls3.add(2);
        ls3.add(0);

        adj.add(ls1);
        adj.add(ls2);
        adj.add(ls3);

        int[] arr = topoSort(V, adj);
        System.out.println(Arrays.toString(arr));
    }

    static int MARK = 100;

    static void dfs(int current, ArrayList<ArrayList<Integer>> adj, int[] visited, Stack<Integer> stk) {
        visited[current] = MARK;

        for (int v : adj.get(current)) {
            if (visited[v] != MARK) {
                dfs(v, adj, visited, stk);
            }
        }

        stk.push(current);
    }

    // Function to return list containing vertices in Topological order.
    static int[] topoSort(int V, ArrayList<ArrayList<Integer>> adj) {
        // add your code here
        int[] visited = new int[V];
        Stack<Integer> stk = new Stack<>();

        for (int i = 0; i < V; i++) {
            if (visited[i] != MARK) {
                dfs(i, adj, visited, stk);
            }
        }

        int[] arr = new int[V];
        int i = 0;

        while (!stk.isEmpty()) {
            arr[i++] = stk.pop();
        }

        return arr;

        // Complexity analysis
        // Time : O(V) + O(E)
        // Space : O(V) + O(V)
    }

    static void p2() {
        // Problem 2 : Leetcode 802. Find Eventual Safe States -
        // https://leetcode.com/problems/find-eventual-safe-states/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/eventual-safe-states/1

        int[][] graph = { { 1, 2 }, { 2, 3 }, { 5 }, { 0 }, { 5 }, {}, {} };

        List<Integer> list = eventualSafeNodes(graph);
        System.out.println(list.toString());
    }

    static List<Integer> eventualSafeNodes(int[][] graph) {
        int V = graph.length;

        List<List<Integer>> revadj = new ArrayList<>();
        for (int i = 0; i < V; i++) {
            revadj.add(new ArrayList<>());
        }

        int[] indegree = new int[V];
        for (int i = 0; i < V; i++) {
            for (int n : graph[i]) {
                revadj.get(n).add(i);
                indegree[i]++;
            }
        }

        Queue<Integer> q = new LinkedList<>();
        List<Integer> list = new ArrayList<>();

        for (int i = 0; i < V; i++) {
            if (indegree[i] == 0) {
                q.add(i);
            }
        }

        while (!q.isEmpty()) {
            int n = q.remove();

            list.add(n);

            for (int c : revadj.get(n)) {
                indegree[c]--;
                if (indegree[c] == 0) {
                    q.add(c);
                }
            }
        }

        Collections.sort(list);

        return list;

        // Complexity analysis
        // Time : O(V) + O(V + E) + O(V) + O(V) + (V * log(V))
        // Space : O(V * E) + O(V) + O(V)
    }
}
