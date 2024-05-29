#include <iostream>
#include <vector>
#include <map>

using namespace std;

int numberOfSubarrays_Solution1(vector<int>& nums, int k) {
    int niceSubarraysCount = 0;
    int arrSize = nums.size();

    for (int i = 0; i < arrSize; i++) {
        int oddsCount = 0;

        for (int j = i; j < arrSize; j++) {
            if (nums[j] & 1) oddsCount++;
            if (oddsCount == k) niceSubarraysCount++;
            if (oddsCount > k) break;
        }
    }

    return niceSubarraysCount;

    // Complexity analysis 
    // TIme : O(n ^ 2) 
    // Space : O(1) 
}

int numberOfSubarrays_Solution2(vector<int>& nums, int k) {
    int niceSubarraysCount = 0;

    int oddsCount = 0;
    map<int, pair<int, int>> mp = {{0, {-1, -1}}};

    for (int r = 0; r < nums.size(); r++) {
        if (nums[r] & 1) oddsCount++;
        int need = oddsCount - k;

        if (mp.find(need) != mp.end()) niceSubarraysCount += mp[need].second - mp[need].first + 1;

        if (mp.find(oddsCount) != mp.end()) mp[oddsCount].second = r;
        else mp[oddsCount] = {r, r};
    }

    return niceSubarraysCount;

    // Complexity analysis 
    // Time : O(n) 
    // Space : O(n) 
}

int numberOfSubarrays(vector<int>& nums, int k) {
    int n = nums.size();
    int niceSubarraysCount = 0;

    int oddsCount = 0;
    int evens = 0;
    int l = 0, r = 0;

    while (r < n) {
        if (nums[r] & 1) oddsCount++;

        while (l < r && (!(nums[l] & 1) || oddsCount > k)) {
            if (nums[l] & 1) evens = 0, oddsCount--;
            else evens++;

            l++;
        }

        if (oddsCount == k) niceSubarraysCount += 1 + evens;

        r++;
    }

    return niceSubarraysCount;

    // Complexity analysis 
    // Time : O(n) 
    // Space : O(1) 
}

void p1() {
    // Problem 1 : Leetcode 1248. Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/count-subarray-with-k-odds/1 

    vector<int> nums = {1, 2, 1, 5, 6, 2, 2, 2, 1};
    int k = 3;

    int subArrs = numberOfSubarrays(nums, k);
    cout << "subArrs :: " << subArrs << endl;
}


int main() {
    // Day 29 

    p1();


    return 0;
}