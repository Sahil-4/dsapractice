#include <bits/stdc++.h>

using namespace std;

class Solution1 {
private:
  string add(string s, int inc) {
    string out(s);
    for (int i = 1; i < out.size(); i += 2) {
      out[i] = '0' + (((out[i] - '0') + inc) % 10);
    }

    return out;
  }

  string rotate(string s, int k) {
    int N = s.size();
    string pref = s.substr(k, N - k);
    string suff = s.substr(0, k);
    return pref + suff;
  }

public:
  string findLexSmallestString(string s, int a, int b) {
    int N = s.size();

    queue<string> nodesQueue;
    set<string> visited;
    string lexSmallest = s;

    nodesQueue.push(lexSmallest);
    visited.insert(lexSmallest);

    while (!nodesQueue.empty()) {
      string node = nodesQueue.front(); nodesQueue.pop();

      lexSmallest = min(lexSmallest, node);

      string left = add(node, a);
      if (visited.find(left) == visited.end()) {
        nodesQueue.push(left);
        visited.insert(left);
      }

      string right = rotate(node, b);
      if (visited.find(right) == visited.end()) {
        nodesQueue.push(right);
        visited.insert(right);
      }
    }

    return lexSmallest;

    // Complexity analysis 
    // Time : O(N * N)
    // Space : O(2N)
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 1625. Lexicographically Smallest String After Applying Operations - https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/description/?envType=daily-question&envId=2025-10-19 

  vector<pair<string, pair<int, int>>> testcases = {
    { "5525", { 9, 2 } },
    { "74", { 5, 1 } },
    { "0011", { 4, 2 } },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->findLexSmallestString(tc.first, tc.second.first, tc.second.second) << endl;
  }
}

class Node {
public:
  int data;
  Node* left;
  Node* right;

  Node(int val) {
    data = val;
    left = right = NULL;
  }

  static Node* build(vector<int>& nodes, int nullFlag = -1) {
    Node* root = new Node(nodes[0]);
    queue<Node*> que;
    que.push(root);

    int index = 1;
    int N = nodes.size();

    while (!que.empty()) {
      Node* temp = que.front(); que.pop();

      if (index >= N) break;

      int leftVal = nodes[index++];
      if (leftVal != nullFlag) {
        temp->left = new Node(leftVal);
        que.push(temp->left);
      }

      if (index >= N) break;

      int rightVal = nodes[index++];
      if (rightVal != nullFlag) {
        temp->right = new Node(rightVal);
        que.push(temp->right);
      }
    }

    return root;
  }

  static void print(Node* root) {
    if (!root)return;

    print(root->left);
    cout << root->data << " ";
    print(root->right);
  }
};

class Solution2 {
private:
  priority_queue<pair<int, int>> maxHeap;

  void solve(Node* root, int target, int k) {
    if (!root) return;

    solve(root->left, target, k);

    maxHeap.push({ abs(root->data - target), root->data });
    if (maxHeap.size() > k) maxHeap.pop();

    solve(root->right, target, k);
  }

public:
  vector<int> getKClosest(Node* root, int target, int k) {
    // code here
    solve(root, target, k);

    vector<int> output;
    while (!maxHeap.empty()) {
      output.push_back(maxHeap.top().second);
      maxHeap.pop();
    }

    return output;
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks K closest Values - https://www.geeksforgeeks.org/problems/k-closest-values/1 

  vector<pair<vector<int>, pair<int, int>>> testcases = {
    { { 20, 8, 22, 4, 12, -1, -1, -1, -1, 10, 14 }, { 17, 3 } },
    { { 5, 4, 8, 1 }, { 5, 2 } },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    Node* root = Node::build(tc.first);
    vector<int> closestK = s2->getKClosest(root, tc.second.first, tc.second.second);
    for (auto& e : closestK) cout << e << " ";
    cout << endl;
  }
}

int main() {
  // Day 19 of October 2025

  p1();

  p2();

  return 0;
}
