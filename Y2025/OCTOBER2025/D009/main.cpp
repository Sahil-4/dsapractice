#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  long long minTime(vector<int>& skill, vector<int>& mana) {
    int N = skill.size();
    int M = mana.size();

    vector<long long> pipeline(N, 0);

    for (int j = 0; j < M; j++) {
      long long now = pipeline[0];

      for (int i = 1; i < N; i++) {
        long long timeTaken = skill[i - 1] * 1LL * mana[j];
        now = max(pipeline[i], now + timeTaken);
      }
      long long timeTaken = skill[N - 1] * 1LL * mana[j];
      pipeline[N - 1] = now + timeTaken;

      for (int i = N - 2; i >= 0; i--) {
        int timeTaken = skill[i + 1] * mana[j];
        pipeline[i] = pipeline[i + 1] - timeTaken;
      }
    }

    return pipeline[N - 1];

    // Complexity analysis 
    // Time : O(M * N) 
    // Space : O(N) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3494. Find the Minimum Amount of Time to Brew Potions - https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/description/?envType=daily-question&envId=2025-10-09 

  vector<pair<vector<int>, vector<int>>> testcases = {
    { { 1,5,2,4 }, { 5,1,4,2 } },
    { { 1,1,1 }, { 1,1,1 } },
    { { 1,2,3,4 }, { 1,2 } },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << s1->minTime(tc.first, tc.second) << endl;
  }
}

class Node {
public:
  int data;
  Node* left;
  Node* right;

  Node(int val) {
    data = val;
    left = NULL;
    right = NULL;
  }

  Node* setLeft(int val) {
    this->left = new Node(val);
    return this->left;
  }

  Node* setRight(int val) {
    this->right = new Node(val);
    return this->right;
  }
};

class Solution2 {
private:
  void __postOrderTraversal(vector<int>& output, Node* root) {
    if (!root) return;

    __postOrderTraversal(output, root->left);
    __postOrderTraversal(output, root->right);

    output.push_back(root->data);
  }

public:
  vector<int> postOrder(Node* root) {
    // code here
    vector<int> output;
    __postOrderTraversal(output, root);

    return output;
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Postorder Traversal - https://www.geeksforgeeks.org/problems/postorder-traversal/1 

  Node* root = new Node(11);
  root->setLeft(15)->setLeft(7);

  Solution2* s2 = new Solution2();
  vector<int> output = s2->postOrder(root);
  for (auto& e : output) cout << e << " ";
  cout << endl;
}

int main() {
  // Day 9 of October 2025

  p1();

  p2();

  return 0;
}
