#include <iostream>
#include <vector>
#include <stack>

using namespace std;

vector<int> nextSmallLeft(vector<int>& arr, int n) {
    vector<int> ns(n);
    stack<int> stk;

    for (int i = 0; i < n; i++) {
        while (!stk.empty() && arr[stk.top()] >= arr[i]) stk.pop();

        if (stk.empty()) ns[i] = -1;
        else ns[i] = stk.top();

        stk.push(i);
    }

    return ns;
}

vector<int> nextSmallRight(vector<int>& arr, int n) {
    vector<int> ns(n);
    stack<int> stk;

    for (int i = n - 1; i >= 0; i--) {
        while (!stk.empty() && arr[stk.top()] > arr[i]) stk.pop();

        if (stk.empty()) ns[i] = n;
        else ns[i] = stk.top();

        stk.push(i);
    }

    return ns;
}

int sumSubarrayMins(vector<int>& arr) {
    int mod = 1e9 + 7;
    int sum = 0;

    int n = arr.size();

    vector<int> ns_l = nextSmallLeft(arr, n);
    vector<int> ns_r = nextSmallRight(arr, n);

    for (int i = 0; i < n; i++) {
        long long e = arr[i], l = ns_l[i], r = ns_r[i];

        long long sub_arr = (i - ns_l[i]) * (ns_r[i] - i);
        long long prod = (e % mod) * (sub_arr % mod) % mod;

        sum = ((sum % mod) + (prod % mod) % mod);
    }

    return sum;
}

void p1() {
    // Problem 1 : Leetcode 907. Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/sum-of-subarray-minimum/1 

    vector<int> arr = {2,1,4,5,7,1};
    int sum = sumSubarrayMins(arr);
    cout << "sum ::" << sum << endl;
}


int main() {
    // Day 9 

    p1();


    return 0;
}