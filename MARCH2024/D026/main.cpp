#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int ballsCanPlaced(vector<int>& position, int minDifference) {
    int ballsPlaced = 1;
    int lastPositionIndex = 0;

    for (int i = 1; i < position.size(); i++) {
        if (position[i] - position[lastPositionIndex] >= minDifference) lastPositionIndex = i, ballsPlaced++;
    }

    return ballsPlaced;
}

int maxDistance(vector<int>& position, int m) {
    sort(position.begin(), position.end());

    int ans = -1;
    int low = 1, high = position[position.size() - 1];
    int mid = low + (high - low) / 2;

    while (low <= high) {
        int ballsPlaced = ballsCanPlaced(position, mid);

        if (ballsPlaced >= m) ans = mid, low = mid + 1;
        else high = mid - 1;

        mid = low + (high - low) / 2;
    }

    return ans;
}

void p1() {
    // Problem 1 : LC 1552. Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/description/ 

    vector<int> position = {1,2,3,4,7};
    int m = 3;

    int d = maxDistance(position, m);
    cout << d << endl;
}

int makeSubarrays(vector<int>& nums, int maxSum) {
    int n = 1;
    int sum = nums[0];

    for (int i = 1; i < nums.size(); i++) {
        if (sum + nums[i] <= maxSum) sum += nums[i];
        else sum = nums[i], n++;
    }

    return n;
}

int splitArray(vector<int>& nums, int k) {
    int low = nums[0], high = nums[0];
    for (int i = 1; i < nums.size(); i++) low = max(low, nums[i]), high += nums[i];

    int mid = low + (high - low) / 2;

    while (low <= high) {
        int n = makeSubarrays(nums, mid);

        if (n > k) low = mid + 1;
        else high = mid - 1;

        mid = low + (high - low) / 2;
    }

    return low;
}

void p2() {
    // Problem 2 : LC 410. Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/ 

    vector<int> nums = {7,2,5,10,8}; 
    int k = 2;

    int ls = splitArray(nums, k);
    cout << ls << endl;
}

int main() {
    // Day 26 

    p1();

    p2();


    return 0;
}