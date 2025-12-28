#include <bits/stdc++.h>

using namespace std;

class Problem1 {
public:
    string addBinary(string a, string b) {
        string out = "";

        int i = a.length() - 1;
        int j = b.length() - 1;

        int carry = 0;

        while (i >= 0 && j >= 0) {
            int d = carry + (a[i] - '0') + (b[j] - '0');

            if (d == 0 || d == 1) {
                out.push_back('0' + d);
                carry = 0;
            }
            else if (d == 2) {
                out.push_back('0');
                carry = 1;
            }
            else if (d == 3) {
                out.push_back('1');
                carry = 1;
            }

            i--, j--;
        }

        while (i >= 0) {
            int d = carry + (a[i] - '0');

            if (d == 0 || d == 1) {
                out.push_back('0' + d);
                carry = 0;
            }
            else if (d == 2) {
                out.push_back('0');
                carry = 1;
            }
            else if (d == 3) {
                out.push_back('1');
                carry = 1;
            }

            i--;
        }

        while (j >= 0) {
            int d = carry + (b[j] - '0');

            if (d == 0 || d == 1) {
                out.push_back('0' + d);
                carry = 0;
            }
            else if (d == 2) {
                out.push_back('0');
                carry = 1;
            }
            else if (d == 3) {
                out.push_back('1');
                carry = 1;
            }

            j--;
        }

        while (carry > 0) {
            int d = carry;

            if (d == 0 || d == 1) {
                out.push_back('0' + d);
                carry = 0;
            }
            else if (d == 2) {
                out.push_back('0');
                carry = 1;
            }
            else if (d == 3) {
                out.push_back('1');
                carry = 1;
            }
        }

        reverse(out.begin(), out.end());

        return out;

        // Complexity analysis 
        // Time : O(Max(N,M)) 
        // Space : O(1) 
    }
};

void p1() {
    // Problem 1 : Leetcode 67. Add Binary - https://leetcode.com/problems/add-binary/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/add-binary-strings3805/1 

    cout << Problem1().addBinary("1010", "1011") << endl;
    cout << Problem1().addBinary("1111", "0000") << endl;
    cout << Problem1().addBinary("1111", "0001") << endl;
}

class Problem2 {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t out = 0;

        for (int i = 0; i < 32; i++) {
            out = (out << 1) | n & 1;
            n >>= 1;
        }

        return out;

        // Complexity analysis 
        // Time : O(32) 
        // Space : O(1) 
    }
};

void p2() {
    // Problem 2 : Leetcode 190. Reverse Bits - https://leetcode.com/problems/reverse-bits/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/reverse-bits3556/1 

    cout << Problem2().reverseBits(1) << endl;
    cout << Problem2().reverseBits(0) << endl;
    cout << Problem2().reverseBits(5) << endl;
}

class Problem3 {
public:
    int hammingWeight(int n) {
        int count = 0;

        while (n != 0) {
            count += n & 1;
            n >>= 1;
        }

        return count;

        // Complexity analysis 
        // Time : O(32) 
        // Space : O(1) 
    }
};

void p3() {
    // Problem 3 : Leetcode 191. Number of 1 Bits - https://leetcode.com/problems/number-of-1-bits/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/set-bits0143/1 

    cout << Problem3().hammingWeight(0) << endl;
    cout << Problem3().hammingWeight(1) << endl;
    cout << Problem3().hammingWeight(2) << endl;
    cout << Problem3().hammingWeight(5) << endl;
    cout << Problem3().hammingWeight(10) << endl;
    cout << Problem3().hammingWeight(2147483647) << endl;
}

class Problem4 {
public:
    int singleNumber(vector<int>& nums) {
        int out = 0;
        for (int n : nums) out ^= n;
        return out;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }
};

void p4() {
    // Problem 4 : Leetcode 136. Single Number - https://leetcode.com/problems/single-number/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/single-number1014/1 

    vector<int> nums = { 1, 2, 1 };
    cout << Problem4().singleNumber(nums) << endl;
}

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        // track numbers appearing once, and twice 
        int ones = 0, twos = 0;

        // update 
        for (int n : nums) {
            // add n, and remove numbers appeard thrice 
            ones = (ones ^ n) & ~twos;

            // add n, and remove numbers appeard thrice 
            twos = (twos ^ n) & ~ones;
        }

        // left with a number appeard only once 
        return ones;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }
};

class Problem5 {
public:
    int singleNumber(vector<int>& nums) {
        // track numbers appearing once, and twice 
        int ones = 0, twos = 0;

        // update 
        for (int n : nums) {
            // add n, and remove numbers appeard thrice 
            ones = (ones ^ n) & ~twos;

            // add n, and remove numbers appeard thrice 
            twos = (twos ^ n) & ~ones;
        }

        // left with a number appeard only once 
        return ones;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }
};

void p5() {
    // Problem 5 : Leetcode 137. Single Number II - https://leetcode.com/problems/single-number-ii/description/?envType=study-plan-v2&envId=top-interview-150 

    vector<int> nums = { 0,1,0,1,0,1,99 };
    cout << Problem5().singleNumber(nums) << endl;
}

class Problem6 {
    int solve1(int left, int right) {
        int shift = 0;

        // longest common prefix 
        while (left != right) {
            left >>= 1;
            right >>= 1;
            shift++;
        }

        int bAnd = left << shift;

        return bAnd;

        // Complexity analysis 
        // Time : O(Log(N)) 
        // Space : O(1) 
    }

    int solve2(int left, int right) {
        while (right > left) {
            right = (right & (right - 1));
        }

        return right;

        // Complexity analysis 
        // Time : O(Log(N)) 
        // Space : O(1) 
    }

public:
    long long int findBitwiseOR(long long int left, long long int right) {
        // complete the function here

        int shift = 0;

        // longest common prefix 
        while (left != right) {
            left >>= 1;
            right >>= 1;
            shift++;
        }

        long long int bOr = left;
        for (int i = 0; i < shift; i++) {
            bOr = (bOr << 1) | (1);
        }

        return bOr;

        // Complexity analysis 
        // Time : O(Log(N)) 
        // Space : O(1) 
    }

    int rangeBitwiseAnd(int left, int right) {
        // return solve1(left, right);

        return solve2(left, right);
    }
};

void p6() {
    // Problem 6 : Leetcode 201. Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/ishaans-curiosity0853/0 

    cout << Problem6().rangeBitwiseAnd(1, 2147483647) << endl;
    cout << Problem6().findBitwiseOR(1, 2147483647) << endl;
    cout << Problem6().rangeBitwiseAnd(1, 1) << endl;
    cout << Problem6().findBitwiseOR(1, 1) << endl;
    cout << Problem6().rangeBitwiseAnd(1, 2) << endl;
    cout << Problem6().findBitwiseOR(1, 2) << endl;
}


int main() {
    // Day 11 of February 

    p1();

    p2();

    p3();

    p4();

    p5();

    p6();


    return 0;
}