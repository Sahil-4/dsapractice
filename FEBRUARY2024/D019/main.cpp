#include <iostream>

using namespace std;

int majorityElement(int a[], int size) {
    // your code here 
    
    // {1,2,3} 
    // {3,1,3,3,2} 
    // logic : optimal approach 
    // Moore's Voting Algo
    // if think deeply 
    // we can say that we have to deal with two types of element 
    // Type 1 will contain one element that is occurred more then n/2 
    // Type 2 will contain other elements that ic not occurred more then n/2 or may be occurred once or twice or thrice 
    // what if we devide all elements into these two categories 
    // we can keep track of element 
    // and count of this element 
    // initially we will assume element as null 
    // and count as 0 
    // we will traverse through the array 
    // and if the count is zero at any point 
    // we will simply set element as current element and increase the count by 1 
    // if count is not 0 we will compare element and current element 
    // if both are same then we will increase the count by 1 
    // if both are not same we will simply decrease the count by 1 
    // if we are sure that we must have a majority element in our array 
    // then we can simply return the element as this will be our answer 
    // if we are not sure about it 
    // we will have to traverse the array again 
    // and we will have to count the occurrence of element in array 
    // if occurrence is more then n/2 
    // then we will return element 
    // else we will return -1 as we dont have any majority element in array 

    int element = -1;
    int count = 0;

    for (int i = 0; i < size; i++) {
        if (count == 0) {
            element = a[i];
            count++;
        } else if (element == a[i]) {
            count++;
        } else {
            count--;
        }
    }

    // return element;

    int occurrence = 0;
    for (int i = 0; i < size; i++) {
        if (element == a[i]) occurrence++;
        if (occurrence > size/2) return element;
    }

    return -1;
}

void p1() {
    // Problem 1 : Majority Element - https://www.geeksforgeeks.org/problems/majority-element-1587115620/1 

    int arr[] = {3,1,3,3,2};
    int size = sizeof(arr) / sizeof(arr[0]);

    int mjEl = majorityElement(arr, size);

    cout << mjEl << endl;
}

int main() {
    // Day 019 

    p1();


    return 0;
}