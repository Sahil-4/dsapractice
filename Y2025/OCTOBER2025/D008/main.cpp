#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
    int N = spells.size();
    int M = potions.size();
    sort(potions.begin(), potions.end());

    vector<int> pairs(N, 0);

    for (int i = 0; i < N; i++) {
      long long need = ceil((success * 1.0l) / (spells[i] * 1.0l));
      auto it = lower_bound(potions.begin(), potions.end(), need);
      int index = distance(potions.begin(), it);
      pairs[i] = max(0, M - index);
    }

    return pairs;

    // Complexity analyss
    // Time : O(M * Log(M)) + O(N * Log(M))
    // Space : O(M)
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 2300. Successful Pairs of Spells and Potions - https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/?envType=daily-question&envId=2025-10-08 

  vector<pair<pair<vector<int>, vector<int>>, long long>> testcases = {
    { { { 5,1,3 }, { 1,2,3,4,5 } }, 7 },
    { { { 3,1,2 }, { 8,5,8 } }, 16}
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    vector<int> pairs = s1->successfulPairs(tc.first.first, tc.first.second, tc.second);
    for (auto& p : pairs) cout << p << " ";
    cout << endl;
  }
}

class Node {
public:
  int data;
  Node* left;
  Node* right;

  Node(int x) {
    data = x;
    left = NULL;
    right = NULL;
  }

  static void print(Node* root) {
    if (root == NULL) return;

    queue<Node*> que;
    que.push(root);

    while (!que.empty()) {
      int N = que.size();

      for (int i = 0; i < N; i++) {
        Node* node = que.front();
        que.pop();

        cout << node->data << " ";

        if (node->left) que.push(node->left);
        if (node->right) que.push(node->right);
      }
    }
  }
};

class Solution2 {
  int preIndex = 0;
  int postIndex = 0;

  vector<int> pre;
  vector<int> post;

  Node* construct(int parent) {
    if (preIndex >= pre.size()) return NULL;
    if (parent == post[postIndex]) return NULL;

    Node* node = new Node(pre[preIndex]);
    preIndex++;

    node->left = construct(node->data);
    node->right = construct(node->data);

    postIndex++;
    return node;
  }

public:
  Node* constructTree(vector<int>& pre, vector<int>& post) {
    // code here
    this->pre = pre;
    this->post = post;
    this->preIndex = 0;
    this->postIndex = 0;

    return construct(-1);

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(N) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Construct Tree from Preorder & Postorder - https://www.geeksforgeeks.org/problems/construct-tree-from-preorder-postorder/1 

  vector<pair<vector<int>, vector<int>>> testcases = {
    {
      {1, 2, 4, 8, 9, 5, 3, 6, 7},
      {8, 9, 4, 5, 2, 6, 7, 3, 1},
    },
    {
      {1, 2, 4, 5, 3, 6, 7},
      {4, 5, 2, 6, 7, 3, 1},
    },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    Node* root = s2->constructTree(tc.first, tc.second);
    Node::print(root);
    cout << endl;
  }
}

int main() {
  // Day 8 of October 2025

  p1();

  p2();

  return 0;
}
