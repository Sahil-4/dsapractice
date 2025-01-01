#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

// A structure to represent a stack
struct Stack {
    int top;
    unsigned capacity;
    int* array;
};

// function to create a stack of given capacity. It initializes size of
// stack as 0
struct Stack* createStack(unsigned capacity) {
    struct Stack* stack = (struct Stack*) malloc(sizeof(struct Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->array = (int*) malloc(stack->capacity * sizeof(int));
    return stack;
}

// Stack is full when top is equal to the last index
int isFull(struct Stack* stack) {
    return stack->top == stack->capacity - 1;
}

// Stack is empty when top is equal to -1
int isEmpty(struct Stack* stack) {
    return stack->top == -1;
}

// Function to return the top from stack without removing it
int peek(struct Stack* stack) {
    if (isEmpty(stack)) return INT_MIN;
    return stack->array[stack->top];
}

// Function to add an item to stack.  It increases top by 1
void push(struct Stack* stack, int item) {
    if (isFull(stack)) return;
    (stack->array)[++(stack->top)] = item;
}

// Function to remove an item from stack.  It decreases top by 1
int pop(struct Stack* stack) {
    if (isEmpty(stack)) return;
    return (stack->array)[(stack->top)--];
}

void p1() {
    // Problem 1 : Geeksforgeeks - Implement Stack using Linked List - https://www.geeksforgeeks.org/problems/implement-stack-using-linked-list/1 

    struct Stack* stack = createStack(1000);
    printf("popped element :: %d\n", pop(stack));
    push(stack, 12);
    push(stack, 8);
    printf("popped element :: %d\n", pop(stack));
    push(stack, 1);
    printf("popped element :: %d\n", pop(stack));
    printf("popped element :: %d\n", pop(stack));
    push(stack, 6);
    push(stack, 22);
    push(stack, 12);
    push(stack, 56);
    printf("popped element :: %d\n", pop(stack));
    printf("popped element :: %d\n", pop(stack));
    push(stack, 56);
    printf("popped element :: %d\n", pop(stack));
    printf("popped element :: %d\n", pop(stack));
    printf("popped element :: %d\n", pop(stack));
    printf("popped element :: %d\n", pop(stack));
    printf("popped element :: %d\n", pop(stack));
    printf("popped element :: %d\n", pop(stack));
}


int main() {
    // problem 1 

    p1();


    return 0;
}
