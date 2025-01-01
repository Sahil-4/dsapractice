#include <bits/stdc++.h>

using namespace std;

int findContentChildren(vector<int> gf, vector<int> cs) {
    // taking input by value as we dont want to modify real input set 
    // we can reduce memory if we perform operation (sorting) on actual dataset 

    // sort greed factor and cookies size 
    sort(gf.begin(), gf.end());
    sort(cs.begin(), cs.end());

    // create two pointers - p1 for greed, p2 for cookies 
    int p1 = 0, G = gf.size();
    int p2 = 0, C = cs.size();

    // perform two pointer 
    while (p1 < G && p2 < C) {
        // check can we assign p2 cookie to p1 child 
        if (gf[p1] <= cs[p2]) p1++; // assign cookie 
        p2++; // this cookie can not be used for next childs 
    }

    return p1; // number of childs whose greed factor is satisfied 

    // Complexity analysis 
    // Time : O(G * Log(G)) + O(C * Log(C)) + O(min(G, C)) 
    // Space : O(G) + O(C) 
}

void p1() {
    // Problem 1 : Leetcode 455. Assign Cookies - https://leetcode.com/problems/assign-cookies/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/assign-cookies/0 

    cout << findContentChildren({ 1,2,3 }, { 1,1 }) << endl;
}

int recursion(vector<int>& nums, int N, int target, int index, int result) {
    if (index == N) return (target == result);

    // two possibilities 
    int p = recursion(nums, N, target, index + 1, result + nums[index]);
    int m = recursion(nums, N, target, index + 1, result - nums[index]);

    return p + m;

    // Complexity analysis 
    // Time : O(2^N) 
    // Space : O(N) depth 
}

int memoize(vector<int>& nums, int N, int target, int index, int result, vector<vector<int>>& dp) {
    if (index == N) return (target == result);

    if (dp[index][result + 1000] != -1) return dp[index][result + 1000];

    // two possibilities 
    int p = memoize(nums, N, target, index + 1, result + nums[index], dp);
    int m = memoize(nums, N, target, index + 1, result - nums[index], dp);

    return dp[index][result + 1000] = p + m;

    // Complexity analysis 
    // Time : O(2*2*N) 
    // Space : O(N) depth + O(N * 2001) memory 
}

int findTargetSumWays(vector<int> nums, int target) {
    int N = nums.size();

    // return recursion(nums, nums.size(), target, 0, 0);

    vector<vector<int>> dp(N, vector<int>(2001, -1));
    return memoize(nums, N, target, 0, 0, dp);
}

void p2() {
    // Problem 2 : Leetcode 494. Target Sum - https://leetcode.com/problems/target-sum/ 

    cout << findTargetSumWays({ 2,6,8,4,6,1 }, 12) << endl;
}

int main() {
    // Day 18 of December 

    p1();

    p2();


    return 0;
}
