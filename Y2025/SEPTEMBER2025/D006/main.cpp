#include <bits/stdc++.h>

using namespace std;

class Solution1 {
private:
  long long countOperations(int l, int r) {
    long long L = 1;
    long long S = 1;

    long long operations = 0;

    while (L <= r) {
      long long R = ((4 * L) - 1);

      long long start = max(L, (long long)l);
      long long end = min(R, (long long)r);

      long long count = end - start + 1;

      if (count > 0) operations += (count * S);

      S = S + 1;
      L = R + 1;
    }

    return operations;
  }

public:
  long long minOperations(vector<vector<int>>& queries) {
    long long toperations = 0;

    for (auto& query : queries) {
      int l = query[0];
      int r = query[1];

      long long operations = countOperations(l, r);

      toperations += ((operations + 1) / 2);
    }

    return toperations;

    // Complexity analysis 
    // Time : O(Q * Log4(R)) 
    // Space : O(1) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3495. Minimum Operations to Make Array Elements Zero - https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/?envType=daily-question&envId=2025-09-06 

  vector<vector<vector<int>>> testcases = {
    {{1,2},{2,4}},
    {{2,6}}
  };
  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    int out = s1->minOperations(tc);
    cout << out << endl;
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
  int lengthOfLoop(Node* head) {
    // code here
    // using slow and fast pointers
    Node* slow = head;
    Node* fast = head;

    while (fast != NULL && fast->next != NULL) {
      slow = slow->next;
      fast = fast->next;
      fast = fast->next;
      if (slow == fast) break;
    }

    // no loop present
    if (fast == NULL || fast->next == NULL) return 0;

    // loop present find length
    int length = 1;
    slow = slow->next;
    while (slow != fast) {
      length++;
      slow = slow->next;
    }

    return length;

    // Complexity analysis 
    // Time : O(2N) 
    // Space : O(1) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Find length of Loop - https://www.geeksforgeeks.org/problems/find-length-of-loop/1 

  vector<int> tc = { 1, 2, 3, 4, 5 };
  Node* head = Node::build(tc); // 0 loop length
  Solution2* s2 = new Solution2();
  cout << s2->lengthOfLoop(head) << endl;
}

int main() {
  // Day 6 of September 2025

  p1();

  p2();

  return 0;
}
