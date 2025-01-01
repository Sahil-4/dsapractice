#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

vector<vector<int>> threeSum_solution1(vector<int>& nums) {
    set<vector<int>> st;

    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            for (int k = j + 1; k < nums.size(); k++) {
                if (nums[i] + nums[j] + nums[k] == 0) {
                    vector<int> tmp = {nums[i], nums[j], nums[k]};
                    sort(tmp.begin(), tmp.end());
                    st.insert(tmp);
                }
            }
        }
    }

    vector<vector<int>> ans(st.begin(), st.end());
    return ans;

    // !TLE 
    // T = O(n^3) 
    // S = O(2n) 
}

vector<vector<int>> threeSum_solution2(vector<int>& nums) {
    set<vector<int>> st;

    for (int i = 0; i < nums.size(); i++) {
        set<int> hashset;
        for (int j = i + 1; j < nums.size(); j++) {
            int need = -(nums[i] + nums[j]);

            if (hashset.find(need) != hashset.end()) {
                vector<int> tmp = {nums[i], nums[j], need};
                sort(tmp.begin(), tmp.end());
                st.insert(tmp);
            }

            hashset.insert(nums[j]);
        }
    }

    return {st.begin(), st.end()};

    // !TLE 
    // T = O(n ^ 2) 
    // S = O(2n) 
}

vector<vector<int>> threeSum(vector<int>& nums) {
    // sort the given array - n * log(n) 
    sort(nums.begin(), nums.end());

    vector<vector<int>> ans;
    int n = nums.size();

    for (int l = 0; l < n; l++) {
        if (l > 0 && nums[l] == nums[l - 1]) continue;

        int m = l + 1;
        int h = n - 1;

        while (m < h) {
            int sum = nums[l] + nums[m] + nums[h];

            if (sum == 0) {
                ans.push_back({nums[l], nums[m], nums[h]});

                m++;
                h--;

                while (m < h && nums[m] == nums[m - 1]) m++;
                while (h > m && nums[h] == nums[h + 1]) h--;
            } else if (sum < 0) {
                m++;
            } else {
                h--;
            }
        }
    }

    return ans;

    // T = O((n * log(n)) + (n^2)) 
    // S = O(1) 
}

void p1() {
    // Problem 1 : 3Sum - https://leetcode.com/problems/3sum/description/ 

    vector<int> nums = {};
    vector<vector<int>> ans = threeSum(nums);

    for (int i = 0; i < ans.size(); i++) {
        for (int j = 0; j < ans[i].size(); j++) {
            cout << ans[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    // Day 16 

    p1();


    return 0;
}