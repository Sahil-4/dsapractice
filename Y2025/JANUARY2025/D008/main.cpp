#include <bits/stdc++.h>

using namespace std;

class Problem1 {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> out;

        int n = words.size();
        int i = 0;

        while (i < n) {
            // count letters of words and spaces between words (1 space)
            int lettersCount = words[i].length();
            int spacesCount = 0;
            int j = i + 1;

            // take in letters and space of words[j] 
            while (j < n && words[j].length() + 1 + lettersCount + spacesCount <= maxWidth) {
                lettersCount += words[j].length();
                spacesCount++;
                j++;
            }

            // calculate remaining spaces/slots on screen/line 
            int remainingSlots = maxWidth - lettersCount;
            // spaces between each word 
            int spacesEach = spacesCount == 0 ? 0 : remainingSlots / spacesCount;
            // extra spaces (add 1 space after each word to left justified) 
            int spacesExtra = spacesCount == 0 ? 0 : remainingSlots % spacesCount;

            // last line - left justified and no extra spaces 
            if (j == n) {
                spacesEach = 1;
                spacesExtra = 0;
            }

            // now create actual line to print on screen 
            string line = "";
            // even space to add between words 
            string spaces = "";
            for (int s = 0; s < spacesEach; s++) spaces += ' ';
            for (int k = i; k < j; k++) {
                line += words[k];
                if (k != j - 1) line += spaces; // last word dont add space 
                if (spacesExtra > 0 && spacesExtra--) line += ' ';
            }

            // line still may have remaining slots add spaces in them 
            while (line.length() < maxWidth) line += ' ';

            // add this line into output array 
            out.push_back(line);

            i = j; // update pointer for next line 
        }

        return out;

        // Complexity analysis 
        // Time : O(N*strlen) single array traversal + line building 
        // Space : O(1) 
    }
};

void p1() {
    // Problem 1 : Leetcode 68. Text Justification - https://leetcode.com/problems/text-justification/description/?envType=study-plan-v2&envId=top-interview-150 

    vector<string> words = { "This", "is", "an", "example", "of", "text", "justification." };
    int maxWidth = 16;
    vector<string> screenLines = Problem1().fullJustify(words, maxWidth);
    for (string line : screenLines) cout << line << endl;
}

class Problem2 {
    bool solve1(string s) {
        // two pointers 

        int i = 0, j = 0;

        // remove spaces and non alphanumeric chars 
        i = j = 0;
        while (j < s.length()) {
            if (s[j] >= 'a' && s[j] <= 'z') s[i++] = s[j];
            else if (s[j] >= 'A' && s[j] <= 'Z') s[i++] = s[j];
            else if (s[j] >= '0' && s[j] <= '9') s[i++] = s[j];
            j++;
        }

        // remove extra chars 
        s.erase(i);
        // convert caps to small 
        i = j = 0;
        while (j < s.length()) {
            if (s[j] >= 'A' && s[j] <= 'Z') s[j] = 'a' + (s[j] - 'A');
            j++;
        }

        // check for palindrome 
        i = 0, j = s.length() - 1;
        while (i < j) {
            if (s[i] != s[j]) return false;
            i++, j--;
        }

        return true;

        // Complexity analysis 
        // Time : O(N) traversal 
        // Space : O(N) copying input data 
    }

public:
    bool isPalindrome(string s) {
        return solve1(s);
    }
};

void p2() {
    // Problem 2 : Leetcode 125. Valid Palindrome - https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/palindrome-string0817/1 

    cout << Problem2().isPalindrome("A man, a plan, a canal: Panama") << endl;
}

class Problem3 {
public:
    bool isSubsequence(string s, string t) {
        int N = s.length(), M = t.length();
        int i = 0, j = 0;

        while (i < N && j < M) {
            if (s[i] == t[j]) i++;
            j++;
        }

        return i == N;

        // Complexity analysis 
        // Time : O(N+M) 
        // Space : O(1) 
    }
};

void p3() {
    // Problem 3 : Leetcode 392. Is Subsequence - https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/check-for-subsequence4930/1 

    cout << Problem3().isSubsequence("", "") << endl;
}

class Problem4 {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0, r = numbers.size() - 1;

        while (l < r) {
            if (numbers[l] + numbers[r] == target) return { l + 1, r + 1 };
            else if (numbers[l] + numbers[r] < target) l++;
            else r--;
        }

        return {};

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }
};

void p4() {
    // Problem 4 : Leetcode 167. Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150 

    vector<int> numbers = { 2,7,11,15 };
    int t = 9;
    vector<int> indices = Problem4().twoSum(numbers, t);
    cout << numbers[indices[0]] + numbers[indices[1]] << endl;
}


int main() {
    // Day 8 of January 2025 

    p1();

    p2();

    p3();

    p4();


    return 0;
}