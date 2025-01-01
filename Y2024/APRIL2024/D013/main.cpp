#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

int listLength(ListNode *head) {
    int length = 0;

    ListNode *temp = head;
    while (temp != NULL) {
        length++;
        temp = temp->next;
    }

    return length;
}

ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    // set pointers 
    ListNode *temp1 = headA;
    ListNode *temp2 = headB;
    // find length of both lists 
    int len1 = listLength(headA);
    int len2 = listLength(headB);

    // update pointer 1 will be large length 
    if (len2 > len1) {
        temp1 = headB;
        temp2 = headA;
        swap(len2, len1);
    }

    // make pointer at equal distance from end 
    while (len1 > len2) {
        temp1 = temp1->next;
        len1--;
    }

    // compare nodes and return if matches 
    while (temp1 != NULL && temp2 != NULL) {
        if (temp1 == temp2) return temp2;
        temp1 = temp1->next;
        temp2 = temp2->next;
    }

    // return null if no intersaction point found 
    return NULL;
}

void p1() {
    // Problem 1 : Leetcode 160. Intersection of Two Linked Lists - https://leetcode.com/problems/intersection-of-two-linked-lists/ 

    // list 1 
    ListNode na3 =ListNode(5, NULL);
    ListNode na2 =ListNode(3, &na3);
    ListNode na1 =ListNode(1, &na2);

    // list 2 
    ListNode nb2 =ListNode(50, NULL);
    ListNode nb1 =ListNode(10, &nb2);

    // intersection nodes 
    ListNode nc3 =ListNode(10);
    ListNode nc2 =ListNode(9, &nc3);
    ListNode nc1 =ListNode(8, &nc2);

    // making intersection 
    na3.next = &nc1;
    nb2.next = &nc1;

    ListNode *inter = getIntersectionNode(&na1, &nb1);
    if (inter == &nc1) cout << "correct ans" << endl;
    else cout << "incorrect ans" << endl;
}

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode *dummy = new ListNode(0);
    int carry = 0;

    ListNode *temp = dummy;

    while (l1 != NULL || l2 != NULL || carry != 0) {
        int a = l1 ? l1->val : 0;
        int b = l2 ? l2->val : 0;

        int sum = a + b + carry;
        int d = sum % 10;
        carry = sum / 10;

        temp->next = new ListNode(d);
        temp = temp->next;

        l1 = l1 ? l1->next : nullptr;
        l2 = l2 ? l2->next : nullptr;
    }

    ListNode *ans = dummy->next;
    delete dummy;
    return ans;
}

void p2() {
    // Problem 2 : Leetcode 2. Add Two Numbers - https://leetcode.com/problems/add-two-numbers/ 

    // list 1 
    ListNode na4 =ListNode(9, NULL);
    ListNode na3 =ListNode(9, &na4);
    ListNode na2 =ListNode(9, &na3);
    ListNode na1 =ListNode(9, &na2);

    // list 2 
    ListNode nb2 =ListNode(9, NULL);
    ListNode nb1 =ListNode(9, &nb2);

    // answer 
    ListNode *ans = addTwoNumbers(&na1, &nb1);
    while (ans != NULL) {
        cout << ans->val << " ";
        ans = ans->next;
    } cout << endl;
}


int main() {
    // Day 13 

    p1();

    p2();


    return 0;
}