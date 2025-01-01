#include <iostream>
#include <vector>

using namespace std;

int totalFruit_Solution1(vector<int>& fruits) {
    int n = fruits.size();
    int fruitCount = 0;

    for (int i = 0; i < n; i++) {
        int type1 = -1, type2 = -1;
        int count = 0;

        for (int j = i; j < n; j++) {
            if (type1 == -1 || type1 == fruits[j]) {
                type1 = fruits[j];
                count++;
            } else if (type2 == -1 || type2 == fruits[j]) {
                type2 = fruits[j];
                count++;
            } else break;

            if (fruitCount < count) fruitCount = count;
        }
    }

    return fruitCount;

    // !TLE 
    // Time : O(n * n) 
    // Space : O(1) 
}

int totalFruit(vector<int>& fruits) {
    int n = fruits.size();
    int fruitsCount = 0;

    // fruitType : frequency 
    int fruitTypes[2] = { -1, -1 }; // store types of fruits 
    int fruitCounts[2] = { 0, 0 }; // store count of fruits 

    // left pointer 
    int l = 0;

    for (int r = 0; r < n; r++) {
        // update count of fruit of type fruits[r] if this type is present in fruitTypes[] 
        if (fruits[r] == fruitTypes[0]) {
            fruitCounts[0]++;
        } else if (fruits[r] == fruitTypes[1]) {
            fruitCounts[1]++;
        } else if (fruitTypes[0] == -1) {
            fruitTypes[0] = fruits[r];
            fruitCounts[0] = 1;
        } else if (fruitTypes[1] == -1) {
            fruitTypes[1] = fruits[r];
            fruitCounts[1] = 1;
        } else {
            // we will have to remove an old type and add current type fruits[r]
            // before this 
            // update the fruitsCount 
            if (fruitsCount < fruitCounts[0] + fruitCounts[1]) fruitsCount = fruitCounts[0] + fruitCounts[1];
            // now remove the 0th type and its count 
            while (fruitCounts[0] > 0 && fruitCounts[1] > 0) {
                if (fruits[l] == fruitTypes[0]) fruitCounts[0]--;
                if (fruits[l] == fruitTypes[1]) fruitCounts[1]--;
                l++;
            }

            // do a shifting of elements - move old element to index 0, so that we can add new element at index 1 
            if (fruitCounts[1] > 0) {
                fruitTypes[0] = fruitTypes[1];
                fruitCounts[0] = fruitCounts[1];
            }

            // now add new type fruits[r]
            fruitTypes[1] = fruits[r];
            fruitCounts[1] = 1;
        }
    }

    // for last types 
    if (fruitsCount < fruitCounts[0] + fruitCounts[1]) fruitsCount = fruitCounts[0] + fruitCounts[1];

    return fruitsCount;

    // Time : O(n) 
    // Space : O(1) 
}

void p1() {
    // Problem 1 : Leetcode 904. Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/fruit-into-baskets-1663137462/1 

    vector<int> fruits = {0,0,0,1,0,1,1,2,3};

    int maximumFruitsCount = totalFruit(fruits);
    cout << "maximumFruitsCount :: " << maximumFruitsCount << endl;
}

int main() {
    // Day 26 

    p1();


    return 0;
}