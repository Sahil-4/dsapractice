#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* deleteMiddle_solution1(ListNode* head) {
    if (head->next == NULL) return NULL;

    int length = 0;
    ListNode *temp = head;
    while (temp != NULL) {
        length++;
        temp = temp->next;
    }

    int deleteNode = length / 2;
    temp = head;
    for (int i = 1; i < deleteNode; i++) temp = temp->next;

    temp->next = temp->next->next;

    return head;
}

ListNode* deleteMiddle(ListNode* head) {
    if (head->next == NULL) return NULL;
    if (head->next->next == NULL) {
        head->next = NULL;
        return head;
    }

    ListNode *slow = head;
    ListNode *fast = head->next->next;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next;
        fast = fast->next;
    }

    slow->next = slow->next->next;

    return head;
}

void p1() {
    // Problem 1 : Leetcode 2095. Delete the Middle Node of a Linked List - https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/ 

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

    // ListNode *temp = deleteMiddle_solution1(head_node);
    ListNode *temp = deleteMiddle(head_node);
    while (temp != NULL) {
        cout << temp->val << " ";
        temp = temp->next;
    } cout << endl;
}

int main() {
    // Day 11 

    p1();


    return 0;
}