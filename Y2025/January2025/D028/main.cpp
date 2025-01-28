#include <bits/stdc++.h>

using namespace std;


class DisjointSet {
    int* parent;
    int* rank;
    int* size;

public:
    DisjointSet(int N) {
        parent = new int[N + 1];
        rank = new int[N + 1];
        size = new int[N + 1];

        for (int i = 0; i <= N; i++) {
            parent[i] = i;
            rank[i] = 1;
            size[i] = 1;
        }
    }

    int getParent(int u) {
        if (parent[u] == u) return u;
        return parent[u] = getParent(parent[parent[u]]);
    }

    void unionBySize(int u, int v) {
        int uparent = getParent(u);
        int vparent = getParent(v);

        if (uparent == vparent) return;

        int usize = size[uparent];
        int vsize = size[vparent];

        if (usize < vsize) {
            parent[uparent] = vparent;
            size[vparent] += size[uparent];
        }
        else {
            parent[vparent] = uparent;
            size[uparent] += size[vparent];
        }
    }

    void unionByRank(int u, int v) {
        int uparent = getParent(u);
        int vparent = getParent(v);

        if (uparent == vparent) return;

        int uparentrank = rank[uparent];
        int vparentrank = rank[vparent];

        if (uparentrank < vparentrank) {
            parent[uparent] = vparent;
        }
        else if (uparentrank > vparentrank) {
            parent[vparent] = uparent;
        }
        else {
            parent[uparent] = vparent;
            rank[vparent] = rank[vparent] + 1;
        }
    }

    int getSize(int u) {
        return size[u];
    }

    ~DisjointSet() {
        delete[] this->parent;
        delete[] this->rank;
        delete[] this->size;
        delete this;
    }
};

class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

class Problem1 {
    Node* cloneGraph(Node* node, unordered_map<Node*, Node*>& nodesMap) {
        if (node == nullptr) return nullptr;

        Node* nnode = new Node(node->val);
        nodesMap.insert({ node, nnode });

        for (Node* neighbor : node->neighbors) {
            if (nodesMap.find(neighbor) != nodesMap.end()) {
                nnode->neighbors.push_back(nodesMap[neighbor]);
            }
            else {
                nnode->neighbors.push_back(cloneGraph(neighbor, nodesMap));
            }
        }

        return nnode;

        // Complexity analysis 
        // Time : O(V + E) 
        // Space : O(V) + O(2V) 
    }

public:
    Node* cloneGraph(Node* node) {
        unordered_map<Node*, Node*> nodesMap;
        return cloneGraph(node, nodesMap);
    }
};

void p1() {
    // Problem 1 : Leetcode 133. Clone Graph - https://leetcode.com/problems/clone-graph/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/clone-graph/1 

    Node* node1, * node2;
    node1 = new Node(1, { node2 });
    node2 = new Node(2, { node1 });

    Node* cnode = Problem1().cloneGraph(node1);
}

class Problem2 {
    double resolveQuery(string qu, string qv, unordered_map<string, vector<pair<string, double>>>& adj, unordered_set<string>& visited) {
        if (qu == qv) return 1.0;
        if (visited.find(qu) != visited.end()) return -1.0;

        visited.insert(qu);

        for (auto neighbour : adj[qu]) {
            string nqu = neighbour.first;
            double v = neighbour.second;

            double nv = resolveQuery(nqu, qv, adj, visited);
            if (nv != -1.0) return v * nv;
        }

        return -1.0;
    }

public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        int N = equations.size();

        // adjacency list
        // "u" -> [("v", Double(A/B))]
        unordered_map<string, vector<pair<string, double>>> adj;
        for (int i = 0; i < N; i++) {
            string u = equations[i][0], v = equations[i][1];
            double UV = values[i];
            adj[u].push_back({ v, UV });
            adj[v].push_back({ u, 1.0 / UV });
        }

        vector<double> result;

        int M = queries.size();
        for (vector<string> query : queries) {
            string qu = query[0], qv = query[1];

            double ans = -1.0;

            if (adj.find(qu) != adj.end() && adj.find(qv) != adj.end()) {
                unordered_set<string> visited;
                ans = resolveQuery(qu, qv, adj, visited);
            }

            result.push_back(ans);
        }

        return result;

        // Complexity analysis 
        // Time : O(N) + O(M + V) 
        // Space : O(V) + O(V) + O(V) 
    }
};

void p2() {
    // Problem 2 : Leetcode 399. Evaluate Division - https://leetcode.com/problems/evaluate-division/description/?envType=study-plan-v2&envId=top-interview-150 

    vector<vector<string>> equations = { {"a","b"},{"c","d"} };
    vector<vector<string>> queries = { {"a","c"},{"b","d"},{"b","a"},{"d","c"} };
    vector<double> values = { 1.0,1.0 };
    vector<double> result = Problem2().calcEquation(equations, values, queries);
    for (double e : result) cout << e << " ";
    cout << endl;
}


int main() {
    // Day 28 of January 2025 

    p1();

    p2();


    return 0;
}