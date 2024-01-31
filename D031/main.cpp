#include <iostream>
#include <vector>

using namespace std;

vector<int> merge4(vector<int>& arr1, vector<int>& arr2, int m, int n) {
    // Solution 3 S(1) T(m+n)
    // Fancy code 

    int p1 = m-1, p2 = n-1, p3 = m + n - 1;

    while (p2 >= 0 && p1 >= 0) {
        if (arr1[p1] > arr2[p2])  arr1[p3--] = arr1[p1--];
        else arr1[p3--] = arr2[p2--];
    }

    while (p3 >= 0 && p2 >= 0)  arr1[p3--] = arr2[p2--];

    return arr1;
}

vector<int> merge3(vector<int>& arr1, vector<int>& arr2, int m, int n) {
    // Solution 3 S(1) T(m+n)

    int p1 = m-1, p2 = n-1, p3 = m + n - 1;

    while (p2 >= 0 && p1 >= 0) {
        if (arr1[p1] > arr2[p2]) {
            arr1[p3] = arr1[p1];
            p1--;
        } else {
            arr1[p3] = arr2[p2];
            p2--;
        }

        p3--;
    }

    while (p3 >= 0 && p2 >= 0) {
        arr1[p3--] = arr2[p2--];
    }

    return arr1;
}

vector<int> merge2(vector<int>& arr1, vector<int>& arr2, int m, int n) {
    // Solution 2 S(1) T(n*m) 

    for (int i = 0; i < n; i++) {
        int l = m-1;
        int element = arr2[i];

        while (l >= 0 && arr1[l] > element) {
            arr1[l+1] = arr1[l];
            l--;
        }

        arr1[l+1] = element;
        m++;
    }

    return arr1;
}

vector<int> merge(vector<int>& arr1, vector<int>& arr2, int m, int n) {
    // Solution 1 : T(n+m) and S(n+m) 

    // create new array 
	vector<int> ans;

    // traverse the both given array 
	int p1 = 0, p2 = 0;
	while (arr1[p1] != 0 && p1 < arr1.size() && p2 < arr2.size()) {
        // check for small element one by one 
        // and insert it in the answer array 
		if (arr1[p1] == arr2[p2]) {
			ans.push_back(arr1[p1]);
			ans.push_back(arr2[p2]);
			p1++;
			p2++;
		} else if (arr1[p1] < arr2[p2]) {
			ans.push_back(arr1[p1]);
			p1++;
		} else {
			ans.push_back(arr2[p2]);
			p2++;
		}
	}

    // add left over elements of arrays 
	while (arr1[p1] != 0 && p1 < arr1.size()) {
		ans.push_back(arr1[p1]);
		p1++;
	}

	while (p2 < arr2.size()) {
		ans.push_back(arr2[p2]);
		p2++;
	}

    // return the answer 
	return ans;
}

void p1() {
    // Problem 1 : Merge Two Sorted Arrays - https://www.codingninjas.com/studio/problems/ninja-and-sorted-arrays_1214628 

    // vector<int> arr1 = {3, 6, 9, 0, 0};
    // vector<int> arr2 = {4, 10};
    vector<int> arr1 = {1, 4, 7, 0, 0, 0};
    vector<int> arr2 = {2, 5, 8};

    arr1 = merge3(arr1, arr2, arr1.size() - arr2.size(), arr2.size());

    for (int i = 0; i < arr1.size(); i++) {
        cout << arr1[i] << " ";
    }
    cout << endl;
}

int main() {
    // Day 31 

    p1();


    return 0;
}