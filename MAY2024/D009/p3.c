#include <stdio.h>
#include <stdbool.h>

// A structure to represent a stack
typedef struct {
    int top;
    unsigned capacity;
    int* array;
} Stack;

Stack* createStack(unsigned capacity) {
    Stack* stack = (Stack*) malloc(sizeof(Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->array = (int*)malloc(stack->capacity * sizeof(int));
    return stack;
}

bool isEmpty_Stack(Stack* stack) {
    if (stack->top == -1) return true;
    return false;
}

//Function to push an integer into the stack.
void push_Stack(Stack* stack, int item) {
    //code here
    if (stack->top == stack->capacity - 1) return;
    (stack->array)[++(stack->top)] = item;
}

//Function to remove an item from top of the stack.
int pop_Stack(Stack* stack) {
    //code here
    if (isEmpty_Stack(stack)) return -1;
    return (stack->array)[(stack->top)--];
}

int top_Stack(Stack* stack) {
    if (isEmpty_Stack(stack)) return -1;
    return (stack->array)[stack->top];
}

// Queue structure 
typedef struct {
    Stack *input;
    Stack *output;
    int capacity;
} MyQueue;

// fucntion to create a new queue 
MyQueue* myQueueCreate() {
    MyQueue *q = (MyQueue*) malloc(sizeof(MyQueue));

    q->capacity = 100;

    q->input = createStack(q->capacity);
    q->output = createStack(q->capacity);

    return q;
}

// perform push operation in queue obj, with argument x 
void myQueuePush(MyQueue* obj, int x) {
    push_Stack(obj->input, x);
}

// perform pop operation in queue obj
int myQueuePop(MyQueue* obj) {
    if (!isEmpty_Stack(obj->output)) {
        return pop_Stack(obj->output);
    } else {
        while (!isEmpty_Stack(obj->input)) {
            push_Stack(obj->output, pop_Stack(obj->input));
        }
        return pop_Stack(obj->output);
    }
}

// perform peek operation in queue obj
int myQueuePeek(MyQueue* obj) {
    if (!isEmpty_Stack(obj->output)) {
        return top_Stack(obj->output);
    } else {
        while (!isEmpty_Stack(obj->input)) {
            push_Stack(obj->output, pop_Stack(obj->input));
        }
        return top_Stack(obj->output);
    }
}

// return true if queue obj is empty 
bool myQueueEmpty(MyQueue* obj) {
    if (isEmpty_Stack(obj->input) && isEmpty_Stack(obj->output)) return true;
    return false;
}

// free allocated memory 
void myQueueFree(MyQueue* obj) {
    free(obj->input);
    free(obj->output);
    free(obj);
}

/**
 * Your MyQueue struct will be instantiated and called as such:
 * MyQueue* obj = myQueueCreate();
 * myQueuePush(obj, x);
 
 * int param_2 = myQueuePop(obj);
 
 * int param_3 = myQueuePeek(obj);
 
 * bool param_4 = myQueueEmpty(obj);
 
 * myQueueFree(obj);
*/

void p3() {
    // Problem 3 : Leetcode 232. Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/description/ 

    // create Queue 
    MyQueue *q = myQueueCreate();
    myQueuePush(q, 12);
    myQueuePush(q, 78);
    myQueuePush(q, 10);
    myQueuePush(q, 14);
    printf("top :: %d\n", myQueuePeek(q));
    printf("popped element :: %d\n", myQueuePop(q));
    printf("popped element :: %d\n", myQueuePop(q));
    myQueueFree(q);
}

int main() {
    // Day 9 - p3 

    p3();


    return 0;
}