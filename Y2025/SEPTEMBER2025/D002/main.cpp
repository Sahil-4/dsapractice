#include <bits/stdc++.h>

using namespace std;

class Solution1 {
private:
  int solution1(vector<vector<int>>& points) {
    // sort the points - {ASC x, DESC y}
    vector<vector<int>> copy(points);
    auto comparator = [](vector<int>& p1, vector<int>& p2) {
      return (p1[1] != p2[1]) ? p1[1] < p2[1] : p1[0] > p2[0];
    };
    sort(copy.begin(), copy.end(), comparator);

    int N = copy.size();

    int count = 0;

    auto isPair = [&copy](int pi, int pj) {
      // return true if point i and j can form a pair 

      int xi = copy[pi][1], xj = copy[pj][1];
      int yi = copy[pi][0], yj = copy[pj][0];

      // condition 1 - point i is on upper left of point j 
      if (!(xi <= xj && yi >= yj)) return false;

      // condition 2 - there is no other point between point i, and j 
      for (int i = pi + 1; i < pj; i++) {
        int x = copy[i][1];
        int y = copy[i][0];
        if ((xi <= x && x <= xj) && (yi >= y && y >= yj)) return false;
      }

      return true;
    };

    for (int i = 0; i < N; i++) {
      for (int j = i + 1; j < N; j++) {
        if (isPair(i, j)) count++;
      }
    }

    return count;

    // Complexity analysis 
    // Time : O(N * Log(N)) + O(N * N * N) 
    // Space : O(N) 
  }

  int solution2(vector<vector<int>>& points) {
    // copy input
    vector<vector<int>> copy(points);

    // sort by { ASC y, DESC x }
    auto comparator = [](vector<int>& p1, vector<int>& p2) {
      return p1[0] == p2[0] ? p1[1] > p2[1] : p1[0] < p2[0];
    };
    sort(copy.begin(), copy.end(), comparator);

    int N = copy.size();
    int count = 0;

    for (int i = 0; i < N; i++) {
      int xi = copy[i][1], last = -1;

      for (int j = i + 1; j < N; j++) {
        int xj = copy[j][1];
        if (xj <= xi && xj > last) {
          last = xj;
          count++;
        }
      }
    }

    return count;

    // Complexity analysis
    // Time : O(N * Log(N)) + O(N * N)
    // Space : O(N)
  }

public:
  int numberOfPairs(vector<vector<int>>& points) {
    // return solution1(points);
    return solution2(points);
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3025. Find the Number of Ways to Place People I - https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/description/?envType=daily-question&envId=2025-09-02 

  Solution1* s1 = new Solution1();
  int out = 0;
  vector<vector<vector<int>>> testCases = {
    { {1,1},{2,2},{3,3} },
    { { 6,2 },{4,4},{2,6} },
    { { 3,1 },{1,3},{1,1} },
    { { 1,5 },{2,0},{5,5} },
    { { 10,10 },{9,9},{8,8},{7,7},{6,6},{5,5},{4,4},{3,3},{2,2},{1,1} },
    { { 50,50 },{49,49},{48,48},{47,47},{46,46},{45,45},{44,44},{43,43},{42,42},{41,41} },
    { { 50,50 },{49,49},{48,48},{47,47},{46,46},{45,45},{44,44},{43,43},{42,42},{41,41},{10,10},{9,9},{8,8},{7,7},{6,6},{5,5},{4,4},{3,3},{2,2},{1,1} },
    { { 50,50 },{49,49},{48,48},{47,47},{46,46},{45,45},{44,44},{43,43},{42,42},{41,41},{40,40},{39,39},{38,38},{37,37},{36,36},{35,35},{34,34},{33,33},{32,32},{31,31},{30,30},{29,29},{28,28},{27,27},{26,26},{25,25},{24,24},{23,23},{22,22},{21,21},{20,20},{19,19},{18,18},{17,17},{16,16},{15,15},{14,14},{13,13},{12,12},{11,11},{10,10},{9,9},{8,8},{7,7},{6,6},{5,5},{4,4},{3,3},{2,2},{1,1} },
  };

  for (auto tc : testCases) {
    out = s1->numberOfPairs(tc);
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
};

class Solution2 {
private:
  int countNodes(Node* head) {
    int count = 0;

    Node* temp = head;
    while (temp != NULL) {
      temp = temp->next;
      count++;
    }

    return count;
  }

public:
  Node* swapKth(Node* head, int k) {
    // code here

    // count nodes 
    int N = countNodes(head);

    // invalid or same node
    if (k > N || 2 * k - 1 == N) return head;

    // find {kth prev, kth}
    Node* leftKthPrev = NULL;
    Node* leftKth = head;
    for (int i = 1; i < k; i++) {
      leftKthPrev = leftKth;
      leftKth = leftKth->next;
    }

    Node* rightKthPrev = NULL;
    Node* rightKth = head;
    for (int i = 1; i < N - k + 1; i++) {
      rightKthPrev = rightKth;
      rightKth = rightKth->next;
    }

    // update pointers 
    if (leftKthPrev != NULL) leftKthPrev->next = rightKth;
    if (rightKthPrev != NULL) rightKthPrev->next = leftKth;

    Node* temp = rightKth->next;
    rightKth->next = leftKth->next;
    leftKth->next = temp;

    if (k == 1) head = rightKth;
    if (k == N) head = leftKth;

    return head;

    // Complexity analysis 
    // Time : O(N) + O(2N) 
    // Space : O(4) pointers 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Swap Kth nodes from ends - https://www.geeksforgeeks.org/problems/swap-kth-node-from-beginning-and-kth-node-from-end-in-a-singly-linked-list/1 

  Solution2* s2 = new Solution2();
  Node* head = new Node(-1);
  head->addNext(1)->addNext(2)->addNext(3)->addNext(4)->addNext(5);

  head->next->print();
  head->next = s2->swapKth(head->next, 1);
  head->next->print();
}

int main() {
  // Day 2 of September 2025

  p1();

  p2();

  return 0;
}
