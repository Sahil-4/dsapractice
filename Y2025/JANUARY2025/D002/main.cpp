#include <bits/stdc++.h>
#include <cassert>

using namespace std;

class Problem1 {
public:
    int removeDuplicates(vector<int>& nums) {
        // c = count of n = number, k = index/k
        // int c = 0, n = nums[0], k = 0;
        // for (int e : nums) {
        //     if (e != n) n = e, c = 1;
        //     else c++;

        //     if (c <= 2) nums[k++] = n;
        // }

        // return k;

        int k = 0;
        for (int e : nums) {
            if (k < 2 || e != nums[k - 2]) nums[k++] = e;
        }
        return k;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }
};

void p1() {
    // Problem 1 : Leetcode 80. Remove Duplicates from Sorted Array II - https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150 

    vector<int> nums = { 0,0,1,1,1,1,2,3,3 };
    vector<int> expected = { 0,0,1,1,2,3,3 };
    int k = Problem1().removeDuplicates(nums);
    assert(k == 7);
    for (int i = 0; i < k; i++) {
        assert(nums[i] == expected[i]);
    }
    cout << "Test passed" << endl;
}

class Problem2 {
    int method2(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int e = nums[0], c = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == e) c++;
            else if (c > nums.size() / 2) return e;
            else e = nums[i], c = 1;
        }

        if (c > nums.size() / 2) return e;
        return -1;

        // Complexity analysis 
        // Time : O(N*Log(N)) + O(N) 
        // Space : O(1) + modifying input data 
    }

    int method3(vector<int>& nums) {
        int e = 0, v = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (v == 0) e = nums[i];
            if (e == nums[i]) v++;
            else v--;
        }

        // verification 
        v = 0;
        for (int i = 0; i < nums.size(); i++) if (nums[i] == e) v++;

        if (v > nums.size() / 2) return e;
        return -1;

        // Complexity analysis 
        // Time : O(N + N) 
        // Space : O(1) 
    }

    int solve(vector<int>& nums) {
        // Method 1 : frequency table 

        // Method 2 : sort and count 
        // return method2(nums);

        // Method 3 : Moores voting algorithm 
        return method3(nums);
    }

public:
    int majorityElement(vector<int>& arr) {
        // your code here
        return solve(arr);
    }
};

void p2() {
    // Problem 2 : Leetcode 169. Majority Element - https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/majority-element-1587115620/1 

    vector<int> nums1 = { 1, 2, 3 };
    assert(Problem2().majorityElement(nums1) == -1);
    cout << "Test case 1 passed" << endl;
    vector<int> nums2 = { 1, 2, 1, 3, 1, 1, 1, 2, 1, 3, 1, 2, 2 };
    assert(Problem2().majorityElement(nums2) == 1);
    cout << "Test case 2 passed" << endl;
}

class Problem3 {
    // Clockwise
    void method1(vector<int>& nums, int k) {
        int N = nums.size();
        while (k--) {
            int temp = nums[N - 1];
            for (int i = N - 1; i >= 1; i--) {
                nums[i] = nums[i - 1];
            }
            nums[0] = temp;
        }

        // Complexity analysis
        // Time : O(K * N)
        // Space : O(1)
    }

    // Clockwise
    void method2(vector<int>& nums, int k) {
        // keet k under size
        k = k % nums.size();
        // reverse first n - k element
        reverse(nums.begin(), nums.end() - k);
        // reverse last k element
        reverse(nums.end() - k, nums.end());
        // reverse entire array
        reverse(nums.begin(), nums.end());

        // Complexity analysis
        // Time : O(2N)
        // Space : O(1)
    }

    // Counter clock wise

    void solve(vector<int>& nums, int k) {
        // method 1 : brute force
        // method1(nums, k);

        // method 2 :optimal
        method2(nums, k);
    }
    void method1_counter(vector<int>& nums, int k) {
        int N = nums.size();
        while (k--) {
            int temp = nums[0];
            for (int i = 0; i < N - 1; i++) {
                nums[i] = nums[i + 1];
            }
            nums[N - 1] = temp;
        }

        // Complexity analysis
        // Time : O(K * N)
        // Space : O(1)
    }

    void method2_counter(vector<int>& nums, int k) {
        // keet k under size
        k = k % nums.size();
        // reverse first n - k element
        reverse(nums.begin(), nums.begin() + k);
        // reverse last k element
        reverse(nums.begin() + k, nums.end());
        // reverse entire array
        reverse(nums.begin(), nums.end());

        // Complexity analysis
        // Time : O(2N)
        // Space : O(1)
    }

    void solve_counter(vector<int>& nums, int k) {
        // method 1 : brute force
        // method1_counter(nums, k);

        // method 2 :optimal
        method2_counter(nums, k);
    }

public:
    void rotate(vector<int>& nums, int k) {
        solve(nums, k);
    }
};

void p3() {
    // Problem 3 : Leetcode 189. Rotate Array - https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1 

    vector<int> nums = { 2, 5, 7, 6, 4, 2 };
    int k = 580;
    Problem3().rotate(nums, k);
    for (int e : nums) cout << e << " ";
    cout << endl;
}

class Problem4 {
    int solve(vector<int>& prices, int N) {
        int mprofit = 0;

        for (int i = 0; i < N; i++) {
            // buy at i, sell at j 
            for (int j = i + 1; j < N; j++) {
                int profit = prices[j] - prices[i];
                mprofit = max(mprofit, profit);
            }
        }

        return mprofit;

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(1) 
    }

    int dp(vector<int>& prices, int N) {
        int mprofit = 0;
        int min_price = 0; // last day of lowest price 

        // j = sell day 
        for (int j = 0; j < N; j++) {
            // if todays price is lower then last lowest price, then update last lowest price 
            if (prices[min_price] > prices[j]) min_price = j;

            // now calculate profit, buy price - selling price / profit 
            int profit = prices[j] - prices[min_price];
            mprofit = max(mprofit, profit); // update max profit 
        }

        return mprofit;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }

public:
    int maxProfit(vector<int>& prices) {
        int N = prices.size();
        // return brute(prices, N);
        return dp(prices, N);
    }
};

void p4() {
    // Problem 4 : Leetcode 121. Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/buy-stock-2/1 

    // vector<int> prices = { 4,3,2,1 };
    vector<int> prices = { 1,2,3,4 };
    cout << Problem4().maxProfit(prices) << endl;
}


int main() {
    // Day 2 of January 

    p1();

    p2();

    p3();

    p4();


    return 0;
}