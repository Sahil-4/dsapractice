#include <iostream>
#include <vector>
#include <set>

using namespace std;

set<int> allPrimeFactors(int N) {
    set<int> ans;
    int i = 2;
    while (i <= N && N > 1) {
        if (N % i != 0) i++;
        else {
            ans.insert(i);
            N /= i;
        }
    }
    return ans;
}

int distinctPrimeFactors(vector<int> nums) {
    set<int> ans;

    for (int i = 0; i < nums.size(); i++) {
        set<int> tmp = allPrimeFactors(nums[i]);
        ans.insert(tmp.begin(), tmp.end());
    }

    return ans.size();
}

void p1() {
    // Problem 1 : Leetcode 2427. Number of Common Factors - https://leetcode.com/problems/number-of-common-factors/ 

    // int count = distinctPrimeFactors({2,4,3,7,10,6});
    // int count = distinctPrimeFactors({2,4,8,16});
    int count = distinctPrimeFactors({2,4,5,13});

    cout << count << endl;
}

int main() {
    // Day 7 

    p1();


    return 0;
}