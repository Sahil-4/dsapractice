#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    bool detectCycle(int u, vector<vector<int>>& adj, vector<bool>& visited, vector<bool>& inrecurr) {
        visited[u] = true;
        inrecurr[u] = true;

        for (int v : adj[u]) {
            bool check = ((!visited[v] && detectCycle(v, adj, visited, inrecurr)) || (visited[v] && inrecurr[v]));
            if (check) return true;
        }

        inrecurr[u] = false;

        return false;
    }

public:
    bool canFinish(int N, vector<vector<int>>& prerequisites) {
        // simple - detect cycle in graph 

        // create adjacency list 
        // Ui -> { Vi1, Vi2, ... } 
        vector<vector<int>> adj(N);
        for (auto prerequisite : prerequisites) {
            int v = prerequisite[0], u = prerequisite[1];
            adj[u].push_back(v);
        }

        vector<bool> visited(N, false);
        vector<bool> inrecurr(N, false);

        // traverse greaph and look for cycle in path 
        for (int u = 0; u < N; u++) {
            bool check = !visited[u] && detectCycle(u, adj, visited, inrecurr);
            if (check) return false;
        }

        return true;

        // Complexity analysis 
        // Time : O(E) +  O(V + E) 
        // Space : O(V + E) + O(V) + O(V) 
    }
};

void p1() {
    // Problem 1 : Leetcode 207. Course Schedule - https://leetcode.com/problems/course-schedule/description/?envType=study-plan-v2&envId=top-interview-150 

    int N = 5;
    vector<vector<int>> prerequisites = { {0,1},{1,2},{1,3},{2,4},{3,4} };
    cout << Problem1().canFinish(N, prerequisites) << endl;
}

class Problem2 {
public:
    vector<int> findOrder(int N, vector<vector<int>>& prerequisites) {
        // using kahn's topological sort algo 

        vector<vector<int>> adj(N); // adjacency list 
        vector<int> indegree(N, 0); // indegree of nodes 

        for (auto prerequisite : prerequisites) {
            int v = prerequisite[0], u = prerequisite[1];
            adj[u].push_back(v);
            indegree[v]++;
        }

        vector<int> order; // store sorted vertices 
        queue<int> q; // queue for storing nodes while traversal 

        for (int u = 0; u < N; u++) {
            if (indegree[u] == 0) {
                q.push(u);
                order.push_back(u);
            }
        }

        while (!q.empty()) {
            int u = q.front(); q.pop();

            for (int v : adj[u]) {
                indegree[v]--;
                if (indegree[v] == 0) {
                    q.push(v);
                    order.push_back(v);
                }
            }
        }

        if (order.size() == N) return order;
        return {};

        // Complexity analysis 
        // Time : O(E) +  O(V) + O(V + E) 
        // Space : O(V + E) + O(V) + O(V) + O(E) 
    }
};

void p2() {
    // Problem 2 : Leetcode 210. Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/course-schedule/1 

    int N = 5;
    vector<vector<int>> prerequisites = { {0,1},{1,2},{1,3},{2,4},{3,4} };
    vector<int> order = Problem2().findOrder(N, prerequisites);
    for (int v : order) cout << v << " ";
    cout << endl;
}


int main() {
    // Day 29 of January 30 

    p1();

    p2();


    return 0;
}