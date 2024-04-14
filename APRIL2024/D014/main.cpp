#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* deleteDuplicates(ListNode* head) {
    if (head == NULL || head->next == NULL) return head;

    ListNode *temp = head, *tempNext = head->next;

    while (tempNext != NULL) {
        if (temp->val != tempNext->val) {
            temp->next = tempNext;
            temp = temp->next;
        }

        tempNext = tempNext->next;
    }

    temp->next = NULL;

    return head;
}

void p1() {
    // Problem 1 : Leetcode 83. Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/ 

    ListNode *n1 = new ListNode(10, NULL);
    ListNode *n2 = new ListNode(8, n1);
    ListNode *n3 = new ListNode(8, n2);
    ListNode *n4 = new ListNode(8, n3);
    ListNode *n5 = new ListNode(1, n4);
    ListNode *headNode = new ListNode(1, n5);

    ListNode *temp = deleteDuplicates(headNode);
    while (temp != NULL) {
        cout << temp->val << " ";
        temp = temp->next;
    } cout << endl;
}


int main() {
    // Day 14 

    p1();


    return 0;
}