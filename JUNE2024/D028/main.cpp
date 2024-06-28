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
    ListNode *temp = head;

    while (temp != NULL) {
        if (temp->next != NULL && temp->val == temp->next->val) {
            temp->next = temp->next->next;
        } else {
            temp = temp->next;
        }
    }

    return head;
}

void p1() {
    // Problem 1 : Leetcode 83. Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1 

    ListNode *head_node = new ListNode(1);
    ListNode *n2 = new ListNode(2);
    head_node->next = n2;
    ListNode *n3 = new ListNode(2);
    n2->next = n3;
    ListNode *n3 = new ListNode(3);
    n2->next = NULL;

    ListNode* tmp = deleteDuplicates(head_node);
    while (tmp != NULL) {
        cout << tmp->val << " ";
        tmp = tmp->next;
    } cout << endl;
}

int main() {
    // Day 28 

    p1();


    return 0;
}