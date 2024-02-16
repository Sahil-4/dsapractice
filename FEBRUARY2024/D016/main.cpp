#include <iostream>
#include <map>

using namespace std;


int lenOfLongSubarr(int A[],  int N, int K) { 
    // Complete the function 
    map<int, int> hsm;
    int sum = 0;
    int len = 0;

    for (int i = 0; i < N; i++) {
        sum += A[i];
        hsm.insert({sum, i});

        if (sum == K) {
            len = max(len, i + 1);
        }

        if (hsm.find(sum - K) != hsm.end()) {
            len = max(len, i - hsm.at(sum - K));
        }
    }

    return len;
}

void p1() {
    // Problem 1 : Longest Sub-Array with Sum K - https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1 

    // int arr[] = {10, 5, 2, 7, 1, 9};
    int arr[] = {1, 4, 3, 3, 5, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    int k = 13;

    int len = lenOfLongSubarr(arr, n, k);
    cout << "len : " << len << endl;
}

int main() {
    // Day 16 

    p1();


    return 0;
}