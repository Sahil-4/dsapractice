#include <iostream>
#include <vector>

using namespace std;

void p1() {
    // Problem 1 : Swap alternates - https://www.codingninjas.com/codestudio/problems/swap-alternate_624941  

    int arr[] = {1, 2, 7, 8, 5}; // out : 
    int size = 5;

    // initial array printing 
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    for (int i = 0; i < size; i+=2) {
        // index out of bound 
        if (i+1 >= size) break;

        // swapping 
        arr[i] = arr[i]^arr[i+1];
        arr[i+1] = arr[i]^arr[i+1];
        arr[i] = arr[i]^arr[i+1];
    }

    // answer printing 
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void p2() {
    // Problem 2 : Find unique - https://www.codingninjas.com/codestudio/problems/find-unique_625159 

    int arr[] = {2, 2, 5, 6, 3, 1, 5, 3, 6};
    int size = 9;

    int ans = 0;

    for (int i = 0; i < size; i++) {
        ans = ans ^ arr[i];
    }

    cout << ans << endl;
}

void p3() {
    // Problem 3 : Find duplicate - https://www.codingninjas.com/codestudio/problems/duplicate-in-array_893397 

    vector<int> arr = {1, 2, 3, 5, 2, 4, 6}; // arr[i] > 0 && arr[i] < arr.size(); 

    // int n = arr.size()-1;

    // int ans = (n * (n+1))/2;

    // for (int i = 0; i < arr.size(); i++) {
    //     ans -= arr[i];
    // }

    // cout << ans*-1 << endl;

    int ans = 0;
    for (int i = 0; i < arr.size(); i++) {
        ans = ans ^ arr[i];
    }
    // done XOR one time 

    for (int i = 1; i < arr.size(); i++) {
        ans = ans ^ i;
    }

    // Logic is like this 
    // XOR with 1 to N (range of elements)
    // d ^ c ^ a ^ b ^ a = Y (array elements)
    // Y ^ a ^ b ^ c ^ d (i in range of elements)
    // = d ^ c ^ a ^ b ^ a ^ a ^ b ^ c ^ d 
    // = a ^ a ^ a ^ b ^ b c ^ c ^ d ^ d 
    // = 0 ^ a ^ 0 ^ 0 ^ 0 
    // = a 

    cout << ans << endl;
}

void p4() {
    // Problem 4 : Segregate 0s and 1s - https://www.geeksforgeeks.org/problems/segregate-0s-and-1s5106/1 

    vector<int> arr = {1, 0, 0, 1, 1, 0, 1};
    int size = arr.size();

    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    int l = 0, h = size-1;

    while (l < h) {
        while (arr[l] == 0) {
            l++;
        }

        while (arr[h] == 1) {
            h--;
        }

        // checking l < h is important 
        // because of above loop 
        // but in case we add continue in above loops 
        // then there is no need to add this check 
        if (l < h && arr[l] == 1 && arr[h] == 0) {
            arr[l] = arr[l] ^ arr[h];
            arr[h] = arr[l] ^ arr[h];
            arr[l] = arr[l] ^ arr[h];

            l++;
            h--;
        }
    }

    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}


int main() {
    // Day 010 

    // p1();

    // p2();

    // p3();

    // p4();


    return 0;
}