#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    int solve1(vector<int>& nums, int k) {
        // -------- Sorting -------- 
        int n = nums.size();

        sort(nums.begin(), nums.end());

        return nums[n - k];

        // Complexity analysis 
        // Time : O(N*Log(N)) 
        // Space : O(1) + modifying input data 
    }

    int solve2(vector<int>& nums, int k) {
        // -------- Priority Queue -------- 
        // priority_queue<int, list<int>, greater<int>> pq;
        priority_queue<int> pq;

        for (int e : nums) {
            pq.push(e);
        }

        int out = 0;

        for (int i = 0; i < k; i++) {
            out = pq.top(); pq.pop();
        }

        return out;

        // Complexity analysis 
        // Time : O(N*Log(N)) + O(K) 
        // Space : O(N) 
    }

    int solve3(vector<int>& nums, int k) {
        // -------- Max Heap -------- 
        priority_queue<int, vector<int>, greater<int>> pq;

        for (int e : nums) {
            pq.push(e);
            if (pq.size() > k) pq.pop();
        }

        return pq.top();

        // Complexity analysis 
        // Time : O(K*Log(K)) 
        // Space : O(K) 
    }

public:
    int findKthLargest(vector<int>& nums, int k) {
        // return solve1(nums, k);

        // return solve2(nums, k);

        return solve3(nums, k);
    }
};

void p1() {
    // Problem 1 : Leetcode 215. Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/k-largest-elements4206/1 

    vector<int> nums = { 3,2,1,5,6,4 };
    cout << Problem1().findKthLargest(nums, 1) << endl;
    cout << Problem1().findKthLargest(nums, 2) << endl;
    cout << Problem1().findKthLargest(nums, 5) << endl;
}

struct Project {
    int profit;
    int capital;

    Project(int profit, int capital) {
        this->profit = profit;
        this->capital = capital;
    }
};

struct Compare {
    bool operator()(const Project& p1, const Project& p2) {
        return (p1.capital != p2.capital) ? p1.capital < p2.capital
            : p1.profit < p2.profit;
    }
};

class Problem2 {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        int n = profits.size();

        vector<Project> vec;

        for (int i = 0; i < n; i++) {
            vec.push_back({ profits[i], capital[i] });
        }

        sort(vec.begin(), vec.end(), Compare());

        priority_queue<int> pq;
        int i = 0;

        while (k--) {
            while (i < n && vec[i].capital <= w) {
                pq.push(vec[i].profit);
                i++;
            }

            if (pq.empty()) break;

            w += pq.top();
            pq.pop();
        }

        return w;
    }
};

void p2() {
    // Problem 2 : Leetcode 502. IPO - https://leetcode.com/problems/ipo/description/?envType=study-plan-v2&envId=top-interview-150 

    int k = 2, w = 0;
    vector<int> profits = { 1,2,3 }, capital = { 0,1,1 };
    cout << Problem2().findMaximizedCapital(k, w, profits, capital) << endl;
}


int main() {
    // Day 9 of February 

    p1();

    p2();


    return 0;
}