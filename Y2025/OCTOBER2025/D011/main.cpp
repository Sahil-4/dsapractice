#include <bits/stdc++.h>

using namespace std;

class Solution1 {
  long long solve(vector<int>& uniques, int N, int index, unordered_map<int, int>& frequency, vector<long long>& dp) {
    if (index >= N) return 0;
    if (dp[index] != -1) return dp[index];

    // dont take uniques[index]
    long long skip = solve(uniques, N, index + 1, frequency, dp);

    // dont take uniques[index] and move to next possble place
    int nindex = lower_bound(uniques.begin() + index, uniques.end(), uniques[index] + 3) - uniques.begin();
    long long pick = (uniques[index] * 1LL * frequency[uniques[index]]) + solve(uniques, N, nindex, frequency, dp);

    return dp[index] = max(skip, pick);
  }

public:
  long long maximumTotalDamage(vector<int>& power) {
    // spell frequency map
    unordered_map<int, int> frequency;
    for (int e : power) frequency[e]++;

    // unique spells vector
    vector<int> uniques;
    for (auto& it : frequency) uniques.push_back(it.first);

    // sort unique spells
    sort(uniques.begin(), uniques.end());

    int N = uniques.size();
    vector<long long> dp(N, -1);
    return solve(uniques, N, 0, frequency, dp);

    // Complexity analysis
    // Time : O(N * Log(N))
    // Space : O(N)
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3186. Maximum Total Damage With Spell Casting - https://leetcode.com/problems/maximum-total-damage-with-spell-casting/description/?envType=daily-question&envId=2025-10-11 

  vector<vector<int>> testcases = {
    {1,1,3,4},
    {7,1,6,6},
    {3,4,5,6,6,7,1,1,1,1,1,9,9,9,9,9,9,9,9,9,6},
    {5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4},
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->maximumTotalDamage(tc) << endl;
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
private:
  int solve(Node* root, int& ans) {
    if (!root) return 0;

    int left = solve(root->left, ans);
    int right = solve(root->right, ans);

    // case 1 
    int c1 = left + right + root->data;
    // case 2 
    int c2 = max(left, right) + root->data;
    // case 3 
    int c3 = root->data;

    ans = max({ ans, c1, c2, c3 });

    return max(c2, c3);

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(N) 
  }

public:
  int findMaxSum(Node* root) {
    // code here
    int ans = -100000;

    solve(root, ans);

    return ans;
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Maximum path sum - https://www.geeksforgeeks.org/problems/maximum-path-sum-from-any-node/1 

  vector<vector<int>> testcases = {
    {-17, 11, 4, 20, -2, 10},
    {10, 2, 10, 20, 1, -10000, -25, -10000, -10000, -10000, -10000, 3, 4},
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    Node* root = Node::build(tc, -10000);
    Node::print(root);
    cout << s2->findMaxSum(root) << endl;
  }
}

int main() {
  // Day 11 of October 2025

  p1();

  p2();

  return 0;
}
