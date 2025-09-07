#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  vector<int> sumZero(int n) {
    // n = 5
    // {-1 + 1 + 0 + -2 + 2}

    vector<int> output;

    if (n & 1) {
      output.push_back(0);
    }

    for (int i = 1; i <= n / 2; i++) {
      output.push_back(i);
      output.push_back(-i);
    }

    return output;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 1304. Find N Unique Integers Sum up to Zero - https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description/?envType=daily-question&envId=2025-09-07 

  vector<int> testcases = { 1, 2, 5, 4, 1000 };

  Solution1* s1 = new Solution1();
  for (auto tc : testcases) {
    vector<int> out = s1->sumZero(tc);
    for (auto o : out) {
      cout << o << " ";
    } cout << endl;
  }
}

class Node {
public:
  int data;
  Node* next;

  Node(int x) {
    data = x;
    next = NULL;
  }

  Node* addNext(int x) {
    this->next = new Node(x);
    return this->next;
  }

  void print() {
    Node* temp = this;
    while (temp != NULL) {
      cout << temp->data << " ";
      temp = temp->next;
    } cout << endl;
  }

  static Node* build(vector<int> data) {
    Node* temp = NULL;
    Node* head = NULL;
    for (auto& val : data) {
      if (head == NULL) {
        head = new Node(val);
        temp = head;
      }
      else {
        temp = temp->addNext(val);
      }
    }

    return head;
  }
};

class Solution2 {
public:
  Node* mergeKLists(vector<Node*>& arr) {
    // code here
    auto comparator = [](Node* n1, Node* n2) {
      return n1->data >= n2->data;
    };
    priority_queue<Node*, vector<Node*>, decltype(comparator)> pq(comparator);

    for (Node* n : arr) pq.push(n);

    Node* head = new Node(-1);
    Node* temp = head;

    while (!pq.empty()) {
      Node* curr = pq.top(); pq.pop();
      Node* next = curr->next;

      curr->next = NULL;
      temp->next = curr;

      temp = temp->next;

      if (next != NULL) pq.push(next);
    }

    return head->next;

    // Complexity analysis 
    // Time : O(N) + O(K) 
    // Space : O(N) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Merge K sorted linked lists - https://www.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1 

  vector<vector<vector<int>>> testcases = {
    { {1, 3, 7}, {2, 4, 8}, {9} },
    { {1, 3}, {8}, {4, 5, 6} },
  };

  Solution2* s2 = new Solution2();
  for (auto tc : testcases) {
    vector<Node*> arr;
    for (auto stc : tc) {
      arr.push_back(Node::build(stc));
    }
    Node* head = s2->mergeKLists(arr);
    head->print();
  }
}

int main() {
  // Day 7 of September 2025

  p1();

  p2();

  return 0;
}
