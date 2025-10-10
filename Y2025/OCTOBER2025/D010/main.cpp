#include <bits/stdc++.h>

using namespace std;

class Solution1 {
  int solve1(vector<int>& energy, int k) {
    int N = energy.size();
    int maxE = -10001;

    for (int si = 0; si < N; si++) {
      int collectE = 0;
      for (int i = si; i < N; i += k) {
        collectE += energy[i];
      }

      maxE = max(maxE, collectE);
    }

    return maxE;

    // Complexity analysis 
    // Time : O(N*N) 
    // Space : O(1) 
  }

  int solve2(vector<int>& energy, int k) {
    int N = energy.size();
    vector<int> psum(energy);

    for (int i = k; i < N; i++) {
      psum[i] = max(psum[i], psum[i] + psum[i - k]);
    }

    int maxE = -10001;
    for (int i = N - k; i < N; i++) {
      maxE = max(maxE, psum[i]);
    }

    return maxE;

    // Complexity analysis 
    // Time : O(2N) 
    // Space : O(W) 
  }

public:
  int maximumEnergy(vector<int>& energy, int k) {
    // return solve1(energy, k);
    return solve2(energy, k);
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3147. Taking Maximum Energy From the Mystic Dungeon - https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/description/?envType=daily-question&envId=2025-10-10 

  vector<pair<vector<int>, int>> testcases = {
    { { 5,2,-10,-5,1 }, 3 },
    { { -2,-3,-1 }, 2 },
    { { -1,-2,-5,-2,-2,-5,-2,-3,-7,-5,-2,-3,-7,-2,-3,-7,-2,-5,-2,-3,-7 }, 2 },
    { { -1,-2,-5,-2,-2,-5,-2,-3,-7,-5,-2,-3,-7,-2,-3,-7,-2,-5,-2,-3,-7 }, 5 },
    { { -1,-2,-5,-2,-2,-5,-2,-3,-7,-5,-2,-3,-7,-2,-3,-7,-2,-5,-2,-3,-7 }, 7 },
    { { -1,-2,-5,-2,-2,-5,-2,-3,-7,-5,-2,-3,-7,-2,-3,-7,-2,-5,-2,-3,-7 }, 1 },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->maximumEnergy(tc.first, tc.second) << endl;
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

  static Node* build(vector<int>& nodes) {
    Node* root = new Node(nodes[0]);
    queue<Node*> que;
    que.push(root);

    int index = 1;
    int N = nodes.size();

    while (!que.empty()) {
      Node* temp = que.front(); que.pop();

      if (index >= N) break;

      int leftVal = nodes[index++];
      if (leftVal != -1) {
        temp->left = new Node(leftVal);
        que.push(temp->left);
      }

      if (index >= N) break;

      int rightVal = nodes[index++];
      if (rightVal != -1) {
        temp->right = new Node(rightVal);
        que.push(temp->right);
      }
    }

    return root;
  }

  static void print(Node* root) {
    vector<int> v;
    queue<Node*> que;
    que.push(root);

    while (!que.empty()) {
      Node* temp = que.front(); que.pop();

      v.push_back(temp->data);

      if (temp->left) que.push(temp->left);
      if (temp->right) que.push(temp->right);
    }

    for (int e : v) cout << e << " ";
    cout << endl;
  }
};

class Solution2 {
public:
  vector<int> zigZagTraversal(Node* root) {
    // code here
    vector<int> output;

    deque<Node*> q;
    q.push_back(root);
    int level = 1;

    while (!q.empty()) {
      int LN = q.size();

      if (level & 1) {
        // left to right 
        while (LN--) {
          Node* n = q.front(); q.pop_front();
          output.push_back(n->data);

          if (n->left) q.push_back(n->left);
          if (n->right) q.push_back(n->right);
        }
      } else {
        // right to left 
        while (LN--) {
          Node* n = q.back(); q.pop_back();
          output.push_back(n->data);

          if (n->right) q.push_front(n->right);
          if (n->left) q.push_front(n->left);
        }
      }

      level++;
    }

    return output;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(W) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks ZigZag Tree Traversal - https://www.geeksforgeeks.org/problems/zigzag-tree-traversal/1 

  vector<vector<int>> testcases = {
    {1, 2, 3, 4, 5, 6, 7},
    {7, 9, 7, 8, 8, 6, -1, 10, 9},
    {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31},
    {1, 2, 3, 4, 5, 6, 7, 8, 9, -1, 11, -1, 13, 15, 16, 17, -1, 19, 20, 21, 22, 23, -1, 25, 26, 27, 28, 29, 30, 30},
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    Node* root = Node::build(tc);
    Node::print(root);
    vector<int> output = s2->zigZagTraversal(root);
    for (auto& e : output) cout << e << " ";
    cout << endl;
  }
}

int main() {
  // Day 10 of October 2025

  p1();

  p2();

  return 0;
}
