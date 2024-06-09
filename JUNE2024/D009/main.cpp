#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;

int maxSubArray_Solution1(vector<int>& nums) {
    int n = nums.size();
    int sum = 0;

    for (int startIndex = 0; startIndex < n; startIndex++) {
        int tempSum = 0;

        for (int endIndex = startIndex; endIndex < n; endIndex++) {
            tempSum += nums[endIndex];

            if (tempSum > sum) sum = tempSum;
        }
    }

    return sum;

    // Complexity 
    // Time : O(n * n) 
    // Space : O(1) 
}

int maxSubArray(vector<int>& nums) {
    int sum = INT_MIN;
    int tempSum = 0;

    int start = 0, end = 0;

    while (end < nums.size()) {
        tempSum += nums[end];

        if (tempSum > sum) sum = tempSum;
        while (tempSum < 0) tempSum -= nums[start++];

        end++;
    }

    return sum;

    // Complexity 
    // Time : O(2n) 
    // Space : O(1) 
}

void p1() {
    // Problem 1 : Leetcode 53. Maximum Subarray - https://leetcode.com/problems/maximum-subarray/description/ 

    vector<int> nums = {};
    int s = maxSubArray(nums);
    cout << "maxSubArray :: " << s << endl;
}

int getSum(int a[], int s, int e) {
    int sum = 0;
    for (s; s <= e; s++) sum += a[s];
    return sum;
}

vector<int> findSubarray_Solution1(int a[], int n) {
    // code here
    vector<pair<int, int>> pairs;

    // create index pairs of subarrays without negative numbers 
    int l = 0, h = 0;
    while (h < n) {
        if (a[h] < 0 && h > 0) {
            pairs.push_back({l, h - 1});
            h++;
            l = h;
            continue;
        }
        h++;
    }
    pairs.push_back({l, h - 1});

    int gtSum = 0;
    pair<int, int> ansRange;
    // find sum of each pair index range, and update largest sum 
    for (int i = 0; i < pairs.size(); i++) {
        int temp = getSum(a, pairs[i].first, pairs[i].second);
        if (temp > gtSum || (temp == gtSum && (ansRange.second - ansRange.first) < (pairs[i].second - pairs[i].first))) {
            gtSum = temp;
            ansRange = pairs[i];
        }
    }

    vector<int> out;
    for (int i = ansRange.first; i <= ansRange.second; i++) out.push_back(a[i]);
    return out;
    
    // Complexity 
    // Time : O(n*n) 
    // Space : O(n/2), O(n) 
}

vector<int> findSubarray(int a[], int n) {
    // code here
    vector<int> out;
    int s = -1, e = -1;
    int sum = 0;

    int tSum = 0;
    int l = 0, h = 0;
    while (h < n) {
        if (a[h] < 0) {
            if ((tSum > sum) || ((tSum == sum) && ((e - s) < (h - l - 1)))) {
                sum = tSum;
                s = l, e = h - 1;
            }

            h++, l = h;
            tSum = 0;
            continue;
        }

        tSum += a[h];
        h++;
    }

    if ((tSum > sum) || ((tSum == sum) && ((e - s) < (h - l - 1)))) {
        sum = tSum;
        s = l, e = h - 1;
    }

    if (e == -1) return { -1 };

    for (s; s <= e; s++) out.push_back(a[s]);

    return out;

    // Complexity 
    // Time : O(2n) 
    // Space : O(1) 
}

void p2() {
    // Problem 2 : GeeksForGeeks Maximum Sub Array - https://www.geeksforgeeks.org/problems/maximum-sub-array5443/1 

    int a[] = {1, 2, 5, -7, 2, 3};
    int n = 6;

    vector<int> sub = findSubarray(a, n);
    cout << "sub arr :: ";
    for (int i = 0; i < sub.size(); i++) cout << sub[i] << " ";
    cout << endl;
}


int main() {
    // Day 9 

    p1();

    p2();


    return 0;
}