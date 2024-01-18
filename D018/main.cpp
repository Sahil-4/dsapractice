#include <iostream>
#include <vector>

using namespace std;

void p1() {
    // Problem 1 : Factorial Numbers Not Greater Than N - https://www.codingninjas.com/studio/problems/factorial-numbers-not-greater-than-n_8365435 

    // input 
    long long n = 54545454;

    // answers 
    vector<long long> factorials;

    // base condition 
    if (n == 0) return;

    long long factorial = 1;
    long long i = 1;

    // find factorials 
    while (true) {
        factorial *= i++;
        if (factorial > n) break;
        factorials.push_back(factorial);
    }

    // print answers 
    for (int i = 0; i < factorials.size(); i++) cout << factorials[i] << " ";
    cout << endl;
}


int main() {
    // Day 018 

    p1();


    return 0;
}