#include <bits/stdc++.h>

using namespace std;

class Solution1 {
private:
  bool isAnagram(string& a, string& b) {
    if (a.size() != b.size()) return false;

    vector<int> freq(26, 0);
    for (int i = 0; i < a.size(); i++) {
      freq[a[i] - 'a']++;
      freq[b[i] - 'a']--;
    }

    bool check = true;
    for (int i = 0; i < 26; i++) {
      check = check && freq[i] == 0;
    }

    return check;
  }

public:
  vector<string> removeAnagrams(vector<string>& words) {
    vector<string> output;
    output.push_back(words[0]);

    for (int i = 1; i < words.size(); i++) {
      if (output.empty() || !isAnagram(output.back(), words[i])) {
        output.push_back(words[i]);
      }
    }

    return output;

    // Complexity analysis 
    // Time : O(N * M) 
    // Space : O(26) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 2273. Find Resultant Array After Removing Anagrams - https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description/?envType=daily-question&envId=2025-10-13 

  vector<vector<string>> testcases = {
    {"abba","baba","bbaa","cd","cd"},
    {"a","b","c","d","e"},
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    vector<string> output = s1->removeAnagrams(tc);
    for (auto& word : output) cout << word << " ";
    cout << endl;
  } cout << endl;
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
  int solve(Node* node, unordered_map<Node*, int>& memo) {
    if (!node) return 0;

    if (memo.find(node) != memo.end()) return memo[node];

    // case 1 : dont select node, and move to node->child 
    int c1 = 0 + solve(node->left, memo) + solve(node->right, memo);

    // case 1 : select node, and move to node->child->child 
    int c2 = node->data;
    if (node->left) {
      c2 += solve(node->left->left, memo);
      c2 += solve(node->left->right, memo);
    }
    if (node->right) {
      c2 += solve(node->right->left, memo);
      c2 += solve(node->right->right, memo);
    }

    return memo[node] = max(c1, c2);
  }

public:
  int getMaxSum(Node* root) {
    // code here
    unordered_map<Node*, int> memo;
    return solve(root, memo);

    // Complexity analysis 
    // Time : O(2^N) 
    // Space : O(N) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Maximum Non-Adjacent Nodes Sum - https://www.geeksforgeeks.org/problems/maximum-sum-of-non-adjacent-nodes/1 

  vector<vector<int>> testcases = {
    { 11, 1, 2 },
    { 1, 2, 3, 4, -1, 5, 6 },
    { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    Node* root = Node::build(tc);
    cout << s2->getMaxSum(root) << endl;
  } cout << endl;
}

int main() {
  // Day 13 of October 2025

  p1();

  p2();

  return 0;
}
