#include <iostream>
#include <vector>

using namespace std;

void sortColors(vector<int>& nums) {
    int n = nums.size();

    // initialising pointers 
    int l = 0, m = l, h = n - 1;

    // sorting by swapping appropriate values 
    while (m <= h) {
        if (nums[m] == 0) swap(nums[l], nums[m]), l++, m++;
        else if (nums[m] == 2) swap(nums[h], nums[m]), h--;
        else if (nums[m] == 1) m++;
    }
}

void p1() {
    // Problem 1 : Leetcode 75 Sort colors - https://leetcode.com/problems/sort-colors/ 

    vector<int> nums = {2,1,2,0,1,2};
    sortColors(nums);
    for (int i = 0; i < nums.size(); i++) cout << nums[i] << " ";
    cout << endl;
}

int search(int A[], int l, int h, int key) {
    // l: The starting index
    // h: The ending index, you have to search the key in this range

    // complete the function here
    int m = l + (h - l) / 2;

    while (l <= h) {
        if (A[m] == key) return m;

        if (A[m] >= A[l]) {
            // left side is in sorted order 
            if (A[l] <= key && key <= A[m]) {
                // key is in left part 
                h = m - 1;
            } else {
                // key is in right part 
                l = m + 1;
            }
        } else {
            // right side is in sorted order 
            if (A[m] <= key && key <= A[h]) {
                // key is in left part 
                l = m + 1;
            } else {
                // key is in right part 
                h = m - 1;
            }
        }

        m = l + (h - l) / 2;
    }

    return -1;
}

void p2() {
    // Problem 2 : GeeksForGeeks Search in a Rotated Array - https://www.geeksforgeeks.org/problems/search-in-a-rotated-array4618/1 

    int A[] = {5,6,8,25,1,2,3};
    int n = 7;
    int key = 205;
    int l = 0, h = n - 1;

    int idx = search(A, l, h, key);
    cout << "idx :: " << idx << endl;
}

int main() {
    // Day 7 

    p1();

    p2();


    return 0;
}