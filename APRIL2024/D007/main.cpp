#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

bool hasCycle(ListNode *head) {
    if (head == NULL || head->next == NULL) return false;

    ListNode *slow = head;
    ListNode *fast = head->next->next;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast) return true;
    }

    return false;
}

void p1() {
    // Problem 1 : Leetcode 141. Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/ 

    ListNode *head_node = new ListNode(3);
    ListNode *node2 = new ListNode(2);
    head_node->next = node2;
    ListNode *node3 = new ListNode(0);
    node2->next= node3;
    ListNode *node4 = new ListNode(-4);
    node3->next = node4;

    node4->next = node3; // cycle 
    // node4->next = NULL; // no cycle 

    bool check = hasCycle(head_node);
    if (check) cout << "cycle" << endl;
    else cout << "no cycle" << endl;
}

int main() {
    // Day 7 

    p1();


    return 0;
}