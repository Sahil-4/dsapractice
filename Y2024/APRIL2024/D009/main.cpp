#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

ListNode *reverse(ListNode *head) {
    ListNode *curr = head;
    ListNode *prev = NULL;
    ListNode *next = head;

    while (curr != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    return prev;
}

ListNode *middle(ListNode *head) {
    ListNode *hare = head, *tortoise = head;

    while (hare->next != NULL && hare->next->next != NULL) {
        tortoise = tortoise->next;
        hare = hare->next->next;
    }

    return tortoise;
}

bool compare(ListNode *nodehead1, ListNode *nodehead2) {
    ListNode *temp1 = nodehead1, *temp2 = nodehead2;

    while (temp1 != NULL && temp2 != NULL) {
        if (temp1->val != temp2->val) return false;

        temp1 = temp1->next;
        temp2 = temp2->next;
    }

    return true;
}

bool isPalindrome(ListNode* head) {
    if (head == NULL || head->next == NULL) return true;

    ListNode *mid = middle(head);
    ListNode *newMidNext = reverse(mid->next);
    mid->next = NULL;

    bool check =  compare(head, newMidNext);

    ListNode *newMidNext2 = reverse(newMidNext);
    mid->next = newMidNext2;

    return check;
}

void p1() {
    // Problem 1 : Leetcode 234. Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/ 

    ListNode *head_node = new ListNode(1);
    ListNode *node2 = new ListNode(2);
    head_node->next = node2;
    ListNode *node3 = new ListNode(2);
    node2->next= node3;
    ListNode *node4 = new ListNode(1);
    node3->next = node4;

    node4->next = NULL;

    ListNode *node5 = new ListNode(1);
    node5->next = node3;
    node2->next= node5;

    bool check = isPalindrome(head_node);
    cout << "palindrome : " << check << endl;

    ListNode *temp = head_node;
    while (temp != NULL) {
        cout << "temp->val : " << temp->val << endl;
        temp = temp->next;
    } cout << endl;
}


int main() {
    // Day 10 

    p1();


    return 0;
}