#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* reverseList_iterative(ListNode* head) {
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

ListNode* reverseList_recurdive(ListNode* node) {
    if (node == NULL || node->next == NULL) {
        return node;
    }

    ListNode *nnode = reverseList_recurdive(node->next);
    node->next->next = node;
    node->next = NULL;
    return nnode;
}

void p1() {
    // Problem 1 : Leetcode 206. Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/ 

    ListNode *head = new ListNode(1);
    ListNode *node2 = new ListNode(2);
    head->next = node2;
    ListNode *node3 = new ListNode(3);
    node2->next = node3;
    ListNode *node4 = new ListNode(4);
    node3->next = node4;
    ListNode *node5 = new ListNode(5);
    node4->next = node5;
    // node5->next = NULL;
    ListNode *node6 = new ListNode(6);
    node5->next = node6;
    node6->next = NULL;

    ListNode *temp = head;
    while (temp != NULL) {
        cout << temp->val << " ";
        temp = temp->next;
    } cout << endl;

    // ListNode *newHead = reverseList_iterative(head);
    ListNode *newHead = reverseList_recurdive(head);
    ListNode *temp2 = newHead;
    while (newHead != NULL) {
        cout << newHead->val << " ";
        newHead = newHead->next;
    } cout << endl;
}


int main() {
    // Day 6 

    p1();


    return 0;
}