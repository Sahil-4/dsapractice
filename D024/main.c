#include <conio.h>
#include <stdio.h>
#include <stdlib.h>


void p1() {
    // Problem 1 : Sort 0 1 2 - https://www.codingninjas.com/studio/problems/sort-0-1-2_631055 

    // using three pointers 
    // 0s : 0 to <l 
    // 1s : l to <m 
    // Us : m to h 
    // 2s : h+1 to <n 
    // do l++ if element at l is 0 
    // do h-- if element at h is 2 
    // now check element at m if it is 0 then change swap it with l 
    // and do l++ 
    // if element at m is 2 then swap it with h 
    // and do h-- 


    // int arr[] = {1, 0, 1, 2, 2, 1, 0};
    int arr[] = {2, 1, 0, 1, 2, 2, 1, 0};
    // int arr[] = {2, 1, 0};
    // int arr[] = {0, 1, 2};
    // int arr[] = {0, 2, 1};
    // int arr[] = {0, 2, 0};
    // int arr[] = {0, 2, 0, 1};
    // int arr[] = {0, 1, 2, 2, 1, 0};
    int n = sizeof(arr)/sizeof(arr[0]);

    printf("initially : \n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    int l = 0, m = 0, h = n-1;

    while (m <= h) {
        if (arr[m] == 0) {
            int temp = arr[m];
            arr[m] = arr[l];
            arr[l] = temp;
            l++;
            m++;
        } else if (arr[m] == 2) {
            int temp = arr[m];
            arr[m] = arr[h];
            arr[h] = temp;
            h--;
        } else m++;
    }

    printf("after sorting : \n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void p2() {
    // Problem 2 : Addition of two square matrices - https://www.geeksforgeeks.org/problems/addition-of-two-square-matrices4916/1 

    int matrixA[2][2] = {{1, 2}, {3, 4}}, matrixB[2][2] = {{4, 3}, {2, 1}};

    for (int i = 0; i < sizeof(matrixA)/sizeof(matrixA[0]); i++) {
        for (int j = 0; j < sizeof(matrixA[0])/sizeof(matrixA[0][0]); j++) {
            matrixA[i][j] += matrixB[i][j];
        }
    }

    for (int i = 0; i < sizeof(matrixA)/sizeof(matrixA[0]); i++) {
        for (int j = 0; j < sizeof(matrixA[0])/sizeof(matrixA[0][0]); j++) {
            printf("%d ", matrixA[i][j]);
        }
        printf("\n");
    }
}


int main() {
    // Day 24 

    // p1();

    // p2();


    return 0;
}