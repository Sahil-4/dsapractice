#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

int subarraysWithKDistinct_Solution1(vector<int>& nums, int k) {
    int count = 0;

    for (int i = 0; i < nums.size(); i++) {
        set<int> st;

        for (int j = i; j < nums.size(); j++) {
            st.insert(nums[j]);
            if (st.size() == k) count++;
            if (st.size() > k) break;
        }
    }

    return count;

    // Complexity analysis 
    // Time : O(n ^ 2) 
    // Space : O(n) 
}

int solve(vector<int>& nums, int k) {
    if (k == 0) return 0;

    int count = 0;
    map<int, int> elementsCount; // element : count 

    for (int l = 0, r = 0; r < nums.size(); r++) {
        // push current element with its count 
        elementsCount[nums[r]]++;

        // if size is more then k, remove first element from left 
        while (elementsCount.size() > k) {
            elementsCount[nums[l]]--;
            if (elementsCount[nums[l]] == 0) elementsCount.erase(nums[l]);
            l++;
        }

        // if size is exactly or less then k then increase count by 1 
        if (elementsCount.size() <= k) count += (r - l + 1);
    }

    return count;

    // Complexity analysis 
    // Time : O(2(n * log(n))) 
    // Space : O(n) 
}

int solve_2(vector<int>& nums, int n, int k) {
    // GFG - TLE : n*log(n) 
    if (k == 0) return 0;

    int count = 0;

    int elementsCount[n + 1] = {0}; // element : count 212
    int arrSize = 0;

    for (int l = 0, r = 0; r < n; r++) {
        // push current element with its count 
        elementsCount[nums[r]]++;
        if (elementsCount[nums[r]] == 1) arrSize++;

        // if size is more then k, remove first element from left 
        while (arrSize > k) {
            elementsCount[nums[l]]--;
            if (elementsCount[nums[l]] == 0) arrSize--;
            l++;
        }

        // if size is exactly or less then k then increase count by 1 
        count += (r - l + 1);
    }

    return count;

    // Complexity analysis 
    // Time : O(2n) 
    // Space : O(n) 
}

int subarraysWithKDistinct(vector<int>& nums, int k) {
    int a = solve(nums, k);
    int b = solve(nums, k-1);
    return a - b;

    // Complexity analysis 
    // Time : O(4(n * log(n))) 
    // Space : O(2n) 
}

void p1() {
    // Problem 1 : Leetcode 992. Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/subarrays-with-k-different-integers/1 

    vector<int> nums = {1, 1, 2, 2, 1, 2, 1, 3, 2, 1, 5, 1, 2, 2, 3};
    int k = 2;

    int subArrCount = subarraysWithKDistinct(nums, k);
    cout << "subArrCount :: " << subArrCount << endl;
}

int main() {
    // Day 153, Day 1 of June 

    p1();


    return 0;
}