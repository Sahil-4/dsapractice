#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

void p1() {
    // Problem 1 : Two sum - https://leetcode.com/problems/two-sum/

    vector<int> arr = {2,7,11,15};
    int target = 9;
    unordered_map<int, int> hashmap;
    vector<int> ans;

    for (int i = 0; i < arr.size(); i++) {
        // how much do we need with arr[i] to make target 
        int need = target - arr[i];

        // do we have this much in the hashmap 
        if (hashmap.find(need) != hashmap.end()) {
            // yes we have 
            ans.push_back(i);
            ans.push_back(hashmap[need]);
            break;
        }

        // no we dont have 
        // put current element with its index in the hashmap 
        hashmap.insert(make_pair(arr[i], i));
        // for next elements 
    }

    for (int i = 0; i < ans.size(); i++) {
        cout << arr[ans[i]] << " ";
    }
    cout << endl;
}

void sortBubble(vector<int> &arr, int n) {
    for (int i = 0; i < arr.size() - 1; i++) {
        bool flag = true;
        for (int j = 0; j < arr.size() - 1 - i; j++) {
            if (arr[j] < arr[j+1]) continue;

            flag = false;

            int temp = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = temp;
        }

        if (flag == true) break;
    }
} 

void p2() {
    // Problem 2 : Bubble Sort - https://www.codingninjas.com/studio/problems/bubble-sort_624380 

    vector<int> arr = {5, 2, 7};

    for (int i = 0; i < arr.size(); i++) cout << arr[i] << " ";
    cout << endl;

    sortBubble(arr, arr.size());

    for (int i = 0; i < arr.size(); i++) cout << arr[i] << " ";
    cout << endl;
}


int main() {
    // Day 026 

    // p1();

    // p2();


    return 0;
}