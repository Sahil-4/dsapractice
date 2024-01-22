#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>


void p1() {
    // problem 1 : Perfect Numbers - https://www.geeksforgeeks.org/problems/perfect-numbers3207/1

    // find all factors of n till <n 
    // calculate sum of all factors 
    // return true if n is equal to the sum else return false 

    int n = 6;
    int sum = 1;

    for (int i = 2; i*i < n; i++) {
        if (n % i ==0) {
            if (i*i != n) sum += n/i;
            sum += i;
        };
    }

    printf("%d\n", sum == n && n != 1);
}

void p2() {
    // problem 2 : Armicable Numbers - https://www.geeksforgeeks.org/problems/amicable-pair0804/1 

    int a = 220;
    int b = 284;

    if (a == 0 || b == 0) {
        printf("false");
        return;
    }

    int sum_a = 1;
    int sum_b = 1;

    for (int i = 2; i * i <= a; i++) {
        if (a % i == 0) {
            sum_a += i;
            if (i*i != a) sum_a += a/i;
        }
    }

    if (sum_a != b) {
        printf("false");
        return;
    }

    for (int i = 2; i * i <= b; i++) {
        if (b % i == 0) {
            sum_b += i;
            if (i*i != a) sum_b += b/i;
        }
    }

    printf("%d", sum_a == b && sum_b == a);
}

void p3() {
    // problem 3 : Roots Of A Quadratic Equation - https://www.codingninjas.com/studio/problems/roots-of-a-quadratic-equation_893024 

    int a = 1, b = -5, c = 6;

    // find d 
    int d = (b * b) - (4 * a * c);

    // if there is no root 
    if (d < 0) {
        printf("not real roots");
        return;
    }

    // if roots are equal 
    if (d == 0) {
        int x1 = floor(-b / (2 * a));
        printf("root is only one : %d", x1);
        return;
    }

    // roots are different 
    int x1 = floor((-b + sqrt(abs(d)))/(2*a));
    int x2 = floor((-b - sqrt(abs(d)))/(2*a));

    // answer 
    printf("roots are : %d and %d", x1, x2);
}

void printReverse(char *str) {
    // print string in reverse order 
    if (*str == '\0') return;

    printReverse(++str);
    printf("%c", *(--str)); 
}

void p4() {
    // problem 4 : Reverse a String - https://www.geeksforgeeks.org/problems/reverse-a-string/1 

    char str[]= "gnihtemos";

    // int l = 0, h = sizeof(str)/sizeof(str[0]);
    // while (l < h) {
    //     char temp = str[l];
    //     str[l] = str[h];
    //     str[h] = temp;
        
    //     l++;
    //     h--;
    // }

    printReverse(str);
}


int main() {
    // Day 22 

    // p1();

    // p2();

    // p3();

    // p4();


    return 0;
}