#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int makeTheIntegerZero(int num1, int num2) {
    for (int op = 1; op <= 60; op++) {
      long long remaining = num1 - ((long long)op * num2);
      if (remaining < op) return -1;
      if (op >= __builtin_popcountll(remaining)) return op;
    }
    return -1;

    // Complexity analysis 
    // Time : O(60 * 64) -> O(4 * 10^3)
    // Space : O(1) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 2749. Minimum Operations to Make the Integer Zero - https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/description/?envType=daily-question&envId=2025-09-05 

  vector<vector<int>> testcases = {
    {3, -2},
    {5, 7},
    {85, 42},
    {334521, -41},
    {3451, 2213},
    {1066381, -2233},
    {99861952, 12311},
    {1000000000, 100},
  };

  Solution1* s1 = new Solution1();
  for (auto tc : testcases) {
    cout << "IN: " << tc[0] << ", " << tc[1] << endl;
    int out = s1->makeTheIntegerZero(tc[0], tc[1]);
    cout << "OUT: " << out << endl;
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
  Node* segregate(Node* head) {
    // code here
    Node* zeroes = new Node(-1);
    Node* zeroesTemp = zeroes;
    Node* ones = new Node(-1);
    Node* onesTemp = ones;
    Node* twoes = new Node(-1);
    Node* twoesTemp = twoes;

    Node* temp = NULL;;

    temp = head;
    while (temp != NULL) {
      Node* next = temp->next;
      temp->next = NULL;

      if (temp->data == 0) {
        zeroesTemp->next = temp;
        zeroesTemp = zeroesTemp->next;
      }
      else if (temp->data == 1) {
        onesTemp->next = temp;
        onesTemp = onesTemp->next;
      }
      else {
        twoesTemp->next = temp;
        twoesTemp = twoesTemp->next;
      }

      temp = next;
    }

    onesTemp->next = (twoes->next != NULL) ? twoes->next : NULL;
    zeroesTemp->next = (ones->next != NULL) ? ones->next : twoes->next;

    if (zeroes->next != NULL) return zeroes->next;
    if (ones->next != NULL) return ones->next;
    if (twoes->next != NULL) return twoes->next;

    // temp = zeroes;
    // while (temp->next != NULL) temp = temp->next;
    // temp->next = ones->next;
    // while (temp->next != NULL) temp = temp->next;
    // temp->next = twoes->next;

    return NULL;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(1) + few extra pointers 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Sort a linked list of 0s, 1s and 2s - https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1 

  vector<vector<int>> testcases = {
    { 0, 0, 0, 0},
    { 1, 1, 1, 1},
    { 2, 2, 2, 2},
    { 1, 1, 0, 0},
    { 0, 0, 1, 1},
    { 0, 0, 2, 1},
  };

  Solution2* s2 = new Solution2();
  for (auto tc : testcases) {
    Node* head = Node::build(tc);
    cout << "IN: ";
    head->print();
    head = s2->segregate(head);
    cout << "OUT: ";
    head->print();
  }
}

int main() {
  // Day 5 of September 2025

  p1();

  p2();

  return 0;
}
