#include <stdio.h>
#include <stdbool.h>

// A structure to represent a queue
typedef struct {
    unsigned capacity;
    int* arr;
    int front;
    int rear;
} Queue;

Queue* createQueue(unsigned capacity) {
    Queue* queue = (Queue*) malloc(sizeof(Queue));
    queue->capacity = capacity;
    queue->front = queue->rear = 0;
    queue->arr = (int*) malloc(queue->capacity * sizeof(int));
    return queue;
}

bool isEmpty_Queue(Queue* queue) {
    if (queue->front == queue->rear) return true;
    return false;
}

//Function to push an element x in a queue.
void push_Queue(Queue* queue, int x) {
    queue->arr[queue->rear++] = x;
}

//Function to pop an element from queue and return that element.
int pop_Queue(Queue* queue) {
    return queue->arr[queue->front++];
}

//Function to return top element.of queue 
int top_Queue(Queue* queue) {
    if (isEmpty_Queue(queue)) return -1;
    return queue->arr[queue->front];
}

void free_Queue(Queue* queue) {
    free(queue->arr);
    free(queue);
}

typedef struct {
    Queue* primary;
    Queue* secondary;
    unsigned capacity;
} MyStack;

MyStack* myStackCreate() {
    MyStack *stk = (MyStack*) malloc(sizeof(MyStack));
    stk->capacity = 100;
    stk->primary = createQueue(stk->capacity);
    stk->secondary = createQueue(stk->capacity);
    return stk;
}

bool myStackEmpty(MyStack* obj) {
    if (isEmpty_Queue(obj->primary)) return true;
    return false;
}

void myStackPush(MyStack* obj, int x) {
    push_Queue(obj->primary, x);
}

int myStackPop(MyStack* obj) {
    // if stack is already empty 
    if (myStackEmpty(obj)) return -1;
    int popped = -1;

    // move all elements except one from primary to secondary 
    while (!isEmpty_Queue(obj->primary)) {
        int el = pop_Queue(obj->primary);
        if (isEmpty_Queue(obj->primary)) {
            popped = el;
            break;
        }
        push_Queue(obj->secondary, el);
    }

    while (!isEmpty_Queue(obj->secondary)) {
        int el = pop_Queue(obj->secondary);
        push_Queue(obj->primary, el);
    }

    return popped;
}

int myStackTop(MyStack* obj) {
    // if stack is already empty 
    if (myStackEmpty(obj)) return -1;
    int top = -1;

    // move all elements except one from primary to secondary 
    while (!isEmpty_Queue(obj->primary)) {
        int el = pop_Queue(obj->primary);
        push_Queue(obj->secondary, el);
        top = el;
    }

    while (!isEmpty_Queue(obj->secondary)) {
        int el = pop_Queue(obj->secondary);
        push_Queue(obj->primary, el);
    }

    return top;
}

void myStackFree(MyStack* obj) {
    free_Queue(obj->primary);
    free_Queue(obj->secondary);
    free(obj);
}

/**
 * Your MyStack struct will be instantiated and called as such:
 * MyStack* obj = myStackCreate();
 * myStackPush(obj, x);
 
 * int param_2 = myStackPop(obj);
 
 * int param_3 = myStackTop(obj);
 
 * bool param_4 = myStackEmpty(obj);
 
 * myStackFree(obj);
*/

void p4() {
    // Problem 4 : Leetcode 225. Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/description/ 

    // ["MyStack","push","push","top","pop","empty"]

    MyStack *stack = myStackCreate();
    int e;
    myStackPush(stack, 12);
    myStackPush(stack, 15);
    myStackPush(stack, 16);
    e = myStackTop(stack);
    printf("top :: %d\n", e);
    e = myStackPop(stack);
    printf("top :: %d\n", e);
    e = myStackTop(stack);
    printf("top :: %d\n", e);
    myStackFree(stack);
}

int main() {
    // Day 9 - p4 

    p4();


    return 0;
}