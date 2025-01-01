#include <stdio.h>

// User function Template for C

// A structure to represent a stack
struct Stack {
    int top;
    unsigned capacity;
    int* array;
};

struct Stack* createStack(unsigned capacity) {
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->array = (int*)malloc(stack->capacity * sizeof(int));
    return stack;
}

//Function to push an integer into the stack.
void push_Stack(struct Stack* stack, int item) {
    //code here
    if (stack->top == stack->capacity - 1) return;
    (stack->array)[++(stack->top)] = item;
}

//Function to remove an item from top of the stack.
int pop_Stack(struct Stack* stack) {
    //code here
    if (stack->top == -1) return -1;
    return (stack->array)[(stack->top)--];
}

void p1() {
    // Problem 1 : Geeksforgeeks - Implement stack using array - https://www.geeksforgeeks.org/problems/implement-stack-using-array/1 

    struct Stack *stack = createStack(5);
    printf("popped item :: %d", pop_Stack(stack));
    push_Stack(stack, 12);
    printf("popped item :: %d", pop_Stack(stack));
    push_Stack(stack, 1);
    push_Stack(stack, 2);
    push_Stack(stack, 5);
    printf("popped item :: %d", pop_Stack(stack));
    printf("popped item :: %d", pop_Stack(stack));
    printf("popped item :: %d", pop_Stack(stack));
    printf("popped item :: %d", pop_Stack(stack));
}

// User function Template for C

// A structure to represent a queue
struct Queue {
    unsigned capacity;
    int* arr;
    int front;
    int rear;
};

struct Queue* createQueue(unsigned capacity) {
    struct Queue* queue = (struct Queue*)malloc(sizeof(struct Queue));
    queue->capacity = capacity;
    queue->front = 0;
    queue->rear = -1;
    queue->arr = (int*)malloc(queue->capacity * sizeof(int));
    return queue;
}

//Function to push an element x in a queue.
void push_Queue(struct Queue* queue, int x) {
    // Your Code 
    queue->arr[++queue->rear] = x;
}

//Function to pop an element from queue and return that element.
int pop_Queue(struct Queue* queue) {
    // Your Code 
    if (queue->front >= queue->rear) return -1;
    return queue->arr[queue->front++];
}

void p2() {
    // Problem 2 : Geeksforgeeks - Implement Queue using array - https://www.geeksforgeeks.org/problems/implement-queue-using-array/1 

    struct Queue *q = createQueue(10);

    // pop, add, pop, pop, add, add, add, pop 

    printf("popped item :: %d", pop_Queue(q));
    push_Queue(q, 5);
    printf("popped item :: %d", pop_Queue(q));
    push_Queue(q, 3);
    printf("popped item :: %d", pop_Queue(q));
    printf("popped item :: %d", pop_Queue(q));
    push_Queue(q, 1);
    printf("popped item :: %d", pop_Queue(q));
    push_Queue(q, 5);
    push_Queue(q, 0);
    push_Queue(q, 1);
    printf("popped item :: %d", pop_Queue(q));
    printf("popped item :: %d", pop_Queue(q));
    printf("popped item :: %d", pop_Queue(q));
}

void p3() {
    // Problem 3 : Leetcode 232. Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/description/ 

    // CHECK OUT p3.c file 
}

void p4() {
    // Problem 4 : Leetcode 225. Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/description/ 

    // CHECK OUT p4.c file 
}

int main() {
    // Day 9 

    p1();

    p2();

    p3();

    p4();


    return 0;
}