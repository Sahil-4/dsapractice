#include <iostream>

using namespace std;

int getHash(int index, int length, int places) {
    // HASHING HASHING HASHING HASHING HASHING HASHING HASHING HASHING 
    return (places + index) % length;
}

bool isRotated(string str1, string str2) {
    // eat five star and do nothing 
    if (str1.length() != str2.length()) return false;
    // just in case if someone is in mood to play with our algo 

    int len = str1.length();
    int places = 2;

    for (int i = 0; i < str2.size(); i++) {
        if (str1[i] != str2[getHash(i, len, places)] && 
        str2[i] != str1[getHash(i, len, places)]) return 0;
    }

    return true;
}

void p1() {
    // Problem 1 : Check if string is rotated by two places - https://www.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places-1587115620/1 

    // string str1 = "abc";
    // string str2 = "cab";
    // string str1 = "daxjheq";
    // string str2 = "eqdaxjh";
    // string str1 = "abc";
    // string str2 = "bca";
    // string str1 = "amazon";
    // string str2 = "azonam";
    string str1 = "amazon";
    string str2 = "onamaz";

    // Example 1 : 
    // amazon 
    // rotated two places right we will get 
    // onamaz 
    // Example 2 : 
    // amazon 
    // rotated two places left we will get 
    // azonam 
    // Logic : 
    // lets first solve the case where the string is rotated 2 step forward or right 
    // amazon -> onamaz 
    // if we give some time and try to find a relation between indexes of real and rotated string 
    // we will find that str1[i] is placed at str2[(i + places) % str1.length()]
    // by this relation 
    // we can simply traverse the string from i = 0 to i < str.length() 
    // and compare characters on each indexes compare(str1[i], str2[(i + places) % str1.length()])
    // and we will be able to find whether or not string is rotated 2 step forward or on left 
    // now for the 2 step backward rotated case 
    // see Example 1 forward case once again 
    // real string : amazon -> rotated 2 step forward : onamaz 
    // amazon -> onamaz 
    // Example 2 backward case 
    // real string : amazon -> rotated 2 step backward : azonam 
    // amazon -> azonam
    // FOCUS 
    // in example 2 if we assume that the 2 step backwarded string is our real string 
    // then we can say that the real string is actually rotated 2 step forward string of assumed real string 
    // azonam -> amazon 
    // by here we have discarded the need to check for backward rotated string 
    // we will assume str2 as our str1 and will run same algo 
    // compare(str2[i], str1[(i + places) % str,length()])
    // which we are using for first case i.e. check forward rotation 
    // just because it is easy 
    // and we will be able to solve this problem in O(n) instead of O(2n) 

    cout << isRotated(str1, str2) << endl;
}

int main() {
    // Day 7 

    p1();


    return 0;
}