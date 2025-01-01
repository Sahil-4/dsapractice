#include <iostream>
#include <string>

using namespace std;

void p1() {
    // Problem 1 : Add Strings - https://www.codingninjas.com/studio/guided-paths/data-structures-algorithms/content/651072/offering/10442099

    string num1 = "9999";
    string num2 = "199";
    // string num1 = "2";
    // string num2 = "12";
    // string num1 = "12";
    // string num2 = "12";
    // string num2 = "17";
    // string num1 = "5";
    // string num2 = "91";
    // string num1 = "5";
    // string num2 = "17";
    // string num1 = "9";

    int n1 = num1.size() - 1, n2 = num2.size() - 1;
    int carry = 0;
    string answer = "";

    while (n1 >= 0 && n2 >= 0) {
        int d1 = num1[n1] - '0';
        int d2 = num2[n2] - '0';

        int add = d1 + d2 + carry;
        carry = add / 10;
        add %= 10;

        answer = (char) (add + '0') + answer;

        n1--;
        n2--;
    }

    while (n1 >= 0) {
        int d1 = num1[n1] - '0';

        int add = d1 + carry;
        carry = add / 10;
        add %= 10;

        answer = (char) (add + '0') + answer;

        n1--;
    }

    while (n2 >= 0) {
        int d2 = num2[n2] - '0';

        int add = d2 + carry;
        carry = add / 10;
        add %= 10;

        answer = (char) (add + '0') + answer;

        n2--;
    }

    while (carry > 0) {
        int add = carry % 10;
        carry /= 10;

        answer = (char) (add + '0') + answer;
    }

    cout << carry << endl;
    cout << answer << endl;
}

int main() {
    // Day 013 

    p1();


    return 0;
}