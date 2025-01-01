#include <iostream>
#include <vector>

using namespace std;

int majorityElement(vector<int>& nums) {
    int freq = 0;
    int element = -1;

    for (int i = 0; i < nums.size(); i++) {
        if (freq == 0) {
            element = nums[i];
            freq++;
        } else {
            if (nums[i] == element) freq++;
            else freq--;
        }
    }

    return element; // as we must have at least one majority 
    //  in case if it is not the case we can simply run a loop and check the answer using freq and element 
    // if it is not answer return -1 as we dont have any 
}

void p1() {
    // Problem 1 :Majority element - https://leetcode.com/problems/majority-element/description/ 

    vector<int> arr = {2,2,1,1,1,2,2};
    int mj = majorityElement(arr);
    cout << "majority element : " << mj << endl;
}

void sortColors(vector<int>& nums) {
    int l = 0, m = 0, h = nums.size() - 1;
    // 2,0,2,1,1,0 

    while (m <= h) {
        if (nums[m] == 0) {
            swap(nums[l], nums[m]);
            l++;
            m++;
        } else if (nums[m] == 2) {
            swap(nums[h], nums[m]);
            // m++; // we dont know what is on h 
            h--;
        } else m++; // if 1 is on m 
    }
}

void p2() {
    // Problem 2 : Sort colors - https://leetcode.com/problems/sort-colors/description/ 

    // colors : {red : 0}, {white : 1}, {blue : 2} 
    // simply sort 0 1 2 

    vector<int> nums = {2,0,2,1,1,0};
    sortColors(nums);

    for (int i = 0; i < nums.size(); i++) {
        cout << nums[i] << " ";
    }
    cout << endl;
}

int main() {
    // Day 5 

    // p1();

    p2();


    return 0;
}