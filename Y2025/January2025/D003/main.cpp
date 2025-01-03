#include <bits/stdc++.h>

using namespace std;


class Problem1 {
    int recursion(vector<int>& prices, int N, int index, int hold) {
        if (index == N) return 0;

        int profit = 0;

        if (hold == 0) {
            int buy = -prices[index] + recursion(prices, N, index + 1, 1);
            int not_buy = recursion(prices, N, index + 1, hold);
            profit = max(buy, not_buy);
        }
        else {
            int sell = prices[index] + recursion(prices, N, index + 1, 0);
            int not_sell = recursion(prices, N, index + 1, hold);
            profit = max(sell, not_sell);
        }

        return profit;

        // Complexity analysis 
        // Time : O(2^N) 
        // Space : O(N) stack 
    }

    int memoize(vector<int>& prices, int N, int index, int hold, vector<vector<int>>& dp) {
        if (index == N) return 0;

        if (dp[index][hold] != -1) return dp[index][hold];

        int profit = 0;

        if (hold == 0) {
            int buy = -prices[index] + memoize(prices, N, index + 1, 1, dp);
            int not_buy = memoize(prices, N, index + 1, hold, dp);
            profit = max(buy, not_buy);
        }
        else {
            int sell = prices[index] + memoize(prices, N, index + 1, 0, dp);
            int not_sell = memoize(prices, N, index + 1, hold, dp);
            profit = max(sell, not_sell);
        }

        return dp[index][hold] = profit;

        // Complexity analysis 
        // Time : O(2*N*2) 
        // Space : O(N) stack + O(N*2) memory 
    }

    int tabulation(vector<int>& prices, int N) {
        vector<vector<int>> dp(N + 1, vector<int>(2, 0));

        // base - already handled 

        // recurrence 
        for (int index = N - 1; index >= 0; index--) {
            for (int hold = 1; hold >= 0; hold--) {
                int profit = 0;

                if (hold == 0) {
                    int buy = -prices[index] + dp[index + 1][1];
                    int not_buy = dp[index + 1][hold];
                    profit = max(buy, not_buy);
                }
                else {
                    int sell = prices[index] + dp[index + 1][0];
                    int not_sell = dp[index + 1][hold];
                    profit = max(sell, not_sell);
                }

                dp[index][hold] = profit;
            }
        }

        // return 
        return dp[0][0];

        // Complexity analysis 
        // Time : O(N*2) 
        // Space : O(N*2) memory 
    }

    int optimal(vector<int>& prices, int N) {
        vector<int> dpp(2, 0); // index 
        vector<int> dpn(2, 0); // index + 1 

        // base - already handled 

        // recurrence 
        for (int index = N - 1; index >= 0; index--) {
            // hold = 0 
            int buy = -prices[index] + dpp[1];
            int not_buy = dpp[0];
            dpn[0] = max(buy, not_buy);

            // hold = 1 
            int sell = prices[index] + dpp[0];
            int not_sell = dpp[1];
            dpn[1] = max(sell, not_sell);

            // update dp 
            dpp = dpn;
        }

        // return 
        return dpp[0];

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(2*2) memory 
    }

    int greedy(vector<int>& prices, int N) {
        int mprofit = 0;

        for (int buy_day = 0, sell_day = 1; sell_day < N; sell_day++, buy_day++) {
            if (prices[buy_day] < prices[sell_day]) {
                mprofit += prices[sell_day] - prices[buy_day];
            }
        }

        return mprofit;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }

public:
    int maxProfit(vector<int>& prices) {
        int N = prices.size();
        // return recursion(prices, N, 0, 0);

        // vector<vector<int>> dp(N+1, vector<int>(2, -1));
        // return memoize(prices, N, 0, 0, dp);

        // return tabulation(prices, N);

        // return optimal(prices, N);

        return greedy(prices, N);
    }
};

void p1() {
    // Problem 1 : Leetcode 122. Best Time to Buy and Sell Stock II - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/stock-buy-and-sell-1587115621/1 

    vector<int> prices = { 1,3,1,2,2,5 };
    cout << Problem1().maxProfit(prices) << endl;
}

class Problem2 {
    bool recursion(vector<int>& nums, int N, int index) {
        if (index >= N - 1) return true;

        bool out = false;
        int mjump = nums[index];
        while (!out && mjump > 0) {
            out = recursion(nums, N, index + mjump--);
        }

        return out;

        // Complexity analysis 
        // Time : O(N^N) 
        // Space : O(N) 
    }

    bool memoize(vector<int>& nums, int N, int index, vector<int>& dp) {
        if (index >= N - 1) return true;

        if (dp[index] != -1) return dp[index] == 1;

        bool out = false;
        int mjump = nums[index];
        while (!out && mjump > 0) {
            out = memoize(nums, N, index + mjump--, dp);
        }

        return dp[index] = out;

        // Complexity analysis 
        // Time : O(2*N*N) 
        // Space : O(N) + O(N) memory 
    }

    bool tabulation(vector<int>& nums, int N) {
        vector<int> dp(N + 1, 0);

        // base case 
        dp[N] = 1;
        dp[N - 1] = 1;

        for (int index = N - 2; index >= 0; index--) {
            int out = 0;
            int mjump = nums[index];
            while (!out && mjump > 0) {
                if (index + mjump >= N || dp[index + mjump] == 1) out = 1;
                mjump--;
            }
            dp[index] = out;
        }

        return dp[0];

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(N) memory 
    }

    bool greedy(vector<int>& nums, int N) {
        int reached = 0; // till now we have reached till 0th index 

        for (int i = 0; i < N; i++) {
            // if i was unable to reach at this stair 
            if (i > reached) return false;

            int can_reach = i + nums[i]; // i can reach to from ith stair 
            reached = max(reached, can_reach); // maximum stair i can reach 
        }

        // if i can reach last stair 
        return reached >= N - 1;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }

public:
    bool canJump(vector<int>& nums) {
        int N = nums.size();

        // return recursion(nums, N, 0);

        // vector<int> dp(N+1, -1);
        // return memoize(nums, N, 0, dp);

        // return tabulation(nums, N);

        return greedy(nums, N);
    }
};

void p2() {
    // Problem 2 : Leetcode 55. Jump Game - https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/jump-game/1 

    // vector<int> nums = {0, 1, 5};
    // vector<int> nums = { 5, 1, 5 };
    vector<int> nums = { 1, 1, 5 };
    cout << Problem2().canJump(nums) << endl;
}

class Problem3 {
    int BOUND = (int)1e9;

    int recursion(vector<int>& nums, int N, int index) {
        if (index >= N - 1) return 0;

        int out = BOUND;
        int maxj = nums[index];

        for (int len = 1; len <= maxj; len++) {
            int jumps = 1 + recursion(nums, N, index + len);
            out = min(out, jumps);
        }

        return out;

        // Complexity analysis 
        // Time : O(ei ^ N) 
        // Space : O(N) stack 
    }

    int memoize(vector<int>& nums, int N, int index, vector<int>& dp) {
        if (index >= N - 1) return 0;

        if (dp[index] != -1) return dp[index];

        int out = BOUND;
        int maxj = nums[index];

        for (int len = 1; len <= maxj; len++) {
            int jumps = 1 + memoize(nums, N, index + len, dp);
            out = min(out, jumps);
        }

        return dp[index] = out;

        // Complexity analysis 
        // Time : O(2 * ei * N) 
        // Space : O(N) stack + O(N) memory 
    }

    int tabulation(vector<int>& nums, int N) {
        vector<int> dp(N + 1, 0);

        // base - handled 

        // recurrence 
        for (int index = N - 2; index >= 0; index--) {
            int out = BOUND;

            for (int len = 1; len <= nums[index]; len++) {
                int jumps = 1;
                if (index + len < N) jumps += dp[index + len];
                out = min(out, jumps);
            }

            dp[index] = out;
        }

        // return 
        return dp[0] < BOUND ? dp[0] : -1;

        // Complexity analysis 
        // Time : O(ei * N) 
        // Space : O(N) memory 
    }

    int greedy(vector<int>& nums, int N) {
        if (N <= 1) return 0;

        // greed criteira - chose farthest index from available window 

        int jumps = 0;

        // checkpoint - farthest i can reach 
        // reached - current index i reached 
        int checkpoint = 0, reached = 0;

        for (int i = 0; i < N; i++) {
            // extend the farthest window 
            checkpoint = max(checkpoint, i + nums[i]);

            if (i == reached) {
                reached = checkpoint;
                jumps++;
                if (checkpoint >= N - 1) break;
            }
        }

        return jumps;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }

public:
    int jump(vector<int>& nums) {
        int N = nums.size();

        // return recursion(nums, N, 0);

        // vector<int> dp(N, -1);
        // return memoize(nums, N, 0, dp);

        // return tabulation(nums, N);

        return greedy(nums, N);
    }
};

void p3() {
    // Problem 3 : Leetcode 45. Jump Game II - https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1 

    vector<int> nums = { 1,2,3 };
    cout << Problem3().jump(nums) << endl;
}

class Problem4 {
    int brute(vector<int>& citations) {
        // there are h papers with h citations 
        // if h is 1 then there is 1 paper with citations 1 
        // if h is 2 then there are 2 papers with citations 2 
        // if h is 3 then there are 3 papers with citations 3 
        // we have to find the maximum h 

        int N = citations.size(); // total number of papers 
        int h = 0;

        for (int ch = 1; ch <= N; ch++) {
            int pcount = 0;
            for (int i = 0; i < N; i++) {
                if (citations[i] >= ch) pcount++;
            }

            if (pcount >= ch) h = ch;
        }

        return h;

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(1) 
    }

    int binary_search(vector<int>& citations) {
        int N = citations.size(); // total number of papers 

        int hIndex = 0;

        int l = 1, h = N;
        while (l <= h) {
            int ci = l + (h - l) / 2;

            int pcount = 0;
            for (int i = 0; i < N; i++) {
                if (citations[i] >= ci) pcount++;
            }

            if (pcount >= ci) {
                hIndex = ci;
                l = ci + 1;
            }
            else {
                h = ci - 1;
            }
        }

        return hIndex;

        // Complexity analysis 
        // Time : O(Log(N) * N) 
        // Space : O(1) 
    }

    int sort_count(vector<int> citations) {
        int N = citations.size();

        sort(citations.begin(), citations.end(), greater<int>());

        int hi = 0;
        while (hi < N && citations[hi] > hi) hi++;

        return hi;

        // Complexity analysis 
        // Time : O(N*Log(N) + N) 
        // Space : O(1) 
    }

    int counting_sort(vector<int>& citations) {
        int N = citations.size();

        vector<int> citationsCount(N + 1, 0);

        // count citaions 
        for (int c : citations) {
            if (c >= N) citationsCount[N]++;
            else citationsCount[c]++;
        }

        int count = 0;
        // return maximum possible h index 
        for (int i = N; i >= 0; i--) {
            count += citationsCount[i];
            if (count >= i) return i;
        }

        return 0;

        // Complexity analysis 
        // Time : O(N + N) 
        // Space : O(N) 
    }

public:
    int hIndex(vector<int>& citations) {
        // return brute(citations);

        // return binary_search(citations);

        // return sort_count(citations);

        return counting_sort(citations);
    }
};

void p4() {
    // Problem 4 : Leetcode 274. H-Index - https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/find-h-index--165609/1 

    vector<int> citations = { 1,0,1,0,0,2,5,7,5,0,7,5,2,6,1 };
    cout << Problem4().hIndex(citations) << endl;
}


int main() {
    // Day 3 of January 2025 

    p1();

    p2();

    p3();

    p4();


    return 0;
}