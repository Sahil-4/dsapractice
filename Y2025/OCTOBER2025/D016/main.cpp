#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int findSmallestInteger(vector<int>& nums, int value) {
    unordered_map<int, int> cnt;
    for (long long x : nums) {
      int r = (int)((x % value + value) % value);
      cnt[r]++;
    }

    int mex = 0;
    while (true) {
      int r = mex % value;
      auto it = cnt.find(r);
      if (it == cnt.end() || it->second == 0) break;
      it->second--;
      mex++;
    }

    return mex;
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 2598. Smallest Missing Non-negative Integer After Operations - https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/description/?envType=daily-question&envId=2025-10-16 

  vector<pair<vector<int>, int>> testcases = {
    { { 1,-10,7,13,6,8 }, 5 },
    { { 1,-10,7,13,6,8 }, 7 },
    { { 3,0,3,2,4,2,1,1,0,4 }, 5 },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->findSmallestInteger(tc.first, tc.second) << endl;
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
    queue<Node*> que;
    que.push(root);

    while (!que.empty()) {
      int N = que.size();
      for (int i = 0; i < N; i++) {
        Node* temp = que.front(); que.pop();
        cout << temp->data << " ";

        if (temp->left) que.push(temp->left);
        if (temp->right) que.push(temp->right);
      }
      cout << endl;
    }
  }
};

class Solution2 {
public:
  Node* removekeys(Node* root, int l, int r) {
    // code here
    // pseudo 
    // if (!root) return null;
    // if (root < range) return right;
    // if (root > range) return left;
    // if (root in range) return root; // after updating left, and right

    if (!root) return NULL;

    Node* left = removekeys(root->left, l, r);
    Node* right = removekeys(root->right, l, r);

    if (root->data < l) return right;
    if (root->data > r) return left;

    if (left && left->data >= l && left->data <= r) {
      root->left = left;
    } else {
      root->left = NULL;
    }
    if (right && right->data >= l && right->data <= r) {
      root->right = right;
    } else {
      root->right = NULL;
    }

    return root;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(H) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Remove BST keys outside given range - https://www.geeksforgeeks.org/problems/remove-bst-keys-outside-given-range/1 

  vector<pair<vector<int>, pair<int, int>>> testcases = {
    { { 6, -13, 14, -10000, -8, 13, 15, -10000, -10000, 7}, { -10, 13 } },
    { { 14, 4, 16, 2, 8, 15, -10000, -8, 3, 7, 10}, { 2, 6 } },
    { { 2, 1, 3}, { 1, 3 } },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    Node* root = Node::build(tc.first, -10000);
    Node::print(root);
    Node* modified = s2->removekeys(root, tc.second.first, tc.second.second);
    Node::print(modified);
  }
}

int main() {
  // Day 16 of October 2025

  p1();

  p2();

  return 0;
}
