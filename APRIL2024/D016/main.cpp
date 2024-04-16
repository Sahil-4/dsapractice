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

ListNode* rotateRight(ListNode* head, int k) {
    if (head == NULL || head->next == NULL) return head;

    int len = listLength(head);
    k = k % len;

    if (k == 0) return head;

    ListNode *temp = head;
    for (int i = 1; i < len - k; i++) temp = temp->next;

    ListNode *list2 = temp->next;
    temp->next = NULL;

    ListNode *temp2 = list2;
    while (temp2->next != NULL) temp2 = temp2->next;

    temp2->next = head;

    return list2;
}

void p1() {
    // Problem 1 : Leetcode 61. Rotate List - https://leetcode.com/problems/rotate-list/ 

    ListNode *n6 = new ListNode(7, NULL);
    ListNode *n5 = new ListNode(6, n6);
    ListNode *n4 = new ListNode(5, n5);
    ListNode *n3 = new ListNode(4, n4);
    ListNode *n2 = new ListNode(3, n3);
    ListNode *n1 = new ListNode(2, n2);
    ListNode *headNode = new ListNode(1, n1);

    int k = 3;

    ListNode *newHead = rotateRight(headNode, k);
    while (newHead != NULL) {
        cout << newHead->val << " ";
        newHead = newHead->next;
    } cout << endl;
}

int main() {
    // Day 16 

    p1();


    return 0;
}