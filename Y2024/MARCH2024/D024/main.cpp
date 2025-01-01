#include <iostream>
#include <vector>

using namespace std;

int devideAndSum(vector<int>& nums, int d) {
    int sum = 0;

    for (int i = 0; i < nums.size(); i++) {
        sum += (nums[i] / d) + ((nums[i] % d) > 0 ? 1 : 0);
    }

    return sum;
}

int smallestDivisor(vector<int>& nums, int threshold) {
    int maxd = nums[0]; // largest possible divisor 
    for (int i = 1; i < nums.size(); i++) maxd = max(maxd, nums[i]);

    int ans = -1;

    int l = 1, h = maxd;
    int m = l + (h - l) / 2;

    while (l <= h) {
        long long sum = devideAndSum(nums, m);

        if (sum <= threshold) ans = m, h = m - 1;
        else l = m + 1;

        m = l + (h - l) / 2;
    }

    return ans;
}

void p1() {
    // P1 LC 1283. Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/  

    vector<int> nums = {1,2,5,9};
    int threshold = 6;

    int d = smallestDivisor(nums, threshold);
    cout << d << endl;
}

int daysToShip(vector<int>& weights, int cap) {
    int days = 1, load = 0;

    for (int i = 0; i < weights.size(); i++) {
        if (load + weights[i] <= cap) load += weights[i];
        else load = weights[i], days++;
    }

    return days;
}

int shipWithinDays(vector<int>& weights, int days) {
    int lowCap = 1, highCap = 0;

    for (int i = 0; i < weights.size(); i++) {
        lowCap = max(lowCap, weights[i]);
        highCap += weights[i];
    }

    int midCap = lowCap + (highCap - lowCap) / 2;

    int ans = -1;

    while (lowCap <= highCap) {
        int daysReq = daysToShip(weights, midCap);

        if (daysReq <= days) ans = midCap, highCap = midCap - 1;
        else lowCap = midCap + 1;

        midCap = lowCap + (highCap - lowCap) / 2;
    }

    return ans;
}

void p2() {
    // P2 LC 1011. Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/  

    vector<int> weights = {1,2,3,4,5,6,7,8,9,10};
    int days = 5; // out : 15 
    // vector<int> weights = {3,2,2,4,1,4};
    // int days = 3;

    int shipCap = shipWithinDays(weights, days);
    cout << shipCap << endl;
}

int main() {
    // Day 24 

    // p1();

    p2();


    return 0;
}