#include <bits/stdc++.h>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode* next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode* next) : val(x), next(next) {}

  static ListNode* build(vector<int>& arr) {
    ListNode* dummy = new ListNode();
    ListNode* temp = dummy;

    for (int e : arr) {
      temp->next = new ListNode(e);
      temp = temp->next;
    }

    return dummy->next;
  }

  static void print(ListNode* head) {
    ListNode* temp = head;
    while (temp) {
      cout << temp->val << " ";
      temp = temp->next;
    } cout << endl;
  }
};

class Solution1 {
public:
  ListNode* modifiedList(vector<int>& nums, ListNode* head) {
    unordered_set<int> numsSet;
    for (int e : nums) {
      numsSet.insert(e);
    }

    ListNode* dummyHead = new ListNode(-1);
    ListNode* dummyTail = dummyHead;
    ListNode* tail = head;

    while (tail) {
      if (numsSet.find(tail->val) == numsSet.end()) {
        dummyTail->next = tail;
        dummyTail = dummyTail->next;
        tail = tail->next;
      } else {
        dummyTail->next = NULL;
        tail = tail->next;
      }
    }

    return dummyHead->next;
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 3217. Delete Nodes From Linked List Present in Array - https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/?envType=daily-question&envId=2025-11-01 

  vector<pair<vector<int>, vector<int>>> testcases = {
    { { 1,2,3 }, { 1,2,3,4,5 } },
    { { 1 }, { 1,2,1,2,1,2 } },
    { { 5 }, { 1,2,3,4 } },
    { { 5 }, { 1,2,3,4,5 } },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    ListNode* head = ListNode::build(tc.second);
    ListNode::print(head);
    head = s1->modifiedList(tc.first, head);
    ListNode::print(head);
  }
}

class Solution2 {
  vector<int> topologicalSort(vector<vector<int>>& adj, int n, vector<int>& indegree) {
    int processedNodes = 0;
    vector<int> topos;

    queue<int> que;

    for (int u = 0; u < n; u++) {
      if (indegree[u] == 0) {
        que.push(u);
        processedNodes++;
      }
    }

    while (!que.empty()) {
      int u = que.front(); que.pop();

      topos.push_back(u);

      for (int v : adj[u]) {
        indegree[v]--;
        if (indegree[v] == 0) {
          que.push(v);
          processedNodes++;
        }
      }
    }

    if (processedNodes == n) return topos;
    return { };
  }

public:
  vector<int> findOrder(int n, vector<vector<int>>& prerequisites) {
    // code here
    vector<int> indegree(n, 0);
    vector<vector<int>> adj(n, vector<int>());
    for (vector<int>& prerequisite : prerequisites) {
      int x = prerequisite[0];
      int y = prerequisite[1];

      indegree[x]++;
      adj[y].push_back(x);
    }

    return topologicalSort(adj, n, indegree);
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Course Schedule II - https://www.geeksforgeeks.org/problems/course-schedule/1 

  vector<pair<int, vector<vector<int>>>> testcases = {
    { 3, {{1, 0}, {2, 1}}, },
    { 4, {{2, 0}, {2, 1}, {3, 2}}, },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    vector<int> order = s2->findOrder(tc.first, tc.second);
    for (int e : order) cout << e << " ";
    cout << endl;
  }
}

int main() {
  // Day 1 of November 2025

  p1();

  p2();

  return 0;
}
