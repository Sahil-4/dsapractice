#include <iostream>
#include <vector>

using namespace std;

void wave(int *arr, int size) {
    if (size == 0 || size == 1) return;

    for (int i = 0; i < size - 1; i += 2) {
        arr[i] = arr[i] ^ arr[i+1];
        arr[i+1] = arr[i] ^ arr[i+1];
        arr[i] = arr[i] ^ arr[i+1];
    }
}

void p1() {
    // Problem 1 : Wave Array - https://www.geeksforgeeks.org/problems/wave-array-1587115621/1 

    // array is sorted 
    // run a loop 
    // take elements in pairs 
    // swap them 
    // move to next pair 

    int arr[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr)/sizeof(arr[0]);

    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    wave(arr, size);

    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

bool isAnagram(string a, string b) {
    if (a.length() != b.length()) return false;

    if (a.length() == 0 && b.length() == 0) return true;
    if (a == b) return true;

    vector<int> arr1(26, 0);
    vector<int> arr2(26, 0);

    for (int i = 0; i < a.length(); i++) {
        arr1[a[i] - 'a']++;
        arr2[b[i] - 'a']++;
    }

    for (int i = 0; i < 26; i++) {
        if (arr1[i] != arr2[i]) return false;
    }
    return true;
}

void p2() {
    // Problem 2 : Anagram - https://www.geeksforgeeks.org/problems/anagram-1587115620/1 

    // return false if both array does not have same length 
    // init two hashmaps/or array of 26 elements {a-z} 
    // 26 because string consists only lowercase characters [a-z] 
    // traverse the both array together in one loop 
    // check the current character and increase the frequency of it in hashmap or array 

    string str1 = "";
    string str2 = "";
    if (isAnagram(str1, str2)) cout << "anagram" << endl;
    else cout << "not anagram" << endl;
}


int main() {
    // Day 3 

    p1();

    p2();


    return 0;
}
