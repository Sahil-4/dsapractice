#include <iostream>
#include <vector>

#define SUM_OF_N(N) (N * (N + 1)) / 2 

using namespace std;

int missingNumber(vector<int>& arr, int n) {
    // Your code goes here
    int nSum = SUM_OF_N(n);
    int arrSum = 0;

    for (int i = 0; i < n - 1; i++) {
        arrSum += arr[i];
    }

    return nSum - arrSum;
}

void p1() {
    // Problem 1 : Missing number - https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1 

    vector<int> arr = {1, 2, 3, 7, 6, 4, 5};
    int N = 8;

    // N = 3 
    // arr = {1 2} 
    // sumOfN(3) = 1 + 2 + 3 = 6 
    // sumOfArr(arr) = 1 + 2 = 3 
    // ans = sumOfN(3) - sumOfArr(arr) 
    // sumOfN(N) : (N * (N + 1)) / 2 

    int missing = missingNumber(arr, N);
    cout << "missing is : " << missing << endl;
}

int findMaximum(int arr[], int n) {
    // code here 
    int l = 0, h = n-1;
    int m = l + (h - l)/2;

    while (l < h) {
        if (arr[m-1] <= arr[m] && arr[m] >= arr[m+1]) return arr[m];

        if (arr[m-1] <= arr[m] && arr[m] <= arr[m+1]) {
            // search on right side 
            l = m + 1;
        } else {
            // search on left side 
            h = m;
        }

        m = l + (h - l)/2;
    }

    return arr[n-1];
}

void p2() {
    // Problem 2 : Bitonic Point - https://www.geeksforgeeks.org/problems/maximum-value-in-a-bitonic-array3001/1 

    int arr[] = {1, 2, 6, 2, 0};
    int n = 5;

    int bitonic = findMaximum(arr, n);
    cout << bitonic << endl;
}

int main() {
    // Day 9 

    // p1();

    p2();

    // Todays learning 
    // 1. if there is any question includes numbers or if it is related to maths try to apply maths logic on it 
    // 2. check if we can use binary in any question if the time limit is given as log(n) 


    return 0;
}
