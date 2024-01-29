#include <iostream>

using namespace std;

void p1() {
    // Problem 1 : Insertion sort - https://www.codingninjas.com/studio/problems/insertion-sort_624381 

    // lets say arry is arr = { 9 7 8 6 2 0 3 1 5 16 4}
    // initially we will have 9 in sorted array and 7 8 6 2 0 3 1 5 16 4 in un sorted array 
    // so we will be running loop to sort only elements starting from index 1 
    // now we are in loop 
    // ok so we will be now placing 7 in sorted array at its correct position 
    // how ? 
    // we will traverse the sorted array 
    // from last index (which is l = i-1) to 0th index l >= 0 
    // and we will be checking for the element that is either small or equal to 7 because after that only we can place 7 
    // and while traversing the array 
    // we will be increasing the index of each element to make place for 7 (or the element which we have to place)
    // at some point of time we will see that the element is small then 7 
    // or we dont have anu other element we reached to the left edge of the array 
    // now this is the place where we have to put our element 

    // now lets say we are sorting arr = { 9 7 8 6 2 0 3 1 5 16 4 } 
    // we will start the loop i = 1 to i < size; 
    // now inside the loop create temp = arr[i] to preserve it 
    // next run inner loop from j = i-1 to j >= 0 
    // if (arr[j] > temp) simply move arr[j] from j to j+1 index
    // and go to next(or previous index j--) 
    // and if (arr[j] > temp) is false then we have to end this loop (ending loop will be benificial for the case where we can have to put element at 0th index it will just save some line of code)

    int arr[] = { 9, 7, 8, 6, 2, 0, 3, 1, 5, 16, 4};
    int n = 11;

    for (int i = 1; i < n; i++) {
        int temp = arr[i];

        int j = i - 1;

        while (j >= 0 && arr[j] > temp) {
            arr[j + 1] = arr[j--];
        }

        arr[j + 1] = temp;
    }

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}


int main() {
    // Day 29 

    p1();


    return 0;
}