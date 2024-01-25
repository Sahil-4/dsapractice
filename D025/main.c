#include <conio.h>
#include <stdio.h>
#include <stdlib.h>

void p1() {
    // Problem 1 : Implement Selection sort - https://www.codingninjas.com/studio/problems/selection-sort_624469

    // int arr[] = {8, 6, 2, 5, 1};
    // int arr[] = {0, 8, 6, 2, 5, 1};
    int arr[] = {1, 0, 2};
    int arr_size = sizeof(arr)/sizeof(arr[0]);

    for (int i = 0; i < arr_size; i++) {
        int min_index = i;
        for (int j = i+1; j < arr_size; j++) {
            if (arr[j] < arr[min_index]) min_index = j;
        }

        int temp = arr[i];
        arr[i] = arr[min_index];
        arr[min_index] = temp;
    }

    for (int i = 0; i < arr_size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    // Day 25 

    p1();


    return 0;
}