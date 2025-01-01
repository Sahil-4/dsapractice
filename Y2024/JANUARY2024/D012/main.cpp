#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

void p1() {
    // Problem 1 : Find duplicates in an array - https://www.geeksforgeeks.org/problems/find-duplicates-in-an-array/1 

    // range is 0 to n-1
    // old technique multiplying by -1 will not work here 
    // lets try another technique 
    // move the element out of range 
    // lets add n in the element 
    // simply traverse the array 
    // and add n in all elements at arr[i] 
    // arr[i] is the hash 
    // we have used elements as index and incremented values at element index (arr[i] index)
    // now next time to get index out of elements we have to use modulo 
    // as it will give us real element's value after removing all increament of n(s) 
    // if we can return answer in any order then we can create answer array inside this loop only 
    // by just checking the same 
    // if arr[i] / n >= 2 or not 
    // if its true means it is occurred more then once 
    // but we have to return answer in sorted form 
    // we can use above hash 
    // if we look closely we can see that 
    // if arr[i] assume it as 2 is occurred once then we are adding n into 2nd element 
    // now if we start from 0 and keep checking till n 
    // we can find get this in sorted order 

    // vector<int> arr = {0,3,1,2};
    // vector<int> arr = {0,0};
    vector<int> arr = {0,3,1,2,2,1};
    int n = arr.size();
    vector<int> ans;

    // applying hash 
    for (int i = 0; i < n; i++) {
        int e = arr[i]%n;
        arr[e] += n;
    }

    // adding answers in sorted form 
    for (int i = 0; i < n; i++) {
        if (arr[i]/n >= 2) {
            ans.push_back(i);
        }
    }

    if (ans.size() == 0) {
        ans.push_back(-1);
    }

    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << " ";
    }
    cout << endl;
}


int main() {
    // Day 012 

    p1();


    return 0;
}