#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

ListNode *detectCycle(ListNode *head) {
    if (head == NULL || head->next == NULL) return NULL;

    ListNode *slow = head;
    ListNode *fast = head;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;

        if (fast == slow) break;
    }

    if (fast == NULL || fast->next == NULL) return NULL;

    ListNode *temp = head;
    while (temp != slow) {
        temp = temp->next;
        slow = slow->next;
    }

    return temp;
}

void p1() {
    // Problem 1 : Leetcode 142. Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/ 

    ListNode *head_node = new ListNode(3);
    ListNode *node2 = new ListNode(2);
    head_node->next = node2;
    ListNode *node3 = new ListNode(0);
    node2->next= node3;
    ListNode *node4 = new ListNode(-4);
    node3->next = node4;

    node4->next = node3; // cycle 
    // node4->next = NULL; // no cycle 

    ListNode *start = detectCycle(head_node);
    if (start != NULL) cout << "cycle starts at : " << start->val << endl;
    else cout << "no cycle" << endl;
}


int main() {
    // Day 8 

    p1();


    return 0;
}