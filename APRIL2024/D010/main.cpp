#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* oddEvenList(ListNode* head) {
    if (head == NULL) return head;
    if (head->next == NULL || head->next->next == NULL) return head;

    ListNode* n1 = head;
    ListNode* n2 = head->next;

    ListNode* even_head = head->next;

    while (n2 != NULL && n2->next != NULL) {
        n1->next = n2->next;
        n1 = n1->next;

        n2->next = n1->next;
        n2 = n2->next;
    }

    n1->next = even_head;

    return head;
}

void p1() {
    // Problem 1 : Leetcode 328. Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/ 

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

    ListNode *newHead = oddEvenList(head_node);

    ListNode *temp = newHead;
    while (temp != NULL) {
        cout << temp->val << " ";
        temp = temp->next;
    } cout << endl;
}

int lengthOfLinkedList(ListNode* head) {
    ListNode *temp = head;
    int length = 0;

    while (temp != NULL) {
        length++;
        temp = temp->next;
    }

    return length;
}

ListNode* removeNthFromEnd(ListNode* head, int n) {
    int len = lengthOfLinkedList(head);
    int toDelete = len - n;

    if (head->next == NULL) return NULL;
    if (toDelete == 0) return head->next;

    ListNode *temp = head;
    for (int i = 1; i < toDelete; i++) {
        temp = temp->next;
    }

    temp->next = temp->next->next;

    return head;
}

void p2() {
    // Problem 2 : Leetcode 19. Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/ 

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

    ListNode *newHead = removeNthFromEnd(head_node, 5);

    ListNode *temp = newHead;
    while (temp != NULL) {
        cout << temp->val << " ";
        temp = temp->next;
    } cout << endl;
}


int main() {
    // Day 10 

    p1();

    p2();


    return 0;
}