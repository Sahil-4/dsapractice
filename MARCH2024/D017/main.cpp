#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>

using namespace std;

vector<vector<int>> fourSum(vector<int>& nums, int target) {
    // sort the array 
    sort(nums.begin(), nums.end());

    // array to store answer 
    vector<vector<int>> ans;
    int n = nums.size();

    for (int i = 0; i < n; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;

        for (int j = i + 1; j < n; j++) {
            if (j != i + 1 && nums[j] == nums[j - 1]) continue;

            int k = j + 1, l = n - 1;
            while (k < l) {
                long long sum = nums[i];
                sum += nums[j];
                sum += nums[k];
                sum += nums[l];

                if (sum == target) {
                    ans.push_back({nums[i], nums[j], nums[k], nums[l]});
                    k++;
                    l--;
                    while(k < l && nums[k - 1] == nums[k]) k++;
                    while(k < l && nums[l + 1] == nums[l]) l--;
                } else if (sum < target) {
                    k++;
                } else {
                    l--;
                }
            }
        }
    }

    return ans;
}

void p1() {
    // Problem 1 : 4Sum - https://leetcode.com/problems/4sum 

    vector<int> arr = {2,2,2,2,2};
    // vector<int> arr = {1,2,3,4,5};
    int target = 10;

    // get answer and print 
    vector<vector<int>> ans = fourSum(arr, target);
    for (int i = 0; i < ans.size(); i++) {
        for (int j = 0; j < ans[i].size(); j++) {
            cout << ans[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    // Day 17 

    p1();


    return 0;
}