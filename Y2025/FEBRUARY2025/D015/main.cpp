#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    bool recursion(string& str, string substr, int i, unordered_set<string>& wordHashSet) {
        if (i == str.length()) return substr == "";

        bool result = false;

        for (int i2 = i; i2 < str.length() && !result; i2++) {
            substr.push_back(str[i2]);
            if (wordHashSet.find(substr) != wordHashSet.end()) {
                result = recursion(str, "", i2 + 1, wordHashSet);
            }
        }

        return result;

        // Complexity analysis 
        // Time : O(N) ~ 
        // Space : O(N) stack + O(N) substr + O(N) hashset 
    }

    bool memoize(string& str, string substr, int i, unordered_set<string>& wordHashSet, vector<int>& dp) {
        // if (i == str.length()) return substr == "";
        if (i == str.length()) return true;

        if (dp[i] != -1) return dp[i];

        bool result = false;

        for (int i2 = i; i2 < str.length() && !result; i2++) {
            substr.push_back(str[i2]);
            if (wordHashSet.find(substr) != wordHashSet.end()) {
                result = memoize(str, "", i2 + 1, wordHashSet, dp);
            }
        }

        return dp[i] = result;

        // Complexity analysis 
        // Time : O(N) ~ 
        // Space : O(N) stack + O(N) substr + O(N) hashset + O(N) dp 
    }

    bool tabulation(string& str, vector<string>& wordDict) {
        vector<int> dp(str.length() + 1, 0);

        // base case 
        dp[0] = true;

        // recurrence 
        for (int i = 1; i <= str.length(); i++) {
            for (const string& word : wordDict) {
                int starti = i - word.length();
                if (starti >= 0 && dp[starti] && str.substr(starti, word.length()) == word) {
                    dp[i] = true;
                    break;
                }
            }
        }

        // return 
        return dp[str.length()];

        // Complexity analysis 
        // Time : O(N*M) 
        // Space : O(N) dp 
    }

public:
    bool wordBreak(string str, vector<string>& wordDict) {
        // unordered_set<string> wordHashSet;
        // for (const string &word: wordDict) {
        //     wordHashSet.insert(word);
        // }

        // return recursion(str, "", 0, wordHashSet);

        // vector<int> dp(str.length(), -1);
        // return memoize(str, "", 0, wordHashSet, dp);

        return tabulation(str, wordDict);
    }
};

void p1() {
    // Problem 1 : Leetcode 139. Word Break - https://leetcode.com/problems/word-break/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/word-break1352/1 

    vector<string> wordDict = { "a","b","c","d","e","f" };
    cout << Problem1().wordBreak("abcdef", wordDict) << endl;
}

class Problem2 {
    int BOUND = (int)(1e9) + 7;

    int recursion(int amount, vector<int>& coins, int index) {
        if (amount == 0) return 0;
        if (index >= coins.size()) return BOUND;

        int not_pick = recursion(amount, coins, index + 1);
        int pick = BOUND;
        if (amount >= coins[index]) {
            pick = 1 + recursion(amount - coins[index], coins, index);
        }

        return min(not_pick, pick);

        // Complexity analysis 
        // Time : O(2^Amount) 
        // Space : O(Amount) 
    }

    int memoize(int amount, vector<int>& coins, int index, vector<vector<int>>& dp) {
        if (amount == 0) return 0;
        if (index >= coins.size()) return BOUND;

        if (dp[index][amount] != -1) return dp[index][amount];

        int not_pick = memoize(amount, coins, index + 1, dp);
        int pick = BOUND;
        if (amount >= coins[index]) {
            pick = 1 + memoize(amount - coins[index], coins, index, dp);
        }

        return dp[index][amount] = min(not_pick, pick);

        // Complexity analysis 
        // Time : O(2*N*Amount) 
        // Space : O(Amount) + O(Amount*N) dp 
    }

    int tabulation(int AMOUNT, vector<int>& coins) {
        vector<vector<int>> dp(coins.size() + 1, vector<int>(AMOUNT + 1, 0));

        // base case 
        for (int amount = 0; amount <= AMOUNT; amount++) dp[coins.size()][amount] = BOUND;
        for (int i = 0; i <= coins.size(); i++) dp[i][0] = 0;

        // recurrence 
        for (int index = coins.size() - 1; index >= 0; index--) {
            for (int amount = 1; amount <= AMOUNT; amount++) {
                int not_pick = dp[index + 1][amount];
                int pick = BOUND;
                if (amount >= coins[index]) {
                    pick = 1 + dp[index][amount - coins[index]];
                }

                dp[index][amount] = min(not_pick, pick);
            }
        }

        // return 
        return dp[0][AMOUNT];

        // Complexity analysis 
        // Time : O(N*Amount) 
        // Space : O(N*Amount) dp 
    }

    int optimised(int AMOUNT, vector<int>& coins) {
        vector<int> next(AMOUNT + 1, BOUND);

        // base case 
        next[0] = 0;

        // recurrence 
        for (int index = coins.size() - 1; index >= 0; index--) {
            vector<int> curr(AMOUNT + 1, BOUND);
            curr[0] = 0;

            for (int amount = 1; amount <= AMOUNT; amount++) {
                int not_pick = next[amount];
                int pick = BOUND;
                if (amount >= coins[index]) {
                    pick = 1 + curr[amount - coins[index]];
                }

                curr[amount] = min(not_pick, pick);
            }

            next = curr;
        }

        // return 
        return next[AMOUNT];

        // Complexity analysis 
        // Time : O(N*Amount) 
        // Space : O(2*Amount) dp 
    }

public:
    int coinChange(vector<int>& coins, int amount) {
        // int out = recursion(amount, coins, 0);

        // vector<vector<int>> dp(coins.size(), vector<int>(amount+1, -1));
        // int out = memoize(amount, coins, 0, dp);

        // int out = tabulation(amount, coins);

        int out = optimised(amount, coins);

        return out == BOUND ? -1 : out;
    }
};

void p2() {
    // Problem 2 : Leetcode 322. Coin Change - https://leetcode.com/problems/coin-change/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks -  https://www.geeksforgeeks.org/problems/number-of-coins1824/1 

    // vector<int> coins = { 1, 11, 6, 7 };
    // int amount = 13;
    vector<int> coins = { 411,412,413,414,415,416,417,418,419,420,421,422 };
    int amount = 9864;
    cout << Problem2().coinChange(coins, amount) << endl;
}

class Problem3 {
    int recursion(vector<int>& nums, int ci, int pi) {
        if (ci >= nums.size()) return 0;

        int not_take = recursion(nums, ci + 1, pi);
        int take = 0;
        if (pi == -1 || nums[ci] > nums[pi]) {
            take = 1 + recursion(nums, ci + 1, ci);
        }

        return max(take, not_take);

        // Complexity analysis 
        // Time : O(2^N) 
        // Space : O(N) stack 
    }

    int memoize(vector<int>& nums, int ci, int pi, vector<vector<int>>& dp) {
        if (ci >= nums.size()) return 0;

        if (dp[ci][pi + 1] != -1) return dp[ci][pi + 1];

        int not_take = memoize(nums, ci + 1, pi, dp);
        int take = 0;
        if (pi == -1 || nums[ci] > nums[pi]) {
            take = 1 + memoize(nums, ci + 1, ci, dp);
        }

        return dp[ci][pi + 1] = max(take, not_take);

        // Complexity analysis 
        // Time : O(2*N*N) 
        // Space : O(N) stack + O(N*N) dp 
    }

    int tabulation(vector<int>& nums) {
        int n = nums.size();

        vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));

        // base 
        // for (int pi = -1; pi <= n; pi++) dp[n][pi] = 0;

        // recurrence 
        for (int ci = n - 1; ci >= 0; ci--) {
            for (int pi = ci - 1; pi >= -1; pi--) {
                int not_take = dp[ci + 1][pi + 1];
                int take = 0;
                if (pi == -1 || nums[ci] > nums[pi]) {
                    take = 1 + dp[ci + 1][ci + 1];
                }

                dp[ci][pi + 1] = max(take, not_take);
            }
        }

        // return 
        return dp[0][0];

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(N*N) dp 
    }

    int optimised(vector<int>& nums) {
        int n = nums.size();

        vector<int> next(n + 1, 0);

        // base - handled 

        // recurrence 
        for (int ci = n - 1; ci >= 0; ci--) {
            vector<int> curr(n + 1, 0);
            for (int pi = ci - 1; pi >= -1; pi--) {
                int not_take = next[pi + 1];
                int take = 0;
                if (pi == -1 || nums[ci] > nums[pi]) {
                    take = 1 + next[ci + 1];
                }

                curr[pi + 1] = max(take, not_take);
            }

            next = curr;
        }

        // return 
        return next[0];

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(2*N) dp 
    }

public:
    int lengthOfLIS(vector<int>& nums) {
        // return recursion(nums, 0, -1);

        // int n = nums.size();

        // vector<vector<int>> dp(n+1, vector<int>(n+1, -1));
        // return memoize(nums, 0, -1, dp);

        // return tabulation(nums);

        return optimised(nums);
    }
};

void p3() {
    // Problem 3 : Leetcode 300. Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks -  https://www.geeksforgeeks.org/problems/longest-increasing-subsequence-1587115620/1 

    vector<int> nums = { 10,9,2,5,3,7,101,18 };
    cout << Problem3().lengthOfLIS(nums) << endl;
}


int main() {
    // Day 15 of February 2025 

    p1();

    p2();

    p3();


    return 0;
}