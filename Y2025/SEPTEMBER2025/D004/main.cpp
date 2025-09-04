#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int findClosest(int x, int y, int z) {
    int d1 = abs(x - z);
    int d2 = abs(y - z);
    return d1 == d2 ? 0 : d1 < d2 ? 1 : 2;

    // Complexity analysis 
    // Time : O(1) 
    // Space : O(1) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3516. Find Closest Person - https://leetcode.com/problems/find-closest-person/description/?envType=daily-question&envId=2025-09-04 

  vector<vector<int>> testcases = {
    {2, 7, 4},
    {2, 5, 6},
    {1, 5, 3},
  };
  Solution1* s1 = new Solution1();
  for (auto tc : testcases) {
    int out = s1->findClosest(tc[0], tc[1], tc[2]);
    cout << "out: " << out << endl;
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
private:
  Node* setNull(Node* head, int k) {
    Node* curr = head;

    for (int i = 1; i < k; i++) {
      if (curr->next == NULL) break;
      curr = curr->next;
    }

    Node* next = curr->next;
    curr->next = NULL;

    return next;
  }

  Node* reverse(Node* head) {
    Node* prev = NULL;
    Node* curr = head;

    while (curr != NULL) {
      Node* next = curr->next;
      curr->next = prev;
      prev = curr;
      curr = next;
    }

    return prev;
  }

public:
  Node* reverseKGroup(Node* head, int k) {
    // code here
    Node* temp = head;
    Node* nhead = NULL;
    Node* prev = NULL;

    while (temp != NULL) {
      Node* shead = temp;
      Node* snext = setNull(shead, k);
      Node* rhead = reverse(shead);

      if (nhead == NULL) nhead = rhead;

      if (prev != NULL) prev->next = rhead;
      prev = shead;

      temp = snext;
    }

    if (nhead == NULL) nhead = head;

    return nhead;

    // Complexity analysis 
    // Time : O(2N) 
    // Space : O(1) + extra pointers 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Linked List Group Reverse - https://www.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1 

  vector<pair<vector<int>, int>> testcases = {
    { {1, 2, 3, 4, 5},  1},
    { {1, 2, 3, 4, 5},  5},
    { {1, 2, 3, 4, 5, 6},  2},
    { {1, 2, 3, 4, 5, 6},  3},
    { {1, 2, 3, 4, 5, 6},  5},
    { {1, 2, 3, 4, 5, 6},  6},
  };

  Solution2* s2 = new Solution2();
  for (auto tc : testcases) {
    Node* head = Node::build(tc.first);
    head->print();
    cout << "k: " << tc.second << endl;
    s2->reverseKGroup(head, tc.second);
    head->print();
  }
}

int main() {
  // Day 4 of September 2025

  p1();

  p2();

  return 0;
}
