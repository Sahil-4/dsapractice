#include <stdio.h>
#include <stdbool.h>

typedef struct {
    int top;
    unsigned capacity;
    char* array;
} Stack;

Stack* createStack(unsigned capacity) {
    Stack* stack = (Stack*) malloc(sizeof(Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->array = (char*) malloc(stack->capacity * sizeof(char));
    return stack;
}

void push(Stack* stack, char item) {
    if (stack->top > 0 && stack->top >= stack->capacity) return;
    (stack->array)[++(stack->top)] = item;
}

char pop(Stack* stack) {
    if (stack->top < 0) return -1;
    return (stack->array)[(stack->top)--];
}

char top(Stack* stack) {
    if (stack->top < 0) return -1;
    return (stack->array)[(stack->top)];
}

bool isEmpty(Stack* stack) {
    return stack->top == -1;
}

bool isValid(char* s) {
    Stack *stack = createStack(strlen(s) * sizeof(char));

    int it = 0;
    while (s[it] != '\0') {
        char ch = s[it];

        if (ch == '(' || ch == '[' || ch == '{') {
            push(stack, ch);
        } else if (ch == ')' || ch == ']' || ch == '}') {
            if (ch == ')' && top(stack) == '(') pop(stack);
            else if (ch == ']' && top(stack) == '[') pop(stack);
            else if (ch == '}' && top(stack) == '{') pop(stack);
            else push(stack, ch);
        }

        it++;
    }

    if (isEmpty(stack)) return true;
    return false;
}

void p2() {
    // Problem 2 : Leetcode 20. Valid Parentheses - https://leetcode.com/problems/valid-parentheses/ 

    char *s = "((({{{[[[[[]((({{{[[[[[]]]]]}}})))]]]]}}})))";
    printf("is string valid parentheses :: %d", isValid(s));
}

int main() {
    // problem 2 

    p2();


    return 0;
}