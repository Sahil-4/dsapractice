#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode *sumList = NULL;
    ListNode *sumListTemp = NULL;
    int carry = 0;

    while (l1 != NULL || l2 != NULL || carry != 0) {
        int sum = carry;

        if (l1 != NULL) {
            sum += l1->val;
            l1 = l1->next;
        }
        if (l2 != NULL) {
            sum += l2->val;
            l2 = l2->next;
        }

        carry = sum / 10;
        sum = sum % 10;

        ListNode *n = new ListNode(sum);
        if (sumList == NULL) {
            sumList = n;
            sumListTemp = sumList;
        } else {
            sumListTemp->next = n;
            sumListTemp = sumListTemp->next;
        }
    }

    return sumList;
}

void p1() {
    // Problem 1 : Leetcode 2. Add Two Numbers - https://leetcode.com/problems/add-two-numbers/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1 

    // Number 4961 
    ListNode *l1_4 = new ListNode(4);
    ListNode *l1_3 = new ListNode(9, l1_4);
    ListNode *l1_2 = new ListNode(6, l1_3);
    ListNode *l1_head = new ListNode(1, l1_2);

    // Number 945 
    ListNode *l2_3 = new ListNode(9);
    ListNode *l2_2 = new ListNode(4, l2_3);
    ListNode *l2_head = new ListNode(5, l2_2);

    // Number 6095
    ListNode *l3_head = addTwoNumbers(l1_head, l2_head);
    while (l3_head != NULL) {
        cout << l3_head->val << " ";
        l3_head = l3_head->next;
    } cout << endl;
}

ListNode *reverseList(ListNode *head) {
    ListNode *current = head;
    ListNode *next = head;
    ListNode *prev = NULL;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

ListNode* reverseKGroup(ListNode* listPointer, int k) {
    if (k == 1) return listPointer;

    ListNode *new_head = NULL;
    ListNode *new_tail = listPointer;

    ListNode *start = listPointer;
    int nodesCount = 1;

    while (listPointer != NULL) {
        if (nodesCount == k) {
            ListNode *nnext = listPointer->next;
            listPointer->next = NULL;

            ListNode *nrev = reverseList(start);

            if (new_head == NULL) new_head = nrev;
            else new_tail->next = nrev;

            new_tail = start;
            start->next = nnext;

            start = nnext;

            listPointer = nnext;
            nodesCount = 1;
        } else {
            listPointer = listPointer->next;
            nodesCount++;
        }
    }

    return new_head;
}

void p2() {
    // Problem 2 : Leetcode 25. Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1 

    ListNode *n4 = new ListNode(4);
    ListNode *n3 = new ListNode(9, n4);
    ListNode *n2 = new ListNode(6, n3);
    ListNode *head = new ListNode(1, n2);

    int k = 3;

    ListNode *temp_head = reverseKGroup(head, k);
    while (temp_head != NULL) {
        cout << temp_head->val << " ";
        temp_head = temp_head->next;
    } cout << endl;
}

int main() {
    // Day 29 

    p1();

    p2();


    return 0;
}