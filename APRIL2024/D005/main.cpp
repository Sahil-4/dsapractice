#include <iostream>

using namespace std;


/*
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
*/

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


void deleteNode(ListNode* node) {
    ListNode *temp = node;

    while (temp->next != NULL) {
        temp->val = temp->next->val;

        if (temp->next->next == NULL) temp->next = NULL;
        else temp = temp->next;
    }
}

void p1() {
    // Problem 1 : Leetcode 237. Delete Node in a Linked List - https://leetcode.com/problems/delete-node-in-a-linked-list/ 

    ListNode *head_node = new ListNode(4);
    ListNode *node2 = new ListNode(5);
    head_node->next = node2;
    ListNode *node3 = new ListNode(1);
    node2->next= node3;
    ListNode *node4 = new ListNode(9);
    node3->next = node4;

    node4->next = NULL;

    deleteNode(head_node->next);

    ListNode *temp = head_node;

    while (temp != NULL) {
        cout << temp->val << " ";
        temp = temp->next;
    } cout << endl;
}

ListNode* middleNode(ListNode* head) {
    ListNode *fast = head;
    ListNode *slow = head;

    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        slow = slow->next;
    }

    return slow;
}

void p2() {
    // Problem 2 : Leetcode 876. Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/ 

    ListNode *head_node = new ListNode(1);
    ListNode *node2 = new ListNode(2);
    head_node->next = node2;
    ListNode *node3 = new ListNode(3);
    node2->next= node3;
    ListNode *node4 = new ListNode(4);
    node3->next = node4;
    ListNode *node5 = new ListNode(5);
    node4->next = node5;
    node5->next = NULL;
    ListNode *node6 = new ListNode(6);
    node5->next = node6;
    node6->next = NULL;

    ListNode *middle = middleNode(head_node);
    cout << middle->val << endl;
}

int main() {
    // Day 5 

    p1();

    p2();


    return 0;
}