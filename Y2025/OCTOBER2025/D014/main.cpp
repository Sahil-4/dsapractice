#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  bool hasIncreasingSubarrays(vector<int>& nums, int k) {
    int N = nums.size();

    vector<int> increasing(N + 1, 1);

    for (int i = 1; i < N; i++) {
      if (nums[i] > nums[i - 1]) {
        increasing[i] += increasing[i - 1];
      }
    }

    for (int i = k - 1; i <= N - k; i++) {
      if (increasing[i] >= k && increasing[i + k] >= k) return true;
    }

    return false;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(N) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3349. Adjacent Increasing Subarrays Detection I - https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/description/?envType=daily-question&envId=2025-10-14 

  vector<pair<vector<int>, int>> testcases = {
    { { 2,5,7,8,9,2,3,4,3,1 }, 3},
    { { 1,2,3,4,4,4,4,5,6,7 }, 5},
    { { -3,-19,-8,-16 }, 2},
    { { -15,19 }, 1},
    { { 5,8,-2,-1 }, 2},
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->hasIncreasingSubarrays(tc.first, tc.second) << endl;
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
  int nodeSum(Node* root, int l, int r) {
    // code here
    if (!root) return 0;

    int lsum = nodeSum(root->left, l, r);
    int rsum = nodeSum(root->right, l, r);

    if (root->data < l) return rsum; // move to right 
    if (root->data > r) return lsum; // move to left 

    return root->data + lsum + rsum;
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Sum of Nodes in BST Range - https://www.geeksforgeeks.org/problems/range-sum-of-bst/1 

  vector<pair<vector<int>, pair<int, int>>> testcases = {
    { { 10, 5, 15, 3, 7, -1, 18 }, { 7, 15 } },
    { { 22, 12, 30, 8, 20 }, { 10, 22 } },
    { { 8, 5, 11, 3, 6, -1, 20 }, { 11, 15 } },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    Node* root = Node::build(tc.first);
    cout << s2->nodeSum(root, tc.second.first, tc.second.second) << endl;
  }
}

int main() {
  // Day 14 of October 2025

  p1();

  p2();

  return 0;
}
