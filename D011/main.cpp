#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

void p1() {
    // Problem 1 : N-Forest - https://www.codingninjas.com/studio/problems/n-forest_6570177 
    int n = 5;

    for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << "* ";
		}
		cout << endl;
	}
}

void p2() {
    // Problem 2  : N/2-Forest - https://www.codingninjas.com/studio/problems/n-2-forest_6570178 

    int n = 5;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
}

void p3() {
    // Problem 3 : N-Triangles - https://www.codingninjas.com/studio/problems/n-triangles_6573689 

    int n = 3;

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			cout << j << " ";
		}
		cout << endl;
	}
}

void p4() {
    // Problem 4 : Triangle - https://www.codingninjas.com/studio/problems/triangle_6573690 

    int n = 3;

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			cout << i << " ";
		}
		cout << endl;
	}
}

void p5() {
    // Problem 5 : Seeding - https://www.codingninjas.com/studio/problems/seeding_6581892 

    int n = 3;

	for (int i = n; i > 0; i--) {
		for (int j = i; j > 0; j--) {
			cout << "* ";
		}
		cout << endl;
	}
}

void p6() {
    // Problem 6 : Reverse Number Triangle - https://www.codingninjas.com/studio/problems/reverse-number-triangle_6581889 

    int n = 3;

    for (int i = n; i > 0; i--) {
        for (int j = 1; j <= i; j++) {
            cout << j << " ";
        }
        cout << endl;
    }
}

void p7() {
    // Problem 7 : Leetcode 442 : Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/ 

    // ways to solve this 
    // 1. brute force by traversing the whole array and checking for same elements in nested loops 
    // 2. taking an array having elements of range and marking them visited after encountering them 
    // 3. hashing : going to each element, thinking it as a index and updating element at this index by *-1 now next time if we encounter any such value then we can declare it as a duplicate 

    // vector<int> arr = {4,3,2,7,8,2,3,1};
    // vector<int> arr = {4,3,2,7,8,2,3,1};
    vector<int> arr = {1,1,2};
    // vector<int> arr = {10,2,5,10,9,1,1,4,3,7};
    vector<int> ans;

    for (int i = 0; i < arr.size(); i++) {
        int index = abs(arr[i])-1;

        if (arr[index] < 0) {
            // duplicate 
            ans.push_back(index + 1);
        }

        arr[index] *= -1;
    }

    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << endl;
    }
}

int main() {
    // Day 010 

    // p1();

    // p2();

    // p3();

    // p4();

    // p5();

    // p6();

    p7();


    return 0;
}