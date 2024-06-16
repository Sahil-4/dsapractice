#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool isPossibleAnswer(vector<int>& nums, int threshold, int divisor) {
    // if we are able to devide all elements by given divisor 
    // and the sum of division result is less then threshold 
    // then it can be an answer 
    // else if sum exceeds the threshold it can not be an answer 

    long long sum = 0;

    for (int i = 0; i < nums.size(); i++) {
        sum += nums[i] / divisor;
        if ((nums[i] % divisor) > 0) sum++;

        if (sum > threshold) return false;
    }

    return true;
}

int smallestDivisor(vector<int>& nums, int threshold) {
    // minimum divisor = 1, maximum divisor = maxElement(nums)
    vector<int>::iterator itr = max_element(nums.begin(), nums.end());
    int low = 1, high = nums[distance(nums.begin(), itr)];
    int ans = high;
    int mid = low + (high - low) / 2;

    while (low <= high) {
        // mid : divisor 
        bool check = isPossibleAnswer(nums, threshold, mid);

        if (!check) low = mid + 1;
        else {
            ans = min(ans, mid);
            high = mid - 1;
        }

        mid = low + (high - low) / 2;
    }

    return ans;

    // complexity analysis 
    // Time : O(n * log(maxElement(nums_arr))) 
    // Space : O(1) 
}

void p1() {
    // Problem 1 : Leetcode 1283. Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/ 
    // GeeksForGeeks - https://www.geeksforgeeks.org/problems/smallest-divisor/1 

    vector<int> nums = {1,2,5,9};
    int threshold = 5;

    int minDiv = smallestDivisor(nums, threshold);
    cout << "minDiv :: " << minDiv << endl;
}

int findKthPositive_Solution1(vector<int>& arr, int k) {
    for (int it = 0, i = 1; i <= arr.back(); i++) {
        if (arr[it] != i) k--;
        else it++;

        if (k == 0) return i;
    }

    return arr.back() + k;

    // Complexity analysis 
    // Time : O(n) 
    // Space : O(1) 
}

int findKthPositive(vector<int>& arr, int k) {
    // find appropriate element, where missing elements are <= k 
    int low = 0, high = arr.size();
    int mid = low + (high - low) / 2;

    while (low < high) {
        int missings = arr[mid] - mid - 1;

        if (missings < k) low = mid + 1;
        else high = mid;

        mid = low + (high - low) / 2;
    }

    return high + k;

    // Complexity analysis 
    // Time : O(log(n)) 
    // Space : O(1) 
}

void p2() {
    // Problem 2 : Leetcode 1539. Kth Missing Positive Number - https://leetcode.com/problems/kth-missing-positive-number/ 
    // GeeksForGeeks - https://www.geeksforgeeks.org/problems/k-th-missing-element3635/1 

    vector<int> arr = {};
    int k = 5;

    int missing = findKthPositive(arr, k);
    cout << "missing :: " << missing << endl;
}


int main() {
    // Day 16 

    p1();

    p2();


    return 0;
}