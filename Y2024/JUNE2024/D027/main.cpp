#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* nodeBefreMidNode(ListNode *head) {
    ListNode *slow = head, *fast = head;

    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;

        if (fast == NULL || fast->next == NULL) return slow;
        slow = slow->next;
    }

    return slow;
}

ListNode* deleteMiddle(ListNode *head) {
    if (head->next == NULL) return NULL;

    ListNode *mid_prev = nodeBefreMidNode(head);
    mid_prev->next = mid_prev->next->next;

    return head;

    // Complexity analysis : 
    // Time : O(n) 
    // Space : O(1) 
}

void p1() {
    // Problem 1 : Leetcode 2095. Delete the Middle Node of a Linked List - https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/delete-middle-of-linked-list/1 

    ListNode *head_node = new ListNode(1);
    ListNode *n2 = new ListNode(2);
    head_node->next = n2;
    n2->next = NULL;

    ListNode* tempHead = deleteMiddle(head_node);
    while (tempHead != NULL) {
        cout << tempHead->val << " ";
        tempHead = tempHead->next;
    } cout << endl;
}


int main() {
    // Day 27 

    p1();


    return 0;
}