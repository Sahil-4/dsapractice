//{ Driver Code Starts
//Initial Template for C
#include <stdio.h>
#include <stdlib.h>

// A linked list (LL) node to store a queue entry
struct QNode {
	int key;
	struct QNode* next;
};

// The queue, front stores the front node of LL and rear stores the
// last node of LL
struct Queue {
	struct QNode *front, *rear;
};

// A utility function to create a new linked list node.
struct QNode* newNode(int k)
{
	struct QNode* temp = (struct QNode*)malloc(sizeof(struct QNode));
	temp->key = k;
	temp->next = NULL;
	return temp;
}

// A utility function to create an empty queue
struct Queue* createQueue()
{
	struct Queue* q = (struct Queue*)malloc(sizeof(struct Queue));
	q->front = q->rear = NULL;
	return q;
}

// The function to add a key k to q
void push(struct Queue* q, int k);

// Function to remove a key from given queue q
void pop(struct Queue* q);

// } Driver Code Ends

//User function Template for C

// The function to add a key k to q
void push(struct Queue* q, int k) {
    if (q->front == NULL) {
        q->front = newNode(k);
        q->rear = q->front;
        return;
    }

    q->rear->next = newNode(k);
    q->rear = q->rear->next;
}

// Function to remove a key from given queue q
void pop(struct Queue* q) {
    if (q->front == NULL) return;

    q->front = q->front->next;
    if (q->front == NULL) q->rear = NULL;
}

// Driver Program to test anove functions
void test() {
    int T;
    scanf("%d",&T);

    while(T--) {
        struct Queue* q = createQueue();

        int Q;
        scanf("%d",&Q);

        while(Q--){
            int QueryType=0;
            scanf("%d",&QueryType);

            if(QueryType==1) {
                int a;
                scanf("%d",&a);
                push(q, a);
            }else if(QueryType==2) {
                if(q->front!=NULL) printf("%d ", q->front->key);
                else printf("-1 ");
                pop(q);
            }
        }
        printf("\n");
    }
}

void p1() {
    // Problem 1 : Geeksforgeeks - Implement Queue using Linked List - https://www.geeksforgeeks.org/problems/implement-queue-using-linked-list/1 

    test();
}

int main() {
    // Day 11 - problem 1 

    p1();


    return 0;
}