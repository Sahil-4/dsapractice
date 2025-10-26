#include <bits/stdc++.h>

using namespace std;

class Bank {
  long long DEPOSIT_LIMIT = 1000000000000;
  long long WITHDRAW_LIMIT = 1000000000000;
  vector<long long> accounts;
  int N = 0;

  bool isAccountValid(int account) { return account >= 1 && account <= N; }

  bool isDepositValid(int account, long long money) {
    if (!isAccountValid(account)) return false;
    return (money >= 0 && money <= DEPOSIT_LIMIT);
  }

  bool isWithdrawValid(int account, long long money) {
    if (!isAccountValid(account)) return false;
    return (money >= 0 && money <= min(accounts[account - 1], WITHDRAW_LIMIT));
  }

  bool isTransferValid(int account1, int account2, long long money) {
    if (!isWithdrawValid(account1, money)) return false;
    if (!isDepositValid(account2, money)) return false;
    return true;
  }

public:
  Bank(vector<long long>& balance) {
    N = balance.size();
    for (int i = 0; i < N; i++) {
      accounts.push_back(balance[i]);
    }
  }

  bool transfer(int account1, int account2, long long money) {
    if (!isTransferValid(account1, account2, money)) return false;

    withdraw(account1, money);
    deposit(account2, money);

    return true;
  }

  bool deposit(int account, long long money) {
    if (!isDepositValid(account, money)) {
      return false;
    }

    accounts[account - 1] += money;

    return true;
  }

  bool withdraw(int account, long long money) {
    if (!isWithdrawValid(account, money)) {
      return false;
    }

    accounts[account - 1] -= money;

    return true;
  }
};

/**
 * Your Bank object will be instantiated and called as such:
 * Bank* obj = new Bank(balance);
 * bool param_1 = obj->transfer(account1,account2,money);
 * bool param_2 = obj->deposit(account,money);
 * bool param_3 = obj->withdraw(account,money);
 */

void p1() {
  // Problem 1 : POTD Leetcode 2043. Simple Bank System - https://leetcode.com/problems/simple-bank-system/description/?envType=daily-question&envId=2025-10-26 

  vector<long long> balance = { 10, 100, 20, 50, 30 };
  Bank* obj = new Bank(balance);
  int account1 = 3;
  int account2 = 5;
  long long money = 10;
  bool param_1 = obj->transfer(account1, account2, money);
  bool param_2 = obj->deposit(account1, money);
  bool param_3 = obj->withdraw(account1, money);
  cout << param_1 << " " << param_2 << " " << param_3 << endl;
}

class Solution2 {
public:
  int minCost(vector<int>& arr) {
    // code here
    // arr[] = [4, 3, 2, 6]
    // heap = [2, 3, 4, 6]
    // heap = [5, 4, 6]
    // heap = [9, 6]
    // heap = [15]
    // cost = 3 + 2 + 5 + 4 + 15
    // cost = 29

    priority_queue<int, vector<int>, greater<int>> pq;
    for (int e : arr) pq.push(e);

    int tcost = 0;

    while (pq.size() > 1) {
      // two small pieces of ropes 
      int sm1 = pq.top(); pq.pop();
      int sm2 = pq.top(); pq.pop();

      // one joint piece of rope 
      int cost = sm1 + sm2;

      // increment cost 
      tcost += cost;

      // add new rope piece 
      pq.push(cost);
    }

    return tcost;

    // Complexity analysis 
    // Time : O(N * Log(N)) 
    // Space : O(N) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Minimum Cost of ropes - https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1 

  vector<vector<int>> testcases = {
    { 4, 3, 2, 6 },
    { 1, 2, 3, 4, 5 },
    { 5, 17, 100, 11 }
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    int result = s2->minCost(tc);
    cout << result << endl;
  }
}

int main() {
  // Day 26 of October 2025

  p1();

  p2();

  return 0;
}
