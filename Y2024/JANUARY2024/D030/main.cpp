#include <iostream>
#include <string>

using namespace std;

int makeBeautiful(string str) {
	// Write your code here 
	int str1 = 1;
	int str2 = 0;

	int count1 = 0;
	int count2 = 0;

	for (int i = 0; i < str.length(); i++) {
		if ((str[i] - '0') != str1) count1++;
		if ((str[i] - '0') != str2) count2++;

		str1 = str1 == 0 ? 1 : 0;
		str2 = str2 == 0 ? 1 : 0;
	}

	return count1 < count2 ? count1 : count2;

    // more simplified code (Extra)
	int count1 = 0;
	int count2 = 0;

	for (int i = 0; i < str.length(); i++) {
		if (i % 2 == 0 && str[i] != '1') count1++;
		if (i % 2 != 0 && str[i] != '0') count1++;

		if (i % 2 == 0 && str[i] != '0') count2++;
		if (i % 2 != 0 && str[i] != '1') count2++;
	}

	return count1 < count2 ? count1 : count2;
}

void p1() {
    // Problem 1 : Beautiful Strings - https://www.codingninjas.com/studio/problems/beautiful-string_1115625

    // a binary string is given 
    // "0101011100", "011100101" 
    // a beautiful string is a binary string that has alternating 0s and 1s 
    // "010101", "1010101" 
    // it may start from 0 or 1 it may end on 0 or 1 
    // but all bits will be alternating for sure 
    // so the string we have given is binary string
    // and we have to make it beautiful binary string 
    // by performing minimum operations 
    // and at the end we will have to return the number of operations 
    // ok start with first problem 
    // make the binary string a beautiful string 
    // what we can do 
    // lets solve this second problem 
    // we can simply traverse the entire array 
    // and we check if str[current] == str[current + 1] 
    // true then change the str[current+1] element 
    // do this for entire string 
    // by this we will be able to make the string a beautiful 
    // but it may possible that the number of operations performed to make it beautiful is not minimum 
    // so what should we do ? 
    // for this we can create two beautiful strings by our side of same size of the given string 
    // one string str1 will start from 0 and another str2 will start from 1 
    // now after creating the strings 
    // create two variables count1 and count2 
    // traverse the given string 
    // and match character of given string with str1 and str2 
    // if str1[current] != str[current] increament count1 by 1 
    // if str2[current] != str[current] increament count2 by 1 
    // at the end return the minimum of count1 and count2 
    // so now arises third problem 
    // which is we have taken some extra space for strings 
    // to fix this we have to use two integer variables instead of strings 
    // and as we just have to check one bit at a time we can change the value of str1 (integer) and str2(integer) every time after comparing 

    // Extra : 
    // what if we cant even use ints to store bits 
    // in this case we can take benifits of 
    // alternating behaviour of bits 
    // and odd and even indexes 

    cout << makeBeautiful("1010") << endl;
    cout << makeBeautiful("0000") << endl;
    cout << makeBeautiful("101000010101010101000000000111111000000111110001010110101000001111001") << endl;
}


int main() {
    // Day 30 

    p1();
    

    return 0;
}