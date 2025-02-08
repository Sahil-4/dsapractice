#include <bits/stdc++.h>

using namespace std;

class Problem1 {
public:
    int search(vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (nums[mid] == target) {
                return mid;
            }
            else if (nums[low] <= nums[mid]) {
                if (nums[low] <= target && target <= nums[mid]) {
                    high = mid - 1;
                }
                else {
                    low = mid + 1;
                }
            }
            else {
                if (nums[mid] <= target && target <= nums[high]) {
                    low = mid + 1;
                }
                else {
                    high = mid - 1;
                }
            }
        }

        return -1;

        // Complexity analysis 
        // Time : O(Log(N)) 
        // Space : O(1) 
    }
};

void p1() {
    // Problem 1 : Leetcode 33. Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/search-in-a-rotated-array4618/1 

    vector<int> nums = { 18,1,3,6,12 };
    for (int e : nums) cout << e << " ";
    cout << endl;
    cout << 18 << "->" << Problem1().search(nums, 18) << endl;
    cout << 1 << "->" << Problem1().search(nums, 1) << endl;
    cout << 12 << "->" << Problem1().search(nums, 12) << endl;
    cout << 28 << "->" << Problem1().search(nums, 28) << endl;
    cout << 14 << "->" << Problem1().search(nums, 14) << endl;
    cout << 0 << "->" << Problem1().search(nums, 0) << endl;
}

class Problem2 {
    int firstOccurrence(vector<int>& arr, int target) {
        int low = 0, high = arr.size() - 1;
        int out = -1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (arr[mid] == target) {
                out = mid;
                high = mid - 1;
            }
            else if (arr[mid] < target) {
                low = mid + 1;
            }
            else {
                high = mid - 1;
            }
        }

        return out;
    }

    int lastOccurrence(vector<int>& arr, int target) {
        int low = 0, high = arr.size() - 1;
        int out = -1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (arr[mid] == target) {
                out = mid;
                low = mid + 1;
            }
            else if (arr[mid] < target) {
                low = mid + 1;
            }
            else {
                high = mid - 1;
            }
        }

        return out;
    }

public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int fo = firstOccurrence(nums, target);
        int lo = lastOccurrence(nums, target);
        return { fo, lo };

        // Complexity analysis 
        // Time : O(Log(N)) 
        // Space : O(1) 
    }
};

void p2() {
    // Problem 2 : Leetcode 34. Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1 

    vector<int> nums = { 1,3,3,5,6,6,6,7,12,12 };
    int target = 0;
    for (int e : nums) cout << e << " ";
    cout << endl;
    vector<int> out = Problem2().searchRange(nums, target);
    cout << target << " first -> " << out[0] << endl;
    cout << target << " last -> " << out[1] << endl;
}

class Problem3 {
public:
    int findMin(vector<int>& nums) {
        int low = 0, high = nums.size() - 1;

        while (low < high) {
            int mid = low + (high - low) / 2;
            (nums[mid] > nums[high]) ? low = mid + 1 : high = mid;
        }

        return nums[low];

        // Complexity analysis 
        // Time : O(Log(N)) 
        // Space : O(1) 
    }
};

void p3() {
    // Problem 3 : Leetcode 153. Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/minimum-element-in-a-sorted-and-rotated-array3611/1 

    vector<int> nums = { 18,1,3,6,12 };
    for (int e : nums) cout << e << " ";
    cout << endl;
    cout << Problem3().findMin(nums) << endl;
}

class Problem4 {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // apply binary search on smaller array 
        int m = nums1.size(), n = nums2.size();
        if (m > n) return findMedianSortedArrays(nums2, nums1);

        // search space 
        int low = 0, high = m;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            int px = low + (high - low) / 2; // elements from nums1 
            int py = (m + n + 1) / 2 - px; // elements from nums2 

            // left side last elements 
            int x1 = (px == 0) ? INT_MIN : nums1[px - 1];
            int x2 = (py == 0) ? INT_MIN : nums2[py - 1];

            // right side starting elements 
            int x3 = (px == m) ? INT_MAX : nums1[px];
            int x4 = (py == n) ? INT_MAX : nums2[py];

            if (x1 <= x4 && x2 <= x3) {
                if (m + n + 1 & 1) return (max(x1, x2) + min(x3, x4)) / 2.0;
                return max(x1, x2);
            }
            else if (x1 > x4) {
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
        }

        return 0;

        // Complexity analysis 
        // Time : O(Log(n)) 
        // Space : O(1) 
    }
};

void p4() {
    // Problem 4 : Leetcode 4. Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/median-of-2-sorted-arrays-of-different-sizes/1 

    vector<int> nums1 = { 1,2,3,5 };
    vector<int> nums2 = { 4,6,8 };
    cout << Problem4().findMedianSortedArrays(nums1, nums2) << endl;
}


int main() {
    // Day 8 of February 

    p1();

    p2();

    p3();

    p4();


    return 0;
}