#include <bits/stdc++.h>

using namespace std;


class Problem1 {
    int brute(vector<int>& height) {
        int maxWater = 0;

        for (int i = 0; i < height.size(); i++) {
            int a = height[i], ai = i;
            for (int j = 0; j < height.size(); j++) {
                int b = height[j], bi = j;
                int water = abs(ai - bi) * min(a, b);
                maxWater = max(maxWater, water);
            }
        }

        return maxWater;

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(1) 
    }

    int better(vector<int>& height) {
        int N = height.size();

        int mwater = 0;

        int i = 0, j = N - 1;

        while (i < j) {
            // get ai, bi, ae, be 
            int ai = i, ae = height[i];
            int bi = j, be = height[j];

            // calculate water that can be stored 
            int water = abs(i - j) * min(ae, be);
            mwater = max(mwater, water);

            // update pointers 
            if (ae <= be) i++;
            else j--;
        }

        return mwater;

        // Complexity analysis 
        // Time : O(N)  
        // Space : O(1) 
    }

public:
    int maxArea(vector<int>& height) {
        // return brute(height);

        return better(height);
    }
};

void p1() {
    // Problem 1 : Leetcode 11. Container With Most Water - https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/container-with-most-water0535/1 

    // vector<int> height = {1,8,6,2,5,4,8,3,7};
    // vector<int> height = {1,5,1,1,1};
    // vector<int> height = {1,2,8,1,1,1,1,1,2};
    // vector<int> height = {1,1,2,1,1,1,1,8,2};
    // vector<int> height = {1, 1, 2, 1, 1, 1, 1, 8, 2, 1, 1, 2, 1};
    // vector<int> height = {1, 1, 2, 1, 1, 1, 1, 2, 8, 2, 1};
    vector<int> height = { 1, 1, 2, 8, 1, 1, 1, 2, 1, 2, 1 };
    cout << Problem1().maxArea(height) << endl;
}

class Problem2 {
    vector<vector<int>> brute(vector<int>& nums) {
        set<vector<int>> out;

        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < nums.size(); j++) {
                for (int k = 0; k < nums.size(); k++) {
                    if (i == j || j == k || k == i) continue;

                    int sum = nums[i] + nums[j] + nums[k];
                    if (sum == 0) {
                        vector<int> idxs = { nums[i], nums[j], nums[k] };
                        sort(idxs.begin(), idxs.end());
                        out.insert(idxs);
                    }
                }
            }
        }

        return { out.begin(), out.end() };

        // Ccomplexity analysis 
        // Time : O(N^3) 
        // Space : O(N) 
    }

    vector<vector<int>> better(vector<int> nums) {
        sort(nums.begin(), nums.end());

        vector<vector<int>> out;
        int N = nums.size();

        for (int i = 0; i < N; i++) {
            // skip duplicates 
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int l = i + 1, r = N - 1;

            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];

                if (sum == 0) {
                    out.push_back({ nums[i], nums[l], nums[r] });
                    l++, r--;

                    // possible that duplicates are in between 
                    while (l < r && nums[l] == nums[l - 1]) l++;
                    while (r > l && nums[r] == nums[r + 1]) r--;
                }
                else if (sum < 0) l++;
                else r--;
            }
        }

        return out;

        // Ccomplexity analysis 
        // Time : O(N*Log(N)) + O(N^2) 
        // Space : O(N) 
    }

public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // return brute(nums);

        return better(nums);
    }
};

void p2() {
    // Problem 2 : Leetcode 15. 3Sum - https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1 

    vector<int> nums = { -1,0,1,2,-1,-4 };
    vector<vector<int>> out = Problem2().threeSum(nums);
    for (vector<int> v : out) {
        for (int e : v) cout << e << " ";
        cout << endl;
    }
}


int main() {
    // Day 9 of January 2025 

    p1();

    p2();


    return 0;
}