#include <iostream>
#include <map>

using namespace std;

int getPairsCount(int arr[], int n, int k) {
    // code here 
    map<int, int> hsm;
    int count = 0;

    // {1, 5, 7, 1}

    for (int i = 0; i < n; i++) {
        if (hsm.empty()) {
            // empty map 
            // just add current element and its freq 1 
            hsm.insert({arr[i], 1});
        } else if (hsm.find(k - arr[i]) != hsm.end()) {
            // possible answer 
            count += hsm.at(k - arr[i]);

            // update current element also and its freq 
            if (hsm.find(arr[i]) != hsm.end()) hsm.at(arr[i])++;
            else hsm.insert({arr[i], 1});
        } else {
            // not possible to create answer with current element 
            if (hsm.find(arr[i]) != hsm.end()) hsm.at(arr[i])++;
            else hsm.insert({arr[i], 1});
        }
    }

    return count;
}

void p1() {
    // Problem 1 : Count pairs with given sum - https://www.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1 

    int arr[] = {1, 5, 7, 1};
    int N = sizeof(arr) / sizeof(arr[0]);
    int K = 6;

    int count = getPairsCount(arr, N, K);
    cout << "Total count : " << count << endl;
}


int main() {
    // Day 17 

    p1();


    return 0;
}