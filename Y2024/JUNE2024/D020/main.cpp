#include <iostream>
#include <algorithm>

using namespace std;

string reverseWords(string str) {
    string revS = "";

    int n = str.length();
    int start = 0, end = 0;

    while (end < n) {
        while (end < n && str[end] != ' ') end++;
        
        if (start < end) {
            // we have a word 
            string word = str.substr(start, end - start);
            if (revS != "") word += " ";

            revS = word + revS;
        }

        while (end < n && str[end] == ' ') end++;
        start = end;
    }

    if (start < end) {
        // we have a word 
        string word = str.substr(start, end - start);
        if (revS != "") word += " ";
        revS = word + ' ' + revS;
    }

    return revS;
}

void removeExtraSpaces(string &str) {
    int n = str.length();
    int i = 0, j = 0;

    while (j < n) {
        if (str[j] != ' ') str[i++] = str[j++];
        else if (str[j] == ' ' && i != 0 && str[i - 1] != ' ') str[i++] = str[j++];
        else j++;
    }

    while (i > 0 && str[i - 1] == ' ') i--;
    str.erase(i, n - i);
}

string reverseWords(string str) {
    int n = str.length();
    int start = 0, end = 0;

    while (end < n) {
        while (end < n && str[end] != ' ') end++;
        if (start < end) reverse(str.begin() + start, str.begin() + end);

        while (end < n && str[end] == ' ') end++;
        start = end;
    }

    reverse(str.begin(), str.end());
    removeExtraSpaces(str);

    return str;
}

void p1() {
    // Problem 1 : Leetcode 151. Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/ 
    // GeeksForGeeks - https://www.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1 

    string str = "F R I E N D s";
    string rev = reverseWords(str);
    cout << "rev ::" << rev << endl;
}


int main() {
    // Day 20 

    p1();


    return 0;
}