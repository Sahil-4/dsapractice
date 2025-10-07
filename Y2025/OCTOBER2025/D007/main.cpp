#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  vector<int> avoidFlood(vector<int>& rains) {
    int n = rains.size();

    vector<int> answer(n, 0);
    unordered_map<int, int> lastSeen;
    set<int> zeroIndex;

    for (int i = 0; i < n; i++) {
      int lake = rains[i];

      if (lake == 0) {
        zeroIndex.insert(i);
        continue;
      }

      if (lastSeen.find(lake) != lastSeen.end()) {
        if (zeroIndex.size() == 0) return {};

        // find the index of last zero
        auto it = zeroIndex.lower_bound(lastSeen[lake]);
        if (it == zeroIndex.end()) return {};

        answer[*it] = lake;
        zeroIndex.erase(it);
      }

      answer[i] = -1;
      lastSeen[lake] = i;
    }

    for (int i = 0; i < n; i++) {
      if (answer[i] == 0) answer[i] = 1;
    }

    return answer;

    // Complexity analysis 
    // Time : O(N * Log(N)) 
    // Space : O(2N) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 1488. Avoid Flood in The City - https://leetcode.com/problems/avoid-flood-in-the-city/description/?envType=daily-question&envId=2025-10-07 

  vector<vector<int>> testcases = {
    {1,2,3,4},
    {1,2,0,0,2,1},
    {1,2,0,1,2},
    {1,2,0,0,2,1,0,0,2,1,2,0,0,2,1,0,0,2,1},
    {1,2,0,0,3,3},
    {1,2,0,0,2,1,0,0,0,1,2,0,0,2,1,0,0,2,1,2,0,0,2,1,0,0,2,1},
    {0,0,0},
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    vector<int> answer = s1->avoidFlood(tc);
    cout << "[ ";
    for (auto& a : answer) cout << a << " ";
    cout << "]" << endl;
  } cout << endl;
}

class Node {
public:
  int data;
  Node* left;
  Node* right;

  Node(int x) {
    data = x;
    left = right = NULL;
  }
};

class Solution2 {
public:
  vector<int> bottomView(Node* root) {
    // code here
    // minKey = -1
    // root = [1, 2, 3, 4, 5, N, 6]
    // levelOrder = [[1,0]]
    // levelOrder = [[2,-1], [3,1]]
    // levelOrder = [[4,-2], [5,0], [6,2]] 
    // map = { 0:5, -1:2, 1:3, -2:4, 2:6 } 
    // view = [ 4,2,5,3,6 ] 

    int minKey = 0;
    unordered_map<int, int> vmap;
    queue<pair<Node*, int>> levelOrderQue;

    levelOrderQue.push({ root, 0 });

    while (!levelOrderQue.empty()) {
      pair<Node*, int> f = levelOrderQue.front(); levelOrderQue.pop();

      Node* node = f.first;
      int nodeKey = f.second;

      vmap[nodeKey] = node->data;
      minKey = min(minKey, nodeKey);

      if (node->left) {
        levelOrderQue.push({ node->left, nodeKey - 1 });
      }
      if (node->right) {
        levelOrderQue.push({ node->right, nodeKey + 1 });
      }
    }

    vector<int> view;
    while (vmap.find(minKey) != vmap.end()) {
      view.push_back(vmap[minKey]);
      minKey++;
    }

    return view;
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Bottom View of Binary Tree  - https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1 

  Node* root = new Node(1);
  root->left = new Node(2);
  root->right = new Node(3);
  root->left->left = new Node(4);
  root->left->right = new Node(5);
  root->right->right = new Node(6);
  // root->right->right->right = new Node(7);

  Solution2* s2 = new Solution2();
  vector<int> bview = s2->bottomView(root);
  cout << "[ ";
  for (auto& e : bview) cout << e << " ";
  cout << "]" << endl;
  cout << endl;
}

int main() {
  // Day 7 of October 2025

  p1();

  p2();

  return 0;
}
