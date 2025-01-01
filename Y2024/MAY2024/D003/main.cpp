#include <iostream>
#include <vector>

using namespace std;

int countOnBits(int n) {
    int count = 0;

    while (n != 0) {
        if (n & 1) count++;
        n = n >> 1;
    }

    return count;
    // O(log(n))
}

vector<int> countBits_solution1(int n) {
    vector<int> ans;

    for (int i = 0; i <= n; i++) {
        // O(n)
        int nOfOnBits = countOnBits(i);
        ans.push_back(nOfOnBits);
    }

    return ans;
    // T = O(n * log(n)) 
}

vector<int> countBits(int n) {
    if (n == 0) return {0};

    vector<int> ans = {0, 1};

    for (int i = 2; i <= n; i++) {
        if (i & 1) ans.push_back(ans[i/2] + 1);
        else ans.push_back(ans[i/2]);
    }

    return ans;
    // T = O(n) 
}

void p1() {
    // Problem 1 : Leetcode 338. Counting Bits - https://leetcode.com/problems/counting-bits/ 

    int n = 22;

    vector<int> bits = countBits(n);

    for (int i = 0; i < bits.size(); i++) cout << bits[i] << " ";
    cout << endl;
}

int main() {
    // Day 3 

    p1();


    return 0;
}