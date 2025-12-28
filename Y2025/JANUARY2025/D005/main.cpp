#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    int brute(vector<int>& height) {
        int N = height.size();

        vector<int> llel;
        llel.push_back(height[0]);
        for (int i = 1, ll = 0; i < N; i++) {
            if (height[i] >= height[ll]) ll = i;
            llel.push_back(height[ll]);
        }

        vector<int> ller;
        ller.push_back(height[N - 1]);
        for (int i = N - 2, ll = N - 1; i >= 0; i--) {
            if (height[i] >= height[ll]) ll = i;
            ller.push_back(height[ll]);
        }
        reverse(ller.begin(), ller.end());

        int trappedWater = 0;

        for (int i = 0; i < N; i++) {
            trappedWater += (min(llel[i], ller[i]) - height[i]);
        }

        return trappedWater;

        // Complexity analysis 
        // Time : O(4N) 
        // Space : O(2N) 
        // Note: ll in loop is used as stack or priority queue 
        // we need largest elemenet on left/right (only one largest element) 
    }

    int better(vector<int>& height) {
        // DP solution - remembering last largest walls 

        int N = height.size();

        vector<int> lle_lr(N);
        lle_lr[0] = height[0];
        for (int i = 1, ll = 0; i < N; i++) {
            if (height[i] >= height[ll]) ll = i;
            lle_lr[i] = height[ll];
        }

        int trappedWater = 0;

        trappedWater += min(lle_lr[N - 1], height[N - 1]) - height[N - 1];
        for (int i = N - 2, ll = N - 1; i >= 0; i--) {
            if (height[i] >= height[ll]) ll = i;
            trappedWater += (min(lle_lr[i], height[ll]) - height[i]);
        }

        return trappedWater;

        // Complexity analysis 
        // Time : O(2N) 
        // Space : O(N) 
    }

    int optimal(vector<int>& height) {
        // two pointer 

        int trappedWater = 0;
        int N = height.size();

        int l = 0, r = N - 1; // left, right pointer 
        int lmax = 0, rmax = 0; // left, right max height 

        while (l < r) {
            lmax = max(lmax, height[l]);
            rmax = max(rmax, height[r]);

            if (lmax > height[l]) trappedWater += (lmax - height[l]);
            if (rmax > height[r]) trappedWater += (rmax - height[r]);

            height[l] < height[r] ? l++ : r--;
        }

        return trappedWater;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
        // Intuition : we just need the smaller height 
        // and then we will have to get smallerI - heightI 
        // using two pointers we are first traversing smaller ones and remembering them for final result 
    }

public:
    int trap(vector<int>& height) {
        // return brute(height);

        // return better(height);

        return optimal(height);
    }
};

void p1() {
    // Problem 1 : Leetcode 42. Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/0 

    vector<int> height = { 1, 0, 2, 2, 3, 0, 5, 7, 5 };
    cout << Problem1().trap(height) << endl;
}

class Problem2 {
    map<char, int> mp = {
        {'I', 1},   {'V', 5},   {'X', 10},   {'L', 50},
        {'C', 100}, {'D', 500}, {'M', 1000},
    };

public:
    int romanToInt(string s) {
        /*
            I  ->   1
            V  ->   5
            X  ->   10
            L  ->   50
            C  ->   100
            D  ->   500
            M  ->   1000
        */

        // III -> 1 + 1 + 1
        // XI -> 1 + 10
        // XIV -> 5 - 1 + 10
        // XIX -> 10 - 1 + 10

        int number = 0;

        for (int i = 0, N = s.length(); i < N; i++) {
            int cnum = mp[s[i]];
            int nnum = -1;
            if (i != N - 1) nnum = mp[s[i + 1]];

            if (cnum < nnum) number -= cnum;
            else number += cnum;
        }

        return number;

        // Complexity analysis 
        // Time : O(N) + map lookup 
        // Space : O(1) + map 
    }
};

void p2() {
    // Problem 2 : Leetcode 13. Roman to Integer - https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/roman-number-to-integer3201/1 

    string s = "XIV";
    cout << Problem2().romanToInt(s) << endl;
}

class Problem3 {
    map<int, char> mp = {
        {1, 'I'},   {5, 'V'},   {10, 'X'},   {50, 'L'},
        {100, 'C'}, {500, 'D'}, {1000, 'M'},
    };

    void replace(string& s, string oldstr, string newstr) {
        auto it = s.find(oldstr);
        if (it == string::npos) return;
        s.replace(it, oldstr.length(), newstr);

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }

    string solve1(int num) {
        string r = "";

        while (num >= 1000) {
            r += mp[1000];
            num -= 1000;
        }

        while (num >= 500) {
            r += mp[500];
            num -= 500;
        }

        while (num >= 100) {
            r += mp[100];
            num -= 100;
        }

        while (num >= 50) {
            r += mp[50];
            num -= 50;
        }

        while (num >= 10) {
            r += mp[10];
            num -= 10;
        }

        while (num >= 5) {
            r += mp[5];
            num -= 5;
        }

        while (num >= 1) {
            r += mp[1];
            num -= 1;
        }

        /*
            4 - IIII -> IV
            9 - VIIII -> IX
            40 - XXXX -> XL
            90 - LXXXX -> XC
            400 - CCCC -> CD
            900 - DCCCC -> CM
        */

        replace(r, "DCCCC", "CM");
        replace(r, "CCCC", "CD");
        replace(r, "LXXXX", "XC");
        replace(r, "XXXX", "XL");
        replace(r, "VIIII", "IX");
        replace(r, "IIII", "IV");

        return r;

        // Complexity analysis 
        // Time : O(N), N = length of final string 
        // Space : O(1) 
    }

    string tricky(int num) {
        string M[] = { "", "M", "MM", "MMM" }; // 0, 1000, 2000, 3000 
        string C[] = { "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" }; // 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 
        string X[] = { "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" }; // 0, 10, ..., 40, 50, 60, ... 90 
        string I[] = { "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" }; // 0, 1, ..., 4, 5, 6, ... 9 
        return M[num / 1000] + C[(num % 1000) / 100] + X[(num % 100) / 10] + I[num % 10];
    }

public:
    string intToRoman(int num) {
        // return solve1(num);

        return tricky(num);
    }
};

void p3() {
    // Problem 3 : Leetcode 12. Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/convert-to-roman-no/1 

    cout << Problem3().intToRoman(4) << endl;
    cout << Problem3().intToRoman(9) << endl;
    cout << Problem3().intToRoman(40) << endl;
    cout << Problem3().intToRoman(90) << endl;
    cout << Problem3().intToRoman(98) << endl;
    cout << Problem3().intToRoman(99) << endl;
}

class Problem4 {
public:
    int lengthOfLastWord(string s) {
        // remove empty spaces from last 
        int it = s.length() - 1;
        while (it >= 0 && s[it] == ' ') it--;

        // count non space chars and exit on space 
        int len = 0;
        while (it >= 0 && s[it] != ' ') it--, len++;

        return len;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }
};

void p4() {
    // Problem 4 : Leetcode 58. Length of Last Word - https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/length-of-last-word5721/1 

    cout << Problem4().lengthOfLastWord("  abcs sdjsfjd kdsajf  ") << endl;
    cout << Problem4().lengthOfLastWord("  a  ") << endl;
    cout << Problem4().lengthOfLastWord("  a  aaaa ns") << endl;
    cout << Problem4().lengthOfLastWord("  abcs sdjsfjd kdsajf  ") << endl;
}


int main() {
    // Day 5 of January 

    p1();

    p2();

    p3();

    p4();


    return 0;
}