#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;

int removeElement(vector<int>& nums, int val) {
    int a = 0;

    for (int b = 0; b < nums.size(); b++) {
        if (nums[b] == val) continue;
        nums[a++] = nums[b];
    }

    return a;
}

void p1() {
    // Problem 1 : Leetcode 27. Remove Element - https://leetcode.com/problems/remove-element/description/ 

    vector<int> nums = {3,2,2,3};
    int val = 3;
    int n = removeElement(nums, val);
    for (int i = 0; i < n; i++) cout << nums[i] << " ";
    cout << endl;
}

int maxSubArray(vector<int>& nums) {
    int maxSum = INT_MIN;
    int sum = 0;

    for (int b = 0; b < nums.size(); b++) {
        sum += nums[b];
        maxSum = max(maxSum, sum);

        if (sum < 0) sum = 0;
    }

    return maxSum;
}

vector<int> maxSubArray_V2(vector<int>& nums) {
    int maxSum = INT_MIN;
    int sum = 0;

    int start = 0, end = 0;
    int temp_start = 0;

    for (int b = 0; b < nums.size(); b++) {
        if (sum == 0) temp_start = b;

        sum += nums[b];

        if (maxSum < sum) {
            maxSum = sum;
            start = temp_start;
            end = b;
        }

        if (sum < 0) sum = 0;
    }

    return { nums.begin() + start, nums.begin() + end + 1 };
}

vector<int> findSubarray(int n, int nums[]) {
    // code here 
    int maxSum = INT_MIN;
    int sum = 0;

    int start = 0, end = 0;
    int temp_start = 0;

    for (int b = 0; b < n; b++) {
        if (nums[b] < 0) {
            sum = 0;
            continue;
        }

        if (sum == 0) temp_start = b;

        sum += nums[b];

        if (maxSum < sum || (maxSum == sum && b - temp_start > end - start)) {
            maxSum = sum;
            start = temp_start;
            end = b;
        }

        if (sum < 0) {
            sum = 0;
        }
    }

    return { nums + start, nums + end + 1 };
}

void p2() {
    // Problem 2 : Leetcode 53. Maximum Subarray - https://leetcode.com/problems/maximum-subarray/description/ 
    // GeeksForGeeks - https://www.geeksforgeeks.org/problems/maximum-sub-array5443/1 

    vector<int> arr = {-2,1,-3,4,-1,2,1,-5,4};
    int sum = maxSubArray(arr);
    cout << "max sum ::" << sum << endl;

    int arr2[] = {-2,1,-3,4,-1,2,1,-5,4};
    int n = 9;
    vector<int> subArr = findSubarray(n, arr2);
    for (int i = 0; i < subArr.size(); i++) cout << subArr[i] << " ";
    cout << endl;
}

int main() {
    // Day 23 

    p1();

    p2();


    return 0;
}