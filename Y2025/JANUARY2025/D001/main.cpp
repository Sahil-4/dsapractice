#include <bits/stdc++.h>

using namespace std;


class Problem1 {
    void brute_force(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        for (int e : nums2) {
            // put e at correct place in nums1
            int j = m - 1;
            while (j > 0) {
                if (nums1[j] <= e) break;
                swap(nums1[j], nums1[j + 1]);
                j--;
            }

            nums1[j + 1] = e;
            m++;
        }

        // Complexity analysis 
        // Time : O(n * (m+n)) 
        // Space : O(1) 
    }

    void better(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m + n - 1;
        int p1 = m - 1;
        int p2 = n - 1;

        while (p1 >= 0 && p2 >= 0) {
            if (nums1[p1] > nums2[p2]) {
                nums1[i] = nums1[p1];
                i--; p1--;
            }
            else {
                nums1[i] = nums2[p2];
                i--; p2--;
            }
        }

        while (p1 >= 0) {
            nums1[i] = nums1[p1];
            i--; p1--;
        }

        while (p2 >= 0) {
            nums1[i] = nums2[p2];
            i--; p2--;
        }

        // Complexity analysis 
        // Time : O(m+n) 
        // Space : O(1) 
    }

public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // return brute_force(nums1, m, nums2, n);

        return better(nums1, m, nums2, n);
    }
};

void p1() {
    // Problem 1 : Leetcode 88. Merge Sorted Array - https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150 

    vector<int> n1 = { 1, 2, 4, 0, 0, 0 };
    vector<int> n2 = { 2, 7, 12 };

    Problem1().merge(n1, 3, n2, 3);

    for (int e : n1) cout << e << " ";
    cout << endl;
    for (int e : n2) cout << e << " ";
    cout << endl;
}

class Problem2 {
    int move_val_to_end(vector<int>& nums, int val) {
        int i = 0, j = nums.size() - 1;
        int count = 0;

        while (j >= 0 && nums[j] == val) j--;

        while (i <= j) {
            if (nums[i] == val) {
                swap(nums[i], nums[j]); j--;
            }
            else {
                count++; i++;
            }
        }

        return count;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }

    int move_val(vector<int>& nums, int val) {
        // putting val at the end manually 
        int count = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val) nums[count++] = nums[i];
        }

        for (int i = count; i < nums.size(); i++) {
            nums[i] = val;
        }

        return count;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }

public:
    int removeElement(vector<int>& nums, int val) {
        // return move_val_to_end(nums, val);

        return move_val(nums, val);
    }
};

void p2() {
    // Problem 2 : Leetcode 27. Remove Element - https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1 

    vector<int> nums = { 2, 5, 1, 3, 4,2, 5, 1, 3, 4, 5, 7, 2, 1 };
    int k = Problem2().removeElement(nums, 12);
    for (int e : nums) cout << e << " ";
    cout << endl;
}

class Ptoblem3 {
public:
    int removeDuplicates(vector<int>& nums) {
        int count = 0;

        for (int i = 1; i < nums.size(); i++) {
            if (nums[count] != nums[i]) count++;
            nums[count] = nums[i];
        }

        return count + 1;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }
};

void p3() {
    // Problem 3 : Leetcode 26. Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1 

    vector<int> nums = { 1,1,1 };
    int k = Ptoblem3().removeDuplicates(nums);
    for (int i = 0; i < k; i++) cout << nums[i] << " ";
    cout << endl;
}


int main() {
    // Day 1 of January 2025 
    // Started with Leetcode 150 - https://leetcode.com/studyplan/top-interview-150/ 

    p1();

    p2();

    p3();


    return 0;
}