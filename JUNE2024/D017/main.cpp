#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;

pair<int, double> checkPartitionCorrect(vector<int>& nums1, vector<int>& nums2, int m, int n, int en1, int en2) {
    // return 
    // { 0, median} : correct partition 
    // { 1, 0} : decrease number of elements taken from nums1 
    // {-1, 0} : increase number of elements taken from nums1 

    // elements taken in left array from nums1 = en1 
    // elements taken in left array from nums2 = en2 

    // end elements of left half 
    int y1 = en1 == 0 ? INT_MIN : nums1[en1 - 1];
    int z1 = en2 == 0 ? INT_MIN : nums2[en2 - 1];

    // starting elements of right half 
    int y2 = en1 == m ? INT_MAX : nums1[en1];
    int z2 = en2 == n ? INT_MAX : nums2[en2];

    // cross checking 
    if (y1 <= z2 && z1 <= y2) {
        // correct partition 
        // now find the median and return it 
        if ((m + n) & 1) return {0, max(y1, z1)};
        return {0, (max(y1, z1) + min(y2, z2)) / 2.0};
    }

    if (y1 > z2) return {1, 0};
    else return {-1, 0};

    // O(1) 
}

double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    int m = nums1.size(), n = nums2.size();

    // keep nums1 small and nums2 bigger 
    if (m > n) return findMedianSortedArrays(nums2, nums1);

    int low = 0, high = m;
    int mid = low + (high - low) / 2; // num of elements to be taken from nums 1 

    while (low <= high) {
        pair<int, double> check = checkPartitionCorrect(nums1, nums2, m, n, mid, (m + n + 1) / 2 - mid);

        if (check.first == 0) return check.second;
        else if (check.first == -1) low = mid + 1;
        else high = mid - 1;

        mid = low + (high - low) / 2;
    }

    return -1;

    // Complexity analysis 
    // Time : O(log(min(m, n))) 
    // Space : O(1) 
}

void p1() {
    // Problem 1 : Leetcode 4. Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/ 
    // GeeksForGeeks - https://www.geeksforgeeks.org/problems/median-of-2-sorted-arrays-of-different-sizes/1 

    vector<int> arr1 = {1, 2, 3, 5, 12};
    vector<int> arr2 = {3, 4, 8, 12};

    int med = findMedianSortedArrays(arr1, arr2);
    cout << "med :: " << med << endl;
}

int main() {
    // Day 17 

    p1();


    return 0;
}