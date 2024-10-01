import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) {
        // Day 1 of October
        // Day 275 of 2024

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Leetcode 207. Course Schedule -
        // https://leetcode.com/problems/course-schedule/description/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/prerequisite-tasks/1

        int[][] prerequisites = { { 1, 0 } };
        int V = 2;

        boolean check = canFinish(V, prerequisites);
        System.out.println(check);
    }

    static boolean canFinish(int V, int[][] prerequisites) {
        // using topological sort

        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] prerequisite : prerequisites) {
            int course = prerequisite[0];
            int pre = prerequisite[1];
            adj.get(pre).add(course);
        }

        int indegree[] = new int[V];
        for (int i = 0; i < V; i++) {
            for (int e : adj.get(i)) {
                indegree[e]++;
            }
        }

        Queue<Integer> q = new LinkedList<>();
        for (int c = 0; c < V; c++) {
            if (indegree[c] == 0) {
                q.add(c);
            }
        }

        int idx = 0;

        while (!q.isEmpty()) {
            int c = q.remove();

            idx++;

            for (int e : adj.get(c)) {
                indegree[e]--;
                if (indegree[e] == 0)
                    q.add(e);
            }
        }

        return idx == V;
    }

    static void p2() {
        // Problem 2 : Leetcode 210. Course Schedule II -
        // https://leetcode.com/problems/course-schedule-ii/description/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/course-schedule/1

        int[][] prerequisites = { { 1, 0 } };
        int V = 2;

        int[] order = findOrder(V, prerequisites);
        System.out.println(Arrays.toString(order));
    }

    static int[] findOrder(int V, int[][] prerequisites) {
        // using topological sort

        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] prerequisite : prerequisites) {
            int course = prerequisite[0];
            int pre = prerequisite[1];
            adj.get(pre).add(course);
        }

        int indegree[] = new int[V];
        for (int i = 0; i < V; i++) {
            for (int e : adj.get(i)) {
                indegree[e]++;
            }
        }

        Queue<Integer> q = new LinkedList<>();
        for (int c = 0; c < V; c++) {
            if (indegree[c] == 0) {
                q.add(c);
            }
        }

        int[] order = new int[V];
        int idx = 0;

        while (!q.isEmpty()) {
            int c = q.remove();

            order[idx++] = c;

            for (int e : adj.get(c)) {
                indegree[e]--;
                if (indegree[e] == 0)
                    q.add(e);
            }
        }

        return idx == V ? order : new int[0];
    }
}
