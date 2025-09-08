#include <bits/stdc++.h>

using namespace std;

class Solution1 {
private:
  bool hasZero(int num) {
    while (num > 0) {
      if (num % 10 == 0) return true;
      num /= 10;
    }
    return false;
  }

public:
  vector<int> getNoZeroIntegers(int n) {
    // we can form pair {a, b} as
    // a = [1 to <n], b = n - a
    // by this a + b == n
    // now for all such pairs
    // we just have to check whether they contain any zero at any position
    // if a or b contains zero we cant take any of them
    // and will move to next possible pairs
    // to check whether a number has zero in it we use divide and modulo operator
    // while num > 0, 
    // we check (num%10 == 0) i.e. last digit is equal to 0 
    // if (num%10 == 0) return true 
    // else update num = floor(num/10) and move to next digit

    for (int a = 1; a < n; a++) {
      int b = n - a;
      if (!hasZero(a) && !hasZero(b)) return { a, b };
    }

    return { 0, 0 };

    // Complexity analysis
    // Time : O(N * Log(N))
    // Space : O(1)
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 1317. Convert Integer to the Sum of Two No-Zero Integers - https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/description/?envType=daily-question&envId=2025-09-08 

  vector<int> testcases = { 2, 10000, 11, 15, 2501 };

  Solution1* s1 = new Solution1();
  for (auto tc : testcases) {
    cout << "IN: " << tc << endl;
    auto out = s1->getNoZeroIntegers(tc);
    cout << "OUT: " << out[0] << ", " << out[1] << endl;
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
  Node* merge(Node* l1, Node* l2) {
    // merges two sorted linked lists into one 
    Node* head = new Node(-1);
    Node* temp = head;

    while (l1 != NULL && l2 != NULL) {
      if (l1->data <= l2->data) {
        temp->next = l1;
        l1 = l1->next;
        temp = temp->next;
      }
      else {
        temp->next = l2;
        l2 = l2->next;
        temp = temp->next;
      }
    }

    if (l1) temp->next = l1;
    if (l2) temp->next = l2;

    return head->next;
  }

  Node* split(Node* head) {
    // split the list into two parts and return head of right part 
    Node* slow = head;
    Node* fast = head->next;

    while (fast != NULL && fast->next != NULL) {
      slow = slow->next;
      fast = fast->next;
      fast = fast->next;
    }

    Node* next = slow->next;
    slow->next = NULL;

    return next;
  }

public:
  Node* mergeSort(Node* head) {
    // code here
    // take range of list [low, high] both inclusive
    // if low > high, no element → return null
    // if low == high, only one element, → return that single node (already sorted)
    // else case
    // divide + conquer + combine → return
    // to split the linked list, 
    // find the middle node, using slow–fast pointer method
    // unlink the next pointer of middle, 
    // so the list is divided into two separate sublists:
    // one starting from the head (left half)
    // one starting from the middle’s next (right half)
    // recursive sort
    // recursively call merge sort on the left and right half
    // after recursion, 
    // both halves will be sorted individually
    // and we get two sorted lists heads
    // merge
    // merge the two sorted linked lists into a single sorted list,
    // using two pointers l1, l2 compare data of both nodes (l1, l2) and
    // attach the smaller one to the result,
    // do this for all nodes of l1, and l2
    // return/result
    // return the head pointer of the merged, sorted linked list

    // zero nodes 
    if (head == NULL) return head;
    // only one node 
    if (head->next == NULL) return head;

    Node* left = head;
    Node* right = split(head);

    left = mergeSort(left);
    right = mergeSort(right);

    Node* nhead = merge(left, right);

    return nhead;

    // Complexity analysis 
    // Time : O(N * Log(N)) 
    // Space : O(1) + few extra pointers 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Merge Sort for Linked List - https://www.geeksforgeeks.org/problems/sort-a-linked-list/1 

  vector<vector<int>> testcases = {
    {1},
    {4, 2},
    {1, 2, 3, 4, 5},
    {5, 4, 3, 2, 1},
    {3, 3, 3, 3, 3},
    {2, 4, 1, 3, 2, 3, 1, 2},
    {10, 1, 2, 8, 3, 7, 4, 6, 5, 9},
    {100, 90, 80, 70, 60, 50, 40, 30, 20, 10},
  };

  Solution2* s2 = new Solution2();
  for (auto tc : testcases) {
    Node* head = Node::build(tc);
    cout << "IN: ";
    head->print();
    head = s2->mergeSort(head);
    cout << "OUT: ";
    head->print();
  }
}

int main() {
  // Day 8 of September 2025

  p1();

  p2();

  return 0;
}
