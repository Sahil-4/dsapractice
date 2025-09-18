#include <bits/stdc++.h>

using namespace std;

class TaskManager {
  // tasksMap { taskId -> { userId, priority } }
  // priority2TaskIdsMap { priority -> taskId[] }

  class TaskItem {
  public:
    int userId;
    int priority;

    TaskItem(int userId, int priority) {
      this->userId = userId;
      this->priority = priority;
    }
  };

  map<int, TaskItem*> tasksMap;
  map<int, set<int>> priority2TaskIdsMap;

public:
  TaskManager(vector<vector<int>>& tasks) {
    for (auto& task : tasks) {
      add(task[0], task[1], task[2]);
    }
  }

  void add(int userId, int taskId, int priority) {
    tasksMap[taskId] = new TaskItem(userId, priority);
    priority2TaskIdsMap[priority].insert(taskId);
  }

  void edit(int taskId, int newPriority) {
    int oldPriority = tasksMap[taskId]->priority;
    priority2TaskIdsMap[oldPriority].erase(taskId);
    if (priority2TaskIdsMap[oldPriority].size() == 0) {
      priority2TaskIdsMap.erase(oldPriority);
    }

    tasksMap[taskId]->priority = newPriority;
    priority2TaskIdsMap[newPriority].insert(taskId);
  }

  void rmv(int taskId) {
    int priority = tasksMap[taskId]->priority;
    priority2TaskIdsMap[priority].erase(taskId);
    if (priority2TaskIdsMap[priority].size() == 0) {
      priority2TaskIdsMap.erase(priority);
    }
    tasksMap.erase(taskId);
  }

  int execTop() {
    if (tasksMap.size() == 0) return -1;

    int highestPriority = priority2TaskIdsMap.rbegin()->first;
    int taskId = *priority2TaskIdsMap[highestPriority].rbegin();
    int userId = tasksMap[taskId]->userId;
    rmv(taskId);
    return userId;
  }

  // Complexity analysis
  // Time : O(Log(N))
  // Space : O(N)
};

/**
 * Your TaskManager object will be instantiated and called as such:
 * TaskManager* obj = new TaskManager(tasks);
 * obj->add(userId,taskId,priority);
 * obj->edit(taskId,newPriority);
 * obj->rmv(taskId);
 * int param_4 = obj->execTop();
 */

void p1() {
  // Problem 1 : POTD Leetcode 3408. Design Task Manager - https://leetcode.com/problems/design-task-manager/?envType=daily-question&envId=2025-09-18 

  vector<vector<int>> tasks = { {1,101,10},{2,102,20},{3,103,15} };
  TaskManager* tm = new TaskManager(tasks);
  tm->add(4, 104, 5);
  tm->edit(102, 8);
  cout << tm->execTop() << endl;
  tm->rmv(101);
  tm->add(5, 105, 15);
  cout << tm->execTop() << endl;
}

class Solution2 {
private:
  vector<int> solve(vector<int>& arr) {
    int N = arr.size();
    vector<int> answer(N, -1);

    for (int i = 0; i < N; i++) {
      for (int j = 1; j < N; j++) {
        int index = ((i + j) % N);
        if (arr[i] < arr[index]) {
          answer[i] = arr[index];
          break;
        }
      }
    }

    return answer;

    // Complexty analysis 
    // Time : O(N * N) 
    // Space : O(1) 
  }

  vector<int> optimal(vector<int>& arr) {
    int N = arr.size();
    int N2 = N * 2;
    vector<int> answer(N, -1);
    stack<int> stk;

    for (int i = N2 - 1; i >= 0; i--) {
      int index = i % N;
      while (!stk.empty() && stk.top() <= arr[index]) stk.pop();

      if (!stk.empty()) answer[index] = stk.top();

      stk.push(arr[index]);
    }

    return answer;

    // Complexty analysis 
    // Time : O(2N + N) 
    // Space : O(N) 
  }

public:
  vector<int> nextGreater(vector<int>& arr) {
    // code here
    // return brute(arr);

    return optimal(arr);
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Next Greater Element in Circular Array - https://www.geeksforgeeks.org/problems/next-greater-element/1 

  vector<vector<int>> testcases = {
    {0, 2, 3, 1, 1},
    {1, 3, 2, 4},
    {1, 2, 3, 4},
    {4, 3, 2, 1},
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << "INPUT:\t";
    for (auto& e : tc) cout << e << " ";
    cout << endl;

    vector<int> nge = s2->nextGreater(tc);
    cout << "OUTPUT:\t";
    for (auto& e : nge) cout << e << " ";
    cout << endl;
  }
}

int main() {
  // Day 18 of September 2025

  p1();

  p2();

  return 0;
}
