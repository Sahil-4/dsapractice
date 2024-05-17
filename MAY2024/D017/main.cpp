#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>

using namespace std;

bool isCollisionPossible(int leftElement, int rightElement) {
    // left element should move towards right, 
    // and right element should move towards left 
    if (leftElement > 0 && rightElement < 0) return true;
    return false;
}

int collisionResult(int leftElement, int rightElement) {
    if (abs(leftElement) == abs(rightElement)) return 0;
    else if (abs(leftElement) > abs(rightElement)) return leftElement;
    else return rightElement;
}

vector<int> asteroidCollision(vector<int>& asteroids) {
    vector<int> ans;

    for (int i = asteroids.size() - 1; i >= 0; i--) {
        if (ans.empty()) {
            ans.push_back(asteroids[i]);
        } else {
            int leftElement = asteroids[i];
            while (!ans.empty() && isCollisionPossible(leftElement, ans.back())) {
                int rightElement = ans.back(); ans.pop_back();
                leftElement = collisionResult(leftElement, rightElement);
            }

            if (leftElement != 0) ans.push_back(leftElement);
        }
    }

    if (!ans.empty()) reverse(ans.begin(), ans.end());
    return ans;
}

void p1() {
    // Problem 1 : Leetcode 735. Asteroid Collision - https://leetcode.com/problems/asteroid-collision/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/asteroid-collision/1 

    vector<int> asteroids = {1, 2, 6, 8, 2, -55};

    vector<int> leftOutAsteroids = asteroidCollision(asteroids);
    for (int i = 0; i < leftOutAsteroids.size(); i++) cout << leftOutAsteroids[i] << " ";
    cout << endl;
}

long long subArrayRanges_Solution1(vector<int>& nums) {
    int n = nums.size();
    long long ansSum = 0;

    for (int i = 0; i < n; i++) {
        long long mini = INT_MAX, maxi = INT_MIN;

        for (int j = i; j < n; j++) {
            if (mini > nums[j]) mini = nums[j];
            if (maxi < nums[j]) maxi = nums[j];

            ansSum += maxi - mini;
        }
    }

    return ansSum;

    // T = O(n * n)
}

long long subArrayRanges(vector<int>& nums) {
    int n = nums.size();
    long long ansSum = 0;

    for (int i = 0; i < n; i++) {
        long long mini = INT_MAX, maxi = INT_MIN;

        for (int j = i; j < n; j++) {
            if (mini > nums[j]) mini = nums[j];
            if (maxi < nums[j]) maxi = nums[j];

            ansSum += maxi - mini;
        }
    }

    return ansSum;

    // BRUTE FORCE - NEEDS TO BE OPTIMIZED 
}

void p2() {
    // Problem 2 : Leetcode 2104. Sum of Subarray Ranges - https://leetcode.com/problems/sum-of-subarray-ranges/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/sum-of-subarray-ranges/1 

    vector<int> nums = {2, 5, 7, 1, 2, 5, 45};
    int sum = subArrayRanges(nums);
    cout << "SUM :: " << sum << endl;
}


int main() {
    // Day 17 

    p1();

    p2();


    return 0;
}