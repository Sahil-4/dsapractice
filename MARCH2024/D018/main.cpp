#include <iostream>
#include <vector>

using namespace std;

int reversePairs_solution1(vector<int>& nums) {
    int count = 0;

    for (int i = 0; i  < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[i] > (long long) nums[j] * 2) count++;
        }
    }

    return count;

    // !TLE 
    // T = O(n ^ 2) 
    // S = O(1)
}

void merge(vector<int>& nums, int l, int m, int h) {
    vector<int> temp;

    int l1 = l;
    int r1 = m + 1;

    while (l1 <= m && r1 <= h) {
        if (nums[l1] <= nums[r1]) temp.push_back(nums[l1++]);
        else temp.push_back(nums[r1++]);
    }

    while (l1 <= m) temp.push_back(nums[l1++]);
    while (r1 <= h) temp.push_back(nums[r1++]);

    int a = l;
    for (int b = 0; b < temp.size(); b++) nums[a++] = temp[b];
}

int countPairs(vector<int>& nums, int l, int m, int h) {
    int count = 0;

    int r = m + 1;
    for (int i = l; i <= m; i++) {
        while (r <= h && nums[i] > (long long) nums[r] * 2) r++;
        count += r - (m + 1);
    }

    return count;
}

int mergeSort(vector<int>& nums, int l, int h) {
    int count = 0;

    if (l >= h) return count;

    int m = l + (h - l) / 2;

    count += mergeSort(nums, l, m);
    count += mergeSort(nums, m + 1, h);
    count += countPairs(nums, l, m, h);
    merge(nums, l, m, h);

    return count;
}

int reversePairs(vector<int>& nums) {
    return mergeSort(nums, 0, nums.size() - 1);
}

void p1() {
    // Problem 1 : Reverse pairs - https://leetcode.com/problems/reverse-pairs/  

    // vector<int> nums = {1,3,2,3,1};
    vector<int> nums = {2,4,3,5,1};
    // vector<int> nums = {2147483647,2147483647,2147483647,2147483647,2147483647,2147483647};
    // vector<int> nums = {2147483647,2147483647,-2147483647,-2147483647,-2147483647,2147483647};

    int c1 = reversePairs_solution1(nums);
    cout << c1 << endl;

    int c = reversePairs(nums);
    cout << c << endl;
}


int main() {
    // Day 18 of March total Day 78th 

    p1();


    return 0;
}