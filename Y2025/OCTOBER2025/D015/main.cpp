#include <bits/stdc++.h>

using namespace std;

class Solution1 {
  bool hasIncreasingSubarrays(vector<int>& nums, int k) {
    int N = nums.size();

    vector<int> increasing(N + 1, 1);

    for (int i = 1; i < N; i++) {
      if (nums[i] > nums[i - 1]) {
        increasing[i] += increasing[i - 1];
      }
    }

    for (int i = k - 1; i <= N - k; i++) {
      if (increasing[i] >= k && increasing[i + k] >= k) {
        return true;
      }
    }

    return false;
  }

  int solve1(vector<int>& nums) {
    int N = nums.size();
    int low = 1;
    int high = N / 2;
    int ans = 1;

    while (low <= high) {
      int mid = low + (high - low) / 2;
      if (hasIncreasingSubarrays(nums, mid)) {
        ans = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    return ans;

    // Complexity analysis
    // Time : O(N * Log(N))
    // Space : O(N)
  }

  int solve2(vector<int>& nums) {
    int N = nums.size();

    int currCount = 1;
    int prevCount = 0;
    int maxxCount = 0;

    for (int i = 1; i < N; i++) {
      if (nums[i] > nums[i - 1]) {
        currCount++;
      } else {
        prevCount = currCount;
        currCount = 1;
      }

      maxxCount = max(maxxCount, min(currCount, prevCount));
      maxxCount = max(maxxCount, currCount / 2);
    }

    return maxxCount;

    // Complexity analysis
    // Time : O(N)
    // Space : O(N)
  }

public:
  int maxIncreasingSubarrays(vector<int>& nums) {
    // return solve1(nums);
    return solve2(nums);
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3350. Adjacent Increasing Subarrays Detection II - https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/description/?envType=daily-question&envId=2025-10-15 

  vector<vector<int>> testcases = {
    {2,5,7,8,9,2,3,4,3,1},
    {1,2,3,4,4,4,4,5,6,7},
    {1,2,3,4,5,1,2,3,4,5},
    {1,2,3,4,5,6,7,8,9,10},
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->maxIncreasingSubarrays(tc) << endl;
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
  int count = 0;
  int el = -1;

  void solve1(Node* root, int k) {
    if (!root) return;

    solve1(root->left, k);

    if (count < k) {
      el = root->data;
      count++;
    }

    solve1(root->right, k);
  }

public:
  int kthSmallest(Node* root, int k) {
    // code here
    // use in-order traversal 
    solve1(root, k);
    return count == k ? el : -1;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(W) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks k-th Smallest in BST - https://www.geeksforgeeks.org/problems/find-k-th-smallest-element-in-bst/1 

  vector<pair<vector<int>, int>> testcases = {
    { { 20, 8, 22, 4, 12, -1, -1, -1, -1, 10, 14 }, 3 },
    { { 2, 1, 3 }, 5 },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    Node* root = Node::build(tc.first);
    cout << s2->kthSmallest(root, tc.second) << endl;
  }
}

int main() {
  // Day 15 of October 2025

  p1();

  p2();

  return 0;
}
