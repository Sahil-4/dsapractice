import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // Day 10 of October

        p1();

        p2();

        p3();
    }

    static void p1() {
        // Problem 1 : Geeksforgeeks Distance from the Source (Bellman-Ford Algorithm) -
        // https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1

        int V = 2;
        int source = 0;
        ArrayList<ArrayList<Integer>> edges = new ArrayList<>();
        ArrayList<Integer> e1 = new ArrayList<>();
        e1.add(0);
        e1.add(1);
        e1.add(9);
        edges.add(e1);

        int[] distances = bellman_ford(V, edges, source);

        System.out.println(Arrays.toString(distances));
    }

    static int MAXD = (int) 1e8;

    static int[] bellman_ford(int V, ArrayList<ArrayList<Integer>> edges, int source) {
        // Write your code here
        // V : number of vertices
        // source
        // edges : { {u, v, w} }

        // distance array
        int[] distances = new int[V];

        for (int i = 0; i < V; i++) {
            distances[i] = MAXD;
        }

        // distance from source to source node
        distances[source] = 0;

        // relaxation - N - 1
        for (int i = 1; i < V; i++) {
            for (ArrayList<Integer> edge : edges) {
                int u = edge.get(0);
                int v = edge.get(1);
                int w = edge.get(2);

                if (distances[u] != MAXD && distances[u] + w < distances[v]) {
                    distances[v] = distances[u] + w;
                }
            }
        }

        // relaxation - Nth
        for (ArrayList<Integer> edge : edges) {
            int u = edge.get(0);
            int v = edge.get(1);
            int w = edge.get(2);

            if (distances[u] != MAXD && distances[u] + w < distances[v]) {
                int[] temp = new int[1];
                temp[0] = -1;
                return temp;
            }
        }

        return distances;

        // Complexity analysis
        // Time : O(V) + O(V * N) + O(N)
        // Space : O(1)
    }

    static void p2() {
        // Problem 2 : GeeksForGeeks Floyd Warshall -
        // https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1

        int[][] matrix = {};

        shortest_distance(matrix);

        for (int[] mat : matrix) {
            System.out.println(Arrays.toString(mat));
        }
    }

    static void shortest_distance(int[][] matrix) {
        // Code here
        int V = matrix.length;

        // init
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (matrix[i][j] == -1) {
                    matrix[i][j] = MAXD;
                }
                if (i == j) {
                    matrix[i][j] = 0;
                }
            }
        }

        // floyd
        for (int mid = 0; mid < V; mid++) {
            for (int i = 0; i < V; i++) {
                for (int j = 0; j < V; j++) {
                    matrix[i][j] = Math.min(matrix[i][j], matrix[i][mid] + matrix[mid][j]);
                }
            }
        }

        // for negative weights cycles
        for (int i = 0; i < V; i++) {
            if (matrix[i][i] < 0) {
                // negative cycle
            }
        }

        // un reachable vertices
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (matrix[i][j] == MAXD) {
                    matrix[i][j] = -1;
                }
            }
        }

        // Complexity analysis
        // Time : O(V * V * V)
        // Space : O(V * V)
    }

    static void p3() {
        // Problem 3 : Leetcode 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance -
        // https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/1

        int V = 5;
        int distanceThreshold = 5;
        int[][] edges = {};

        int city = findTheCity(V, edges, distanceThreshold);
        System.out.println(city);
    }

    static int findTheCity(int V, int[][] edges, int distanceThreshold) {
        int[][] matrix = new int[V][V];

        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                matrix[i][j] = -1;
            }
        }

        for (int[] edge : edges) {
            int cityA = edge[0];
            int cityB = edge[1];
            int weight = edge[2];

            matrix[cityA][cityB] = weight;
            matrix[cityB][cityA] = weight;
        }

        for (int i = 0; i < V; i++) {
            matrix[i][i] = 0;
        }

        shortest_distance(matrix);

        int neighbours = V;
        int city = -1;

        for (int i = 0; i < V; i++) {
            int count = 0;

            for (int j = 0; j < V; j++) {
                if (matrix[i][j] != -1 && matrix[i][j] <= distanceThreshold) {
                    count++;
                }
            }

            if (count <= neighbours) {
                neighbours = count;
                city = i;
            }
        }

        return city;
    }
}
