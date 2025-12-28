#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    int brute(vector<int>& nums, int target) {
        int msubsize = INT_MAX;
        int N = nums.size();

        for (int i = 0; i < N; i++) {
            int sum = 0;
            for (int j = i; j < N; j++) {
                sum += nums[j];
                if (sum >= target) {
                    msubsize = min(msubsize, j - i + 1);
                    break;
                }
            }
        }

        return msubsize == INT_MAX ? 0 : msubsize;

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(1) 
    }

    int better(vector<int>& nums, int target) {
        int msubsize = INT_MAX;
        int N = nums.size();

        int i = 0, j = 0;
        int sum = 0;

        while (j < N) {
            sum += nums[j];
            while (sum >= target) {
                msubsize = min(msubsize, j - i + 1);
                sum -= nums[i];
                i++;
            }
            j++;
        }

        return msubsize == INT_MAX ? 0 : msubsize;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }

    bool subArrayExists(vector<int>& nums, int target, int windowLen) {
        int N = nums.size();

        int sum = 0;

        // first window 
        for (int l = 0; l < windowLen; l++) sum += nums[l];

        // all windows after first window 
        for (int l = 0, r = windowLen; r < N && sum < target; l++, r++) {
            sum -= nums[l];
            sum += nums[r];
        }

        return sum >= target;
    }

    int binary_search(vector<int>& nums, int target) {
        int N = nums.size();
        int low = 1, high = N;

        int msubsize = INT_MAX;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            bool check = subArrayExists(nums, target, mid);

            if (check) high = mid - 1, msubsize = mid;
            else low = mid + 1;
        }

        return msubsize == INT_MAX ? 0 : msubsize;

        // Complexity analysis 
        // Time : O(N * Log(N)) 
        // Space : O(1) 
    }

public:
    int minSubArrayLen(int target, vector<int>& nums) {
        // return brute(nums, target);

        // return better(nums, target);

        return binary_search(nums, target);
    }
};

void p1() {
    // Problem 1 : Leetcode 209. Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1 

    vector<int> nums = { 2,3,1,2,4,3 };
    int target = 7;
    cout << Problem1().minSubArrayLen(target, nums) << endl;
}

class Problem2 {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> map; // we will store char freq in this map 

        int len = 0;

        for (int l = 0, r = 0; r < s.length(); r++) {
            while (l < r && map[s[r]] != 0) map[s[l++]]--;
            map[s[r]]++;
            len = max(len, r - l + 1);
        }

        return len;

        // Complexity analysis 
        // Time : O(2N) 
        // Space : O(1) 
    }
};

void p2() {
    // Problem 2 : Leetcode 3. Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/length-of-the-longest-substring3036/1 

    cout << Problem2().lengthOfLongestSubstring("") << endl;
}


int main() {
    // Day 10 of January 2025 

    p1();

    p2();


    return 0;
}