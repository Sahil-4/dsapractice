#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;

int recursion(vector<int>& coins, int index, int amount) {
    if (index == 0) {
        if (amount % coins[index] == 0) {
            return amount / coins[index];
        }
        return -1;
    }

    int not_pick = 0 + recursion(coins, index - 1, amount);
    int pick = -1;

    if (coins[index] <= amount) {
        int rec = recursion(coins, index, amount - coins[index]);
        if (rec != -1) pick = 1 + rec;
    }

    if (pick != -1 && not_pick != -1) return min(pick, not_pick);
    if (pick == -1) return not_pick;
    return pick;

    // Complexity analysis 
    // Time : O(2^n) 
    // Space : O(n * amount) 
}

int memoization(vector<int>& coins, int index, int amount, vector<vector<int>>& dp) {
    if (index == 0) {
        if (amount % coins[index] == 0) {
            return amount / coins[index];
        }
        return 1e9;
    }

    if (dp[index][amount] != -1) {
        return dp[index][amount];
    }

    int not_pick = 0 + memoization(coins, index - 1, amount, dp);
    int pick = INT_MAX;

    if (amount >= coins[index]) {
        pick = 1 + memoization(coins, index, amount - coins[index], dp);
    }

    return dp[index][amount] = min(pick, not_pick);

    // Complexity analysis 
    // Time : O(amount) 
    // Space : O(n * amount) + O(amount) 
}

int coinChange(vector<int>& coins, int amount) {
    int N = coins.size();

    // recursion
    // return recursion(coins, N - 1, amount);

    // memoization
    vector<vector<int>> dp(N, vector<int>(amount + 1, -1));
    int ans = memoization(coins, N - 1, amount, dp);
    return ans >= 1e9 ? -1 : ans;
}

void p1() {
    // Problem 1 : Leetcode 322. Coin Change - 
    // https://leetcode.com/problems/coin-change/description/ 
    // Geeksforgeeks - 
    // https://www.geeksforgeeks.org/problems/number-of-coins1824/1 

    int amount = 6249;
    vector<int> coins = { 186,419,83,408 };

    int coin = coinChange(coins, amount);
    cout << coin << endl;
}


int main() {
    // Day 5 of DP 

    p1();


    return 0;
}
