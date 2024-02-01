#include <iostream>
#include <vector>

using namespace std;

long long int sum(long long int n) {
	// using sum of n
	// just to avoid TLE 

	return (n * (n + 1)) / 2;
}

long long int prod(long long int n) {
	long long int prod = 1;

	for (long long int i = 1; i <= n; i++) {
		prod *= i;
		prod = prod % 1000000007; // to avoid overflow 
	}

	return prod;
}

long long int sumOrProduct(long long int n, long long int q) {
	if (q == 1) return sum(n);
	if (q == 2) return prod(n);

    return 0;
}

void p1() {
    // Problem 1 :  Sum or Product - https://www.codingninjas.com/studio/problems/sum-or-product_920478 

    long long int n = 5, q = 1;

    int ans = sumOrProduct(n, q);

    cout << ans << endl;
}

vector<int> twoSum(vector<int>& arr, int target) {
    // two pointers : most efficient solution 
    // can be solved linearly with n^2 time complexity - very basic and first approach 
    // can be solved using hashing also (this will be efficient approach if array is not sorted) 

    int l = 0, h = arr.size() - 1;

    while (l < h) {
        if (arr[l] + arr[h] == target) {
            return {l + 1, h + 1};
        } else if (arr[l] + arr[h] < target) {
            l++;
        } else {
            h--;
        }
    }

    return {-1, -1};
}

void p2() {
    // Problem 2 : Leetcode 167 : Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted 

    vector<int> arr = {2,7,11,15};
    int target = 9;

    vector<int> ans = twoSum(arr, target);

    cout << ans[0] << " and " << ans[1] << endl;
}


int main() {
    // Day 27 

    p1();

    p2();


    return 0;
}
