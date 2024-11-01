#include <iostream>
#include <vector>

using namespace std;

long long int MODO = 1e9 + 7;

long long int memo(int n, vector<int>& dp) {
    if (n <= 1) {
        dp[0] = 0;
        dp[1] = 1;

        return dp[n];
    }

    if (dp[n] != -1) {
        return dp[n];
    }

    dp[n] = (((memo(n - 1, dp) % MODO) + (memo(n - 2, dp) % MODO)) % MODO);
    return dp[n];
}

long long int topDown(int n) {
    // code here

    // --- memoization --- 
    // start remembering from first 

    vector<int> dp(10001, -1);
    return memo(n, dp);
}

long long int tabu(int n) {
    vector<int> dp(10001, -1);
    dp[0] = 0;
    dp[1] = 1;

    if (n <= 1) {
        return dp[n];
    }

    for (int i = 2; i <= n; i++) {
        dp[i] = ((dp[i - 1] % MODO) + (dp[i - 2] % MODO)) % MODO;
    }

    return dp[n];
}

long long int bottomUp(int n) {
    // code here

    // --- tabulation --- 
    // start remembering from last 

    // return tabu(n);

    // -- tabulation & space optimised -- 

    int prev2 = 0, prev1 = 1;

    if (n <= 1) {
        return n;
    }

    for (int i = 2; i <= n; i++) {
        int curr = ((prev2 % MODO) + (prev1 % MODO)) % MODO;
        prev2 = prev1;
        prev1 = curr;
    }

    return prev1;
}

void p1() {
    // Problem 1 : Leetcode 509. Fibonacci Number - https://leetcode.com/problems/fibonacci-number/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/introduction-to-dp/1 
    // Introduction to DP 

    int N = 100;

    cout << topDown(N) << endl;
    cout << bottomUp(N) << endl;
}

int main() {
    // Day 1 of November - Started dynamic programming 

    p1();


    return 0;
}