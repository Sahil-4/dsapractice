#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  int numberOfPairs(vector<vector<int>>& points) {
    // copy input
    vector<vector<int>> copy(points);

    // sort by { ASC x, DESC y }
    auto comparator = [](vector<int>& p1, vector<int>& p2) {
      return p1[0] == p2[0] ? p1[1] > p2[1] : p1[0] < p2[0];
    };
    sort(copy.begin(), copy.end(), comparator);

    int N = copy.size();
    int count = 0;

    for (int i = 0; i < N; i++) {
      // alice's coordinates 
      int xi = copy[i][0], yi = copy[i][1];
      int ymax = INT_MIN;

      for (int j = i + 1; j < N; j++) {
        // bob's coordinates 
        int xj = copy[j][0], yj = copy[j][1];

        // valid rectangle 
        if (yj <= yi && yj > ymax) {
          ymax = yj;
          count++;
        }
      }
    }

    return count;

    // Complexity analysis
    // Time : O(N * Log(N)) + O(N * N)
    // Space : O(N)
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3027. Find the Number of Ways to Place People II - https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/description/?envType=daily-question&envId=2025-09-03 

  vector<vector<vector<int>>> testcases = {
    {{1,1},{2,2},{3,3}},
    {{6,2},{4,4},{2,6}},
    {{3,1},{1,3},{1,1}},
  };

  Solution1* s1 = new Solution1();
  for (auto tc : testcases) {
    int out = s1->numberOfPairs(tc);
    cout << out << endl;
  }
}

class Node {
public:
  int data;
  Node* next;
  Node* prev;

  Node(int x) {
    data = x;
    next = NULL;
    prev = NULL;
  }

  Node* addNext(int x) {
    this->next = new Node(x);
    this->next->prev = this;
    return this->next;
  }

  void print() {
    Node* temp = this;
    while (temp != NULL) {
      cout << temp->data << " ";
      temp = temp->next;
    } cout << endl;
  }
};

class Solution2 {
public:
  Node* reverse(Node* head) {
    // code here
    Node* prev = NULL;
    Node* curr = head;

    while (curr != NULL) {
      prev = curr;

      Node* next = curr->next;
      Node* temp = curr->prev;
      curr->prev = curr->next;
      curr->next = temp;

      curr = next;
    }

    return prev;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(1) + some extra pointers 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Reverse a Doubly Linked List - https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1 

  Node* head = new Node(0);
  head->addNext(1)->addNext(2)->addNext(3);

  Solution2* s2 = new Solution2();
  head->print();
  head = s2->reverse(head);
  head->print();
}

int main() {
  // Day 3 of September 2025

  p1();

  p2();

  return 0;
}
