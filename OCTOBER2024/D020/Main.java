import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        // Day 20 of October

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Leetcode 802. Find Eventual Safe States -
        // https://leetcode.com/problems/find-eventual-safe-states/

        int[][] graph = { { 1, 2, 3, 4 }, { 1, 2 }, { 3, 4 }, { 0, 4 }, {} };

        List<Integer> n = eventualSafeNodes(graph);
        System.out.println(n.toString());
    }

    static int MARK = 100;

    static boolean dfs(int[][] graph, int node, int[] visited, int[] terminal) {
        if (visited[node] == MARK) {
            return terminal[node] == MARK;
        }

        visited[node] = MARK;

        for (int next : graph[node]) {
            boolean check = dfs(graph, next, visited, terminal);
            if (!check) {
                return false;
            }
        }

        terminal[node] = MARK;

        return true;
    }

    static List<Integer> eventualSafeNodes(int[][] graph) {
        int V = graph.length;
        int[] visited = new int[V];
        int[] terminal = new int[V];

        for (int i = 0; i < V; i++) {
            if (visited[i] != MARK) {
                dfs(graph, i, visited, terminal);
            }
        }

        List<Integer> t = new ArrayList<>();

        for (int i = 0; i < V; i++) {
            if (terminal[i] == MARK) {
                t.add(i);
            }
        }

        return t;

        // Complexity analysis
        // Time : O(V + E) + O(V)
        // Space : O(V) + O(V) + O(V) stack space
    }

    static void p2() {
        // Problem 2 : Geeksforgeeks Topological sort -
        // https://www.geeksforgeeks.org/problems/topological-sort/1

        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        // {{}, {3}, {3}, {}, {0,1}, {0,2}}
        adj.add(new ArrayList<>());
        adj.add(new ArrayList<>(Arrays.asList(3)));
        adj.add(new ArrayList<>(Arrays.asList(3)));
        adj.add(new ArrayList<>());
        adj.add(new ArrayList<>(Arrays.asList(0, 1)));
        adj.add(new ArrayList<>(Arrays.asList(0, 2)));

        ArrayList<Integer> sorted = topologicalSort(adj);
        ArrayList<Integer> sorted2 = kahns(adj);
        System.out.println(sorted.toString());
        System.out.println(sorted2.toString());
    }

    static void dfs(int node, ArrayList<ArrayList<Integer>> adj, int[] visited, Stack<Integer> stack) {
        visited[node] = MARK;

        for (int next : adj.get(node)) {
            if (visited[next] != MARK) {
                dfs(next, adj, visited, stack);
            }
        }

        stack.push(node);
    }

    // Function to return list containing vertices in Topological order.
    static ArrayList<Integer> topologicalSort(ArrayList<ArrayList<Integer>> adj) {
        // Your code here
        int V = adj.size();

        int visited[] = new int[V];

        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < V; i++) {
            if (visited[i] != MARK) {
                dfs(i, adj, visited, stack);
            }
        }

        ArrayList<Integer> ans = new ArrayList<>();

        while (!stack.isEmpty()) {
            ans.add(stack.pop());
        }

        return ans;

        // Complexity analysis
        // Time : O(V + E)
        // Space : O(V) + O(V)
    }

    static ArrayList<Integer> kahns(ArrayList<ArrayList<Integer>> adj) {
        int V = adj.size();
        int[] indegree = new int[V];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < V; i++) {
            for (int n : adj.get(i)) {
                indegree[n]++;
            }
        }

        for (int i = 0; i < V; i++) {
            if (indegree[i] == 0) {
                stack.push(i);
            }
        }

        ArrayList<Integer> out = new ArrayList<>();

        while (!stack.isEmpty()) {
            int top = stack.pop();

            out.add(top);

            for (int next : adj.get(top)) {
                indegree[next]--;

                if (indegree[next] == 0) {
                    stack.push(next);
                }
            }
        }

        return out;
        
        // Complexity analysis 
        // Time : O(V + E) + O(V) + O(V + E) 
        // Space : O(V) + O(v) 
    }
}