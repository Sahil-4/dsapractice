#include <iostream>
#include <vector>

using namespace std;

int findSum(vector<int>& cardPoints) {
    int sum = cardPoints[0];
    for (int i = 1; i < cardPoints.size(); i++) sum += cardPoints[i];
    return sum;
}

int maxScore(vector<int>& cardPoints, int k) {
    int n = cardPoints.size();
    int sum = 0;

    if (k == n) return findSum(cardPoints);
    if (k == 1) return max(cardPoints.front(), cardPoints.back());

    // left right pointers 
    int l = 0, r = k - 1;

    // initial window - window logic 
    for (int it = l; it <= r; it++) sum += cardPoints[it];

    // other windows - window logic 
    int tempSum = sum;
    for (int pc = 1; pc <= k; pc++) {
        tempSum -= cardPoints[(n + r--) % n];
        tempSum += cardPoints[(n + --l) % n];
        sum = max(sum, tempSum);
    }

    return sum;

    // NOTE : if k can be more then n then make sure to do its modulo first 
    // Complexity analysis 
    // Time : O(n), worst case (if k == n) else O(2k) 
    // Space : O(1) 
}

void p1() {
    // Problem 1 : Leetcode 1423. Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/maximum-point-you-can-obtain-from-cards/0 

    vector<int> cardPoints = {10,6,5,1,5,8,15};
    int k = 5;

    int sum = maxScore(cardPoints, k);
    cout << "max sum :: " << sum << endl;
}


int main() {
    // Day 31 - Completed 5 Months 152 days 

    p1();


    return 0;
}