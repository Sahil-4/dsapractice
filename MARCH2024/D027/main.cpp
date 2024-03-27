#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void combine_sort(vector<int>& arr1, vector<int>& arr2) {
    // code here 
    // gap technique - derived from shell sort 
    int n = arr1.size(), m = arr2.size();
    int t_len = n + m;
    int gap = (t_len / 2) + (t_len % 2);

    // Tc = O(log(n + m))
    while (gap > 0) {
        int l = 0;
        int r = gap;

        // Tc = O(n + m)
        while (r < t_len) {
            if (l < n && r < n) {
                // l is on arr1 and r is also on arr1 
                if (arr1[l] > arr1[r]) swap(arr1[l], arr1[r]);
            } else if (l >= n && r >= n) {
                // l is on arr2 and r is also on arr2 
                if (arr2[l - n] > arr2[r - n]) swap(arr2[l - n], arr2[r - n]);
            } else {
                // l is on arr1 and r is on arr2 
                if (arr1[l] > arr2[r - n]) swap(arr1[l], arr2[r - n]);
            }

            // it is not possible that l is on arr2 and r is also on arr1 

            // update pointers 
            l++;
            r++;
        }

        // update gap 
        if (gap == 1) break;
        gap = (gap / 2) + (gap % 2);
    }

    // Tc = O((n+m) * log(n + m)) 
    // Space = 1 
}

double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    combine_sort(nums1, nums2);

    int n = nums1.size(), m = nums2.size();
    int t_len = n + m;
    int i = t_len / 2;

    float med = 0;

    if (t_len & 1) {
        if (i < n) med = nums1[i];
        else med = nums2[i - n];
    } else {
        if (i < n) med = (double) (nums1[i] + nums1[i - 1]) / 2;
        else if (i == n) med = (double) (nums2[i - n] + nums1[i - 1]) / 2;
        else med = (double) (nums2[i - n] + nums2[i - n - 1]) / 2;
    }

    return med;
}

void p1() {
    // P1 LC 4. Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/ 

    // vector<int> nums1 = {1, 3};
    // vector<int> nums2 = {2};
    // vector<int> nums1 = {1, 3};
    // vector<int> nums2 = {3, 2};
    vector<int> nums1 = {1, 2};
    vector<int> nums2 = {3, 4};

    double m = findMedianSortedArrays(nums1, nums2);
    cout << m << endl;
}

vector<int> rowAndMaximumOnes_solution1(vector<vector<int>>& mat) {
    int r_index = 0;
    int r_row_ones = 0;

    for (int r = 0; r < mat.size(); r++) {
        int ones = 0;

        for (int c = 0; c < mat[r].size(); c++) if (mat[r][c] == 1) ones++;

        if (ones > r_row_ones) r_index = r, r_row_ones = ones;
    }

    return {r_index, r_row_ones};
}

int firstOne(vector<int> row) {
    int l = 0, h = row.size() - 1;
    int m = l + (h - l) / 2;

    while (l <= h) {
        if (row[m] == 1) h = m - 1;
        else l = m + 1;

        m = l + (h - l) / 2;
    }

    return l;
}

vector<int> rowAndMaximumOnes(vector<vector<int>>& mat) {
    // sort each row 
    for (int i = 0; i < mat.size(); i++) sort(mat[i].begin(), mat[i].end());

    int index = 0;
    int ones_count = 0;

    for (int i = 0; i < mat.size(); i++) {
        int idx = firstOne(mat[i]);
        int ones = mat[i].size() - idx;

        if (ones > ones_count) index = i, ones_count = ones;
    }

    return {index, ones_count};
}

void p2() {
    // P2 LC 2643. Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/ 

    // vector<vector<int>> mat = {{0,1},{1,0}};
    vector<vector<int>> mat = {{0, 0, 0,1, 1},{0, 0, 1, 1,1}};
    vector<int> ans = rowAndMaximumOnes(mat);

    cout << "row number : " << ans[0] << endl;
    cout << "zeroes : " << ans[1] << endl;
}

int main() {
    // Day 27 

    p1();

    p2();


    return 0;
}