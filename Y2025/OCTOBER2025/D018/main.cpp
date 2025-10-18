#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int maxDistinctElements(vector<int>& nums, int k) {
    // nums = [1,2,2,3,3,4], k = 2
    // set = { -1, 6, 0, 5, 1, 4 }
    // [-1,2,2,3,3,6]
    // [-1,0,2,3,5,6]
    // [-1,0,1,4,5,6]
    // output = 6
    // nums = [4,4,4,4], k = 1
    // set = { 3, 5, 4 }
    // [3,4,4,5]
    // [3,4,4,5]
    // [3,4,4,5]
    // output = 3
    // nums = [1,2,2,3,3,4], k = 2
    // [-1,2,2,3,3,4]
    // last = -1, 
    // curr = max(last + 1, curr - k);
    // just make sure curr is valid curr >= nums[i] - k && nums[i] + k <= curr

    vector<int> copy(nums);
    sort(copy.begin(), copy.end());

    int distincts = 1;
    int last = copy[0] - k;

    for (int i = 1; i < copy.size(); i++) {
      int maxPossible = copy[i] + k;
      int minPossible = copy[i] - k;
      int safe = last + 1;

      int copyUpdated = max(minPossible, safe);

      if (copyUpdated <= maxPossible) {
        distincts++;
        last = copyUpdated;
      } else {
        last = maxPossible;
      }
    }

    return distincts;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(N) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3397. Maximum Number of Distinct Elements After Operations - https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/description/?envType=daily-question&envId=2025-10-18 

  vector<pair<vector<int>, int>> testcases = {
    { {1,2,2,3,3,4 }, 2 },
    { {4,4,4,4 }, 1 },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->maxDistinctElements(tc.first, tc.second) << endl;
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
  vector<int> store;
  int n = 0;

  void listNodes(Node* root) {
    if (!root) return;

    listNodes(root->left);
    store.push_back(root->data);
    n++;
    listNodes(root->right);
  }

  int kth = -1;
  int k = 0;

  int countNodes(Node* root) {
    if (!root) return 0;
    return 1 + countNodes(root->left) + countNodes(root->right);
  }

  void kthNode(Node* root) {
    if (!root) return;

    kthNode(root->left);
    if (k == 0) {
      kth = root->data;
    }
    k--;
    kthNode(root->right);
  }

public:
  int findMedian(Node* root) {
    // Code here
    // listNodes(root);
    // return store[((n + (n % 2))/2) - 1];

    n = countNodes(root);
    k = (((n + (n % 2)) / 2) - 1);

    kthNode(root);

    return kth;
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Median of BST - https://www.geeksforgeeks.org/problems/median-of-bst/1 

  vector<vector<int>> testcases = {
    {20, 8, 22, 4, 12, -1, -1, -1, -1, 10, 14},
    {5, 4, 8, 1},
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    Node* root = Node::build(tc);
    cout << s2->findMedian(root) << endl;
  }
}

int main() {
  // Day 18 of October 2025

  p1();

  p2();

  return 0;
}
