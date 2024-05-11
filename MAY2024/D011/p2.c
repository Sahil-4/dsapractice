#include <stdio.h>
#include <limits.h>

// Stack structure 
typedef struct {
    unsigned capacity;
    long long *array;
    int top;
    long long minVal;
} MinStack;

// function to create new stack 
MinStack* minStackCreate() {
    MinStack *minS = (MinStack*) malloc(sizeof(MinStack));
    minS->top = -1;
    minS->capacity = 30000;
    minS->minVal = INT_MAX;
    minS->array = (int*) malloc(sizeof(int) * minS->capacity);
    return minS;
}

// push val into stack 
void minStackPush(MinStack* obj, int val) {
    if (obj->top == obj->capacity) return;

    if (obj->top == -1) {
        (obj->array)[++(obj->top)] = val;
        obj->minVal = val;
    } else if (val < obj->minVal) {
        long long y = 1LL * val - obj->minVal + val;
        (obj->array)[++(obj->top)] = y;
        obj->minVal = val;
    } else {
        (obj->array)[++(obj->top)] = val;
    }
}

// pop value from stack 
void minStackPop(MinStack* obj) {
    if (obj->top == -1) return;

    long long topElement = (obj->array)[(obj->top)--];
    if (topElement < obj->minVal) obj->minVal = 2 * obj->minVal - topElement;
}

// get the top element of stack 
int minStackTop(MinStack* obj) {
    if (obj->top == -1) return -1;

    long long topElement = (obj->array)[obj->top];
    if (topElement < obj->minVal) return obj->minVal;
    return topElement;
}

int minStackGetMin(MinStack* obj) {
    if (obj->top == -1) return -1;
    return obj->minVal;
}

void minStackFree(MinStack* obj) {
    free(obj->array);
    free(obj);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * MinStack* obj = minStackCreate();
 * minStackPush(obj, val);
 
 * minStackPop(obj);
 
 * int param_3 = minStackTop(obj);
 
 * int param_4 = minStackGetMin(obj);
 
 * minStackFree(obj);
*/

void p2() {
    // Problem 2 : Leetcode 155. Min Stack - https://leetcode.com/problems/min-stack/ 

    MinStack* obj = minStackCreate();
    minStackPush(obj, 5);
    minStackPush(obj, 55);
    minStackPush(obj, 2);
    minStackPush(obj, 25);
    minStackPop(obj);
    int param_3 = minStackTop(obj);
    int param_4 = minStackGetMin(obj);
    minStackFree(obj);
}

int main() {
    // Day 11 - problem 2 

    p2();


    return 0;
}