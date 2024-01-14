#include <iostream>

using namespace std;

void p1() {
    // Problem 1 : Sum of all divisors - https://www.codingninjas.com/studio/problems/sum-of-all-divisors_8360720?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM 


    // bruteforce solution 
    // int n = 5;
	// int ans = 0;
	// for (int i = 1; i <= n; i++) {
	// 	int add = 0;
	// 	for (int j = 1; j <= i; j++) if (i%j == 0) add += j;
	// 	ans += add;
	// }
    // bruteforce solution 


    // optimised 
    int n = 7;
    int ans = 0;

    for (int i = 1; i <= n; i++) {
        ans += (int) (n/i) * i;
    }
    // optimised 

    cout << ans << endl;
}


int main() {
    // Day 014 

    p1();


    return 0;
}