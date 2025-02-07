#include <bits/stdc++.h>

using namespace std;

class Problem1 {
public:
    int searchInsert(vector<int>& nums, int target) {
        // Approach : 
        // perform normal binary search 
        // while shrinking search space make sure to save/update potential answer 

        int low = 0, high = nums.size() - 1;
        int out = -1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (nums[mid] == target) {
                out = mid;
                break;
            }
            else if (nums[mid] > target) {
                high = mid - 1;
                out = mid;
            }
            else {
                low = mid + 1;
                out = mid + 1;
            }
        }

        return out;

        // Complexity analysis 
        // Time : O(log(N)) 
        // Space : O(1) 
    }
};

void p1() {
    // Problem 1 : Leetcode 35. Search Insert Position - https://leetcode.com/problems/search-insert-position/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/search-insert-position-of-k-in-a-sorted-array/1 

    // vector<int> nums = {0};
    // vector<int> nums = {2};
    vector<int> nums = { 5 };
    int target = 2;

    for (int e : nums) cout << e << " ";
    cout << endl;

    cout << Problem1().searchInsert(nums, target) << endl;
}

class Problem2 {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // intuition : treat it like 1D array 
        // as the entire array is sorted 
        // we can put the i+1th row at the end of ith row while maintaining sorted form 

        int R = matrix.size(), C = matrix[0].size();

        int low = 0, high = R * C - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            int r = mid / C, c = mid % C;

            if (matrix[r][c] == target) return true;
            else if (matrix[r][c] < target) low = mid + 1;
            else high = mid - 1;
        }

        return false;

        // Complexity analysis 
        // Time : O(log(R*C)) 
        // Space : O(1) 
    }
};

void p2() {
    // Problem 2 : Leetcode 74. Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/search-in-a-matrix17201720/1 

    vector<vector<int>> matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {12, 13, 18},
    };
    int target = 12;

    for (vector<int> v : matrix) {
        for (int e : v) cout << e << " ";
        cout << endl;
    }
    cout << Problem2().searchMatrix(matrix, target) << endl;
}

class Problem3 {
public:
    int findPeakElement(vector<int>& nums) {
        int N = nums.size();
        int low = 0, high = N - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if ((mid == 0 || nums[mid] > nums[mid - 1]) && (mid == N - 1 || nums[mid] > nums[mid + 1])) {
                return mid;
            }
            else if ((mid == 0 || nums[mid] > nums[mid - 1]) && (mid == N - 1 || nums[mid] < nums[mid + 1])) {
                low = mid + 1;
            }
            else {
                high = mid - 1;
            }
        }

        return N - 1;

        // Complexity analysis 
        // Time : O(log(N)) 
        // Space : O(1) 
    }
};

void p3() {
    // Problem 3 : Leetcode 162. Find Peak Element - https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/peak-element/1 

    // vector<int> nums = {1};
    // vector<int> nums = { 1,2,3 };
    vector<int> nums = { 1,2,1 };
    vector<int> nums = { 1,2,1,2,5,6 };

    for (int e : nums) cout << e << " ";
    cout << endl;

    cout << Problem3().findPeakElement(nums) << endl;
}


int main() {
    // Day 7 of February 

    p1();

    p2();

    p3();


    return 0;
}