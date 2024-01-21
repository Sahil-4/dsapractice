#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int fibbonacci(int n) {
    // recursion 
    if (n == 0) return 0;
    if (n == 1) return 1;

    return fibbonacci(n-1) + fibbonacci(n-2);

    // Not optimal 
    // Can be opmised using DP - Memoization 
}

void p1() {
    // Problem 1 : Print Fibonacci Series - https://www.codingninjas.com/studio/problems/print-fibonacci-series_7421617 

    int n = 5;
    int ans[5];

    if (n == 1) {
        printf("%d", ans[0]);
        return;
    }
    ans[1] = 1;

    for (int i = 2; i < n; i++) {
        ans[i] = ans[i-1] + ans[i-2];
    }

    return ans;
}

void p2() {
    // Problem 2: Develop algorithm, flowchart and write an interactive program to calculate simple interest and compound interest.

    // start
    // initialize principal = 0, intrst_rate = 0.0, time = 0 
    // initialize simple_intrst = 0.0, compound_intrst = 0.0 
    // take input  principal, intrst_rate, time 
    // calculate simple_intrst = (principal * intrst_rate * time)/100 
    // calculate compound_intrst = principal * ((1 + intrst_rate/100) ** time) - principal
    // print simple_intrst, compound_intrst 
    // end 

    // for input 
    int principal = 0, time = 0;
    float intrst_rate = 0;

    // for output 
    float simple_intrst = 0, compound_intrst = 0;

    // taking input 
    printf("Enter principal amount in rupees : \n");
    scanf("%d", &principal);

    printf("Enter interest rate in percentage : \n");
    scanf("%f", &intrst_rate);

    printf("Enter time in years : \n");
    scanf("%d", &time);

    // calculating 
    simple_intrst = (principal * intrst_rate * time)/100;
    compound_intrst = principal * (pow(1 + intrst_rate/100, time)) - principal;

    // printing output 
    printf("Simple Interest is : %f\n", simple_intrst);
    printf("Compound Interest is : %f\n", compound_intrst);
}

void p3() {
    // Problem 3 : Design a flowchart and write an interactive program that reads in integers until
    // a 0 is entered. If it encounters 0 as input, then it should display:
    // the total number of even and odd integers
    // average value of even integers
    // Average value of odd integers.
    // Note: Use switch statement for selection

    int num = 0;
    int even_count = 0, odd_count = 0;
    do {
        printf("Enter any number : ");
        scanf("%d", &num);
        printf("\n");

        switch (num & 1) {
        case 1:
            // odd 
            num != 0 && odd_count++;
            break;
        
        case 0:
            // even 
            num != 0 && even_count++;
            break;
        
        default:
            break;
        }
    } while (num != 0);

    printf("Total odds : %d\n", odd_count);
    printf("Total odds : %d\n", even_count);
}


int main() {
    // Day 21 

    // p1();

    // p2();

    // p3();


    return 0;
}