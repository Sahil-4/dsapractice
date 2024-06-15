#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

vector<vector<int>> fourSum(vector<int>& nums, int target) {
    sort(nums.begin(), nums.end());
    set<vector<int>> st;
    int n = nums.size();

    for (int a = 0; a < n - 3; a++) {
        for (int b = a + 1; b < n - 2; b++) {
            long long sumTillNow = nums[a] + nums[b];

            int l = b + 1, h = n - 1;

            while (l < h) {
                long long sum = sumTillNow + nums[l] + nums[h];
                if (sum == target) {
                    st.insert({ nums[a], nums[b], nums[l], nums[h] });
                    l++, h--;
                }
                else if (sum < target) l++;
                else h--;
            }
        }
    }

    return {st.begin(), st.end()};

    // Complexity : 
    // Time : O(n ^ 3) 
    // Space : O(n) 
    // space can be further optimised by discarding duplicate elements once they have considered 
}

void p1() {
    // Problem 1 : Leetcode 18. 4Sum - https://leetcode.com/problems/4sum/description/ 
    // GeeksForGeeks - https://www.geeksforgeeks.org/problems/find-all-four-sum-numbers1732/1 

    vector<int> arr = {2, 1, 0, 2, 0, -2, -1};
    int target = 0;
    vector<vector<int>> ans = fourSum(arr, target);
}

int findMax(vector<int> &piles) {
    int maxi = piles[0];
    for (int i = 1; i < piles.size(); i++) maxi = max(maxi, piles[i]);
    return maxi;
}

bool canConsume(vector<int>& piles, int h, int k) {
    // true : if valid answer, able to consume in h hours, save answer, update h 
    // false : if unable to consume within h hours, update l 
    int hours = 0;

    for (int i = 0; i < piles.size(); i++) {
        hours += piles[i] / k;
        if ((piles[i] % k) > 0) hours += 1;

        if (hours > h) return false;
    }

    return true;
}

int minEatingSpeed(vector<int>& piles, int h) {
    // search space 
    int low = 1, high = findMax(piles);
    int mid = low + (high - low) / 2;

    // answer 
    int ans = high;

    while (low <= high) {
        bool out = canConsume(piles, h, mid);

        if (out) ans = min(ans, mid), high = mid - 1;
        else low = mid + 1;

        mid = low + (high - low) / 2;
    }

    return ans;
}

void p2() {
    // Problem 2 : Leetcode 875. Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/description/ 
    // GeeksForGeeks - https://www.geeksforgeeks.org/problems/koko-eating-bananas/1 

    vector<int> piles = {3,6,7,11};
    int h = 8;

    int k = minEatingSpeed(piles, h);
    cout << "k :: " << k << endl;
}


int main() {
    // Day 15 

    p1();

    p2();


    return 0;
}