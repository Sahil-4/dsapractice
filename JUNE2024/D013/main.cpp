#include <iostream>
#include <vector>

using namespace std;

int findMaxConsecutiveOnes(vector<int>& nums) {
    int maxOnesCount = 0, temp = 0;

    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] == 0) temp = 0;
        else temp++;

        maxOnesCount = max(maxOnesCount, temp);
    }

    return maxOnesCount;
}

int maxConsecutiveOnes(int N) {
    // code here
    int maxOnesCount = 0, temp = 0;

    while (N != 0) {
        if ((N & 1) == 0) temp = 0;
        else temp++;

        N = N >> 1;

        maxOnesCount = max(maxOnesCount, temp);
    }

    return maxOnesCount;
}

void p1() {
    // Problem 1 : Leetcode 485. Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/description/ 
    // GeeksForGeeks - https://www.geeksforgeeks.org/problems/longest-consecutive-1s-1587115620/1 

    vector<int> binary = {1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1};
    int ones = findMaxConsecutiveOnes(binary);
    // int ones = maxConsecutiveOnes(12);
    cout << "ones : " << ones << endl;
}

int main() {
    // Day 13 

    p1();


    return 0;
}