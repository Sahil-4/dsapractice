#include <bits/stdc++.h>

using namespace std;

bool isPalindrome(int x) {
    if (x < 0) return false;

    long long copy = x;
    long long y = 0;

    while (copy != 0) {
        int d = copy % 10;
        copy /= 10;
        y *= 10;
        y += d;
    }

    return y == x;

    // Complexity analysis 
    // Time : O(Log(N)) 
    // Space : O(1) 
}

void p1() {
    // Problem 1 : Leetcode 9. Palindrome Number - https://leetcode.com/problems/palindrome-number/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/palindrome0746/1 

    cout << isPalindrome(112) << endl;
    cout << isPalindrome(11211) << endl;
    cout << isPalindrome(123) << endl;
    cout << isPalindrome(121) << endl;
    cout << isPalindrome(0) << endl;
    cout << isPalindrome(-121) << endl;
}

class Problem2 {
    vector<int> solve1(vector<int>& digits) {
        vector<int> result;

        reverse(digits.begin(), digits.end());

        int i = 0, n = digits.size();
        int carry = 1;

        while (i < n) {
            int sum = carry + digits[i];
            int digit = sum % 10;
            carry = sum / 10;
            i++;

            result.push_back(digit);
        }

        while (carry > 0) {
            int sum = carry;
            int digit = sum % 10;
            carry = sum / 10;

            result.push_back(digit);
        }

        reverse(digits.begin(), digits.end());
        reverse(result.begin(), result.end());

        return result;

        // Complexity analysis 
        // Time : O(4N) 
        // Space : O(1) 
    }

    vector<int> solve2(vector<int>& digits) {
        vector<int> result(digits);

        int carry = 1;
        int i = digits.size() - 1;

        while (carry > 0 && i >= 0) {
            int sum = carry + result[i];
            int digit = sum % 10;
            carry = sum / 10;
            result[i] = digit;

            i--;
        }

        while (carry > 0) {
            int sum = carry;
            int digit = sum % 10;
            carry = sum / 10;
            result.insert(result.begin(), digit);
        }

        return result;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }

public:
    vector<int> plusOne(vector<int>& digits) {
        // return solve1(digits);

        return solve2(digits);
    }
};

void p2() {
    // Problem 2 : Leetcode 66. Plus One - https://leetcode.com/problems/plus-one/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/plus-one/1 

    vector<int> digits = { 9 };
    for (int e : digits) cout << e << " ";
    cout << endl;

    vector<int> result = Problem2().plusOne(digits);
    for (int e : result) cout << e << " ";
    cout << endl;
}

class Problem3 {
    int solve1(int n) {
        // calculate factorial 
        long long facto = 1;
        for (n = n; n > 0; n--) facto *= n;

        // count zeores 
        int zeroes = 0;
        while (facto > 0) {
            int d = facto % 10;
            if (d) break;

            facto /= 10;
            zeroes++;
        }

        return zeroes;

        // Complexity analysis 
        // Time : O(N) + O(Log(N)) 
        // Space : O(1) 
    }

    int solve2(int n) {
        int zeroes = 0;
        int X = 5;

        while (X <= n) {
            zeroes += (n / X);
            X *= 5;
        }

        return zeroes;

        // Complexity analysis 
        // Time : O(Log(N)) (base5) 
        // Space : O(1) 
    }

public:
    int trailingZeroes(int n) {
        // return solve1(n);

        return solve2(n);
    }
};

void p3() {
    // Problem 3 : Leetcode 172. Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/trailing-zeroes-in-factorial5134/1 

    cout << Problem3().trailingZeroes(0) << endl;
    cout << Problem3().trailingZeroes(1) << endl;
    cout << Problem3().trailingZeroes(3) << endl;
    cout << Problem3().trailingZeroes(5) << endl;
    cout << Problem3().trailingZeroes(20) << endl;
    cout << Problem3().trailingZeroes(200) << endl;
    cout << Problem3().trailingZeroes(10000) << endl;
}


int main() {
    // Day 12 of February 

    p1();

    p2();

    p3();


    return 0;
}