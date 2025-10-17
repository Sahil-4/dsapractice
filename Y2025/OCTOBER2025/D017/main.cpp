#include <bits/stdc++.h>

using namespace std;

class Solution1 {
private:
  typedef long long ll;
  unordered_map<long long, int> dp;

  ll solve(ll i, ll mask, ll change, int k, string& s) {
    int n = s.size();
    if (i == n) {
      return 1;
    }

    ll currState = (i << 27) | (mask << 1) | (change);

    if (dp.find(currState) != dp.end()) {
      return dp[currState];
    }

    int val = s[i] - 'a';
    ll newMask = mask | (1 << val);

    int count = __builtin_popcount(newMask);

    ll ans = 0;
    ll maxi = 0;

    if (count > k) {
      ans = 1 + solve(i + 1, 1 << val, change, k, s);
      maxi = max(maxi, ans);
    } else {
      ans = solve(i + 1, newMask, change, k, s);
      maxi = max(maxi, ans);
    }

    if (change) {
      return dp[currState] = maxi;
    }

    for (int j = 0; j < 26; j++) {
      ll newMask = mask | (1 << j);
      ll count = __builtin_popcount(newMask);

      if (count > k) {
        maxi = max(maxi, 1 + solve(i + 1, 1 << j, 1, k, s));
      } else {
        maxi = max(maxi, solve(i + 1, newMask, 1, k, s));
      }
    }

    return dp[currState] = maxi;
  }

public:
  int maxPartitionsAfterOperations(string s, int k) {
    return solve(0, 0, 0, k, s);

    // Complexity analysis 
    // Time : O(2^26) 
    // Space : O(2^26) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3003. Maximize the Number of Partitions After Operations - https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/description/?envType=daily-question&envId=2025-10-17 

  vector<pair<string, int>> testcases = {
    { "accca", 2 },
    { "aabaab", 3 },
    { "xxyz", 1 },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->maxPartitionsAfterOperations(tc.first, tc.second) << endl;
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
  int transform(Node* root, int fr) {
    if (!root) return fr;

    int data = root->data;

    int right = transform(root->right, fr);
    int left = transform(root->left, right + data);
    root->data = right;

    return left;
  }

public:
  void transformTree(Node* root) {
    // code here
    transform(root, 0);

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(H) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks BST to greater sum tree - https://www.geeksforgeeks.org/problems/bst-to-greater-sum-tree/1 

  vector<vector<int>> testcases = {
    { 11, 2, 29, 1, 7, 15, 40, -1, -1, -1, -1, -1, -1, 35, -1 },
    { 2, 1, 6, -1, -1, 3, 7 },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    Node* root = Node::build(tc);

    Node::print(root);
    cout << endl;

    s2->transformTree(root);

    Node::print(root);
    cout << endl;
  }
}

int main() {
  // Day 17 of October 2025

  p1();

  p2();

  return 0;
}
