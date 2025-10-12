#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int magicalSum(int m, int k, vector<int>& nums) {
    const int MOD = 1e9 + 7;
    int n = nums.size();

    // Precompute binomial coefficients C[i][j]
    vector<vector<int>> C(m + 1, vector<int>(m + 1, 0));
    for (int i = 0; i <= m; i++) {
      C[i][0] = C[i][i] = 1;
      for (int j = 1; j < i; j++) {
        C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
      }
    }

    // Precompute powers: pow[i][cnt] = nums[i]^cnt % MOD
    vector<vector<int>> powv(n, vector<int>(m + 1, 1));
    for (int i = 0; i < n; i++) {
      for (int cnt = 1; cnt <= m; cnt++) {
        powv[i][cnt] = (1LL * powv[i][cnt - 1] * nums[i]) % MOD;
      }
    }

    // 4D DP: dp[pos][bits][carry][chosen]
    vector dp(n + 1,
      vector(k + 1,
        vector(m + 1,
          vector<int>(m + 1, 0))));

    dp[0][0][0][0] = 1;

    for (int pos = 0; pos < n; pos++) {
      for (int bits = 0; bits <= k; bits++) {
        for (int carry = 0; carry <= m; carry++) {
          for (int chosen = 0; chosen <= m; chosen++) {
            if (dp[pos][bits][carry][chosen] == 0) continue;

            int remaining = m - chosen;
            for (int cnt = 0; cnt <= remaining; cnt++) {
              int total = carry + cnt;
              int new_bits = bits + (total & 1);
              int new_carry = total >> 1;

              if (new_bits <= k && new_carry <= m) {
                long long add = 1LL * dp[pos][bits][carry][chosen]
                  * C[remaining][cnt] % MOD
                  * powv[pos][cnt] % MOD;

                dp[pos + 1][new_bits][new_carry][chosen + cnt] =
                  (dp[pos + 1][new_bits][new_carry][chosen + cnt] + (int)add) % MOD;
              }
            }
          }
        }
      }
    }

    int res = 0;
    for (int carry = 0; carry <= m; carry++) {
      int carry_bits = __builtin_popcount(carry);
      if (carry_bits <= k) {
        res = (res + dp[n][k - carry_bits][carry][m]) % MOD;
      }
    }

    return res;
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3539. Find Sum of Array Product of Magical Sequences - https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/description/?envType=daily-question&envId=2025-10-12 

  vector<pair<pair<int, int>, vector<int>>> testcases = {
    { { 5, 5 }, { 1,10,100,10000,1000000 } },
    { { 2, 2 }, {5,4,3,2,1} },
    { { 1, 1 }, { 28 } },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->magicalSum(tc.first.first, tc.first.second, tc.second) << endl;
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
  int tmoves = 0;

  int solve(Node* root) {
    if (!root) return 0;

    int l = solve(root->left);
    int r = solve(root->right);

    tmoves += abs(l);
    tmoves += abs(r);

    return root->data + l + r - 1;
  }

public:
  int distCandy(Node* root) {
    // code here
    tmoves = 0;
    solve(root);

    return tmoves;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(N) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Distribute Candies - https://www.geeksforgeeks.org/problems/distribute-candies-in-a-binary-tree/1 

  vector<vector<int>> testcases = {
    {1, 1, 1},
    {2, 0, 0},
    {0, 0, 2},
    {0, 2, 0},
    {0, 1, 2},
    {5, 0, 0, -1, -1, 0, 0},
    {2, 0, 0, -1, -1, 3, 0},
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    Node* root = Node::build(tc);
    Node::print(root);
    cout << endl;
    cout << s2->distCandy(root) << endl;
    cout << endl;
  }
}

int main() {
  // Day 12 of October 2025

  p1();

  p2();

  return 0;
}
