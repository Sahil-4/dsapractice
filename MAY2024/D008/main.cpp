#include <iostream>
#include <vector>

using namespace std;

vector<int> sieveOfEratosthenes(int N) {
    // Write Your Code here
    if (N <= 2) return {};

    vector<int> ans(N, 1);
    ans[0] = ans[1] = 0;

    // sieve of eratosthenes
    for (int i = 2; i < N; i++) {
        if (ans[i] == 0) continue;

        ans[i] = i;

        for (int j = i + i; j < N; j += i) ans[j] = 0;
    }

    // using two pointers 
    int it1 = 0, it2 = 0;
    while (it1 < N && it2 < ans.size()) {
        if (ans[it2] != 0) ans[it1++] = ans[it2];

        it2++;
    }

    ans.erase(ans.begin() + it1, ans.end());

    return ans;
}

int countPrimes(int n) {
    vector<int> primes = sieveOfEratosthenes(n);
    return primes.size();
}

void p1() {
    // Problem 1 : Leetcode 204. Count Primes - https://leetcode.com/problems/count-primes/ 

    int c = countPrimes(10);
    cout << c << endl;
}


int main() {
    // Day 8 

    p1();


    return 0;
}