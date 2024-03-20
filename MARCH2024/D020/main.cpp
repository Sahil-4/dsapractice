#include <iostream>
#include <vector>

using namespace std;

bool search(vector<int>& nums, int target) {
    int l = 0, h = nums.size() - 1;
    int mid = l + (h - l) / 2;

    while (l <= h) {
        if (nums[mid] == target) return true;

        if (nums[l] == nums[mid] && nums[mid] == nums[h]) {
            l++;
            h--;
            continue;
        }
        if (nums[l] <= nums[mid]) {
            // left part is sorted 
            // use left part to find the next sub array to find the target 
            if (nums[l] <= target && target < nums[mid]) {
                h = mid - 1;
            } else {
                l = mid + 1;
            }
        } else {
            // right part is sorted 
            // use right part to find next sub array to find target 
            if (nums[mid] < target && target <= nums[h]) {
                l = mid + 1;
            } else {
                h = mid - 1;
            }
        }

        mid = l + (h - l) / 2;
    }

    return false;
}

void p1() {
    // Problem 1 : Search in Rotated Sorted Array II - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/ 

    vector<int> nums = {1,0,1,1,1};
    int target = 5;

    bool t = search(nums, target);
    cout << t << endl;
}

int singleNonDuplicate(vector<int>& nums) {
    int l = 0, h = nums.size() - 1;
    int m = l + (h - l) / 2;

    // edge cases 
    if (nums.size() == 1 || nums[0] != nums[1]) return nums[0];
    if (nums[nums.size() - 2] != nums[nums.size() - 1]) return nums[nums.size() - 1];

    while (l <= h) {
        // nums[m] is the element 
        if (nums[m] != nums[m - 1] && nums[m] != nums[m + 1]) {
            return nums[m];
        }

        if (m & 1) {
            if (nums[m] == nums[m - 1]) {
                l = m + 1;
            } else {
                h = m - 1;
            }
        } else {
            if (nums[m] == nums[m + 1]) {
                l = m + 1;
            } else {
                h = m - 1;
            }
        }

        m = l + (h - l) / 2;
    }

    return -1;
}

void p2() {
    // problem 2 : 540. Single Element in a Sorted Array - https://leetcode.com/problems/single-element-in-a-sorted-array/description/ 

    // vector<int> arr = {3,3,7,7,10,11,11};
    vector<int> arr = {3};

    int element = singleNonDuplicate(arr);
    cout << element << endl;
}


int main() {
    // Day 20 

    p1();

    p2();


    return 0;
}