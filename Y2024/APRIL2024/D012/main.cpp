#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* middleNode(ListNode *head) {
    ListNode *slow = head, *fast = head;

    while (fast->next != NULL && fast->next->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }

    return slow;
}

ListNode* merge(ListNode *list1, ListNode *list2) {
    if (list1 == NULL) return list2;
    if (list2 == NULL) return list1;

    ListNode* n = NULL;

    if (list1->val <= list2->val) {
        n = list1;
        n->next = merge(list1->next, list2);
    } else {
        n = list2;
        n->next = merge(list1, list2->next);
    }

    return n;
}

ListNode* mergeSort(ListNode *head) {
    if (head == NULL || head->next == NULL) return head;

    ListNode *mid = middleNode(head);

    ListNode *list1 = head;
    ListNode *list2 = mid->next;
    mid->next = NULL;

    list1 = mergeSort(list1);
    list2 = mergeSort(list2);

    return merge(list1, list2);
}

ListNode* sortList(ListNode* head) {
    return mergeSort(head);
}

void p1() {
    // Problem 1 : Leetcode 148. Sort List - https://leetcode.com/problems/sort-list/ 

    ListNode *head_node = new ListNode(2);
    ListNode *node2 = new ListNode(3);
    head_node->next = node2;
    ListNode *node3 = new ListNode(5);
    node2->next= node3;
    ListNode *node4 = new ListNode(1);
    node3->next = node4;
    ListNode *node5 = new ListNode(-5);
    node4->next = node5;

    node5->next = NULL;

    ListNode *temp = sortList(head_node);
    while (temp != NULL) {
        cout << temp->val << " ";
        temp = temp->next;
    } cout << endl;
}


int main() {
    // Day 12 

    p1();


    return 0;
}