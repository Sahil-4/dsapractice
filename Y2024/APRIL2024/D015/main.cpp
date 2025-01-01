#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

int listLength(ListNode *head) {
    int length = 0;

    ListNode *temp = head;
    while (temp != NULL) {
        length++;
        temp = temp->next;
    }

    return length;
}

ListNode* reverse(ListNode* head) {
    ListNode *prev = NULL;
    ListNode *curr = head;
    ListNode *next = head;

    while (curr != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    return prev;
}

ListNode* reverseKGroup(ListNode* head, int k) {
    int len = listLength(head);
    if (k == 0 || k == 1) return head;
    if (k == len) return reverse(head);

    ListNode *newHead = NULL;
    ListNode *tail = NULL;

    ListNode *start = head;
    ListNode *end = head;
    int i = 0;

    ListNode *temp = head;

    while (temp != NULL) {
        end = temp;
        temp = temp->next;
        i++;

        if (i == k) {
            i = 0;

            end->next = NULL;
            ListNode *n = reverse(start);
            if (newHead == NULL) newHead = n;
            if (tail != NULL) tail->next = end;

            tail = start;

            start = temp;
            end = NULL;
        }
    }

    if (tail != NULL) tail->next = start;

    return newHead;
}

void p1() {
    // Problem 1 : Leetcode 25. Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/ 

    ListNode *n4 = new ListNode(5, NULL);
    ListNode *n3 = new ListNode(4, n4);
    ListNode *n2 = new ListNode(3, n3);
    ListNode *n1 = new ListNode(2, n2);
    ListNode *headNode = new ListNode(1, n1);

    int k = 3;

    ListNode *newHead = reverseKGroup(headNode, k);
    for (int i = 0; i < 5; i++) {
        if (newHead == NULL) break;
        cout << newHead->val << " ";
        newHead = newHead->next;
    } cout << endl;
}

int main() {
    // Day 15 

    p1();


    return 0;
}