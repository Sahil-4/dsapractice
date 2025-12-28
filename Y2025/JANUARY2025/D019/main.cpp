#include <bits/stdc++.h>

using namespace std;


class ListNode {
public:
    int val;
    ListNode* next;

    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}

    ListNode* setNext(int x) {
        this->next = new ListNode(x);
        this->next;
    }

    void print() {
        ListNode* temp = this;
        cout << "printing linked list" << endl;
        while (temp != nullptr) {
            cout << temp->val << " ";
            temp = temp->next;
        }
        cout << endl;
    }
};

class Problem1 {
    int listLen(ListNode* head) {
        int len = 0;
        while (head != nullptr) {
            len++;
            head = head->next;
        }
        return len;
    }

    vector<ListNode*> reverse(ListNode* head) {
        ListNode* ntail = head;

        ListNode* prev = nullptr;
        ListNode* next = nullptr;
        ListNode* curr = head;

        while (curr != nullptr) {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }

        return { prev, ntail };
    }

public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        int len = listLen(head);

        if (len == 0 || len == 1 || k == 1) return head;

        ListNode* nhead = nullptr;
        ListNode* htemp = head;

        ListNode* ttemp = head;
        ListNode* ltail = nullptr;

        for (int i = 0, c = 1; i < len; i++, c++) {
            ListNode* next = ttemp->next;

            if (c == k) {
                ttemp->next = nullptr;

                vector<ListNode*> ht = reverse(htemp);

                if (nhead == nullptr) nhead = ht[0];
                if (ltail != nullptr) ltail->next = ht[0];

                ht[1]->next = next;
                ltail = ht[1];
                htemp = next;
                c = 0;
            }

            ttemp = next;
        }

        return nhead;

        // Complexity analysis 
        // Time : O(N) + O(N^2) 
        // Space : O(1) 
    }
};

void p1() {
    // Problem 1 : Leetcode 25. Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1 

    ListNode* head = new ListNode(0);
    head->setNext(1)->setNext(2)->setNext(3)->setNext(4)->setNext(5); // ->setNext(6);

    // ListNode* nhead = Problem1().reverseKGroup(head, 1);
    // ListNode* nhead = Problem1().reverseKGroup(head, 2);
    // ListNode* nhead = Problem1().reverseKGroup(head, 3);
    // ListNode* nhead = Problem1().reverseKGroup(head, 4);
    ListNode* nhead = Problem1().reverseKGroup(head, 5);
    nhead->print();
}

class Problem2 {
    int listLen(ListNode* head) {
        int len = 0;
        while (head != nullptr) {
            len++;
            head = head->next;
        }
        return len;
    }

    ListNode* solve1(ListNode* head, int n) {
        int N = listLen(head);
        int k = N - n;

        if (k == 0) return head->next;

        ListNode* temp = head;
        for (int i = 1; i < k; i++) temp = temp->next;

        temp->next = temp->next->next;

        return head;

        // Complexity analysis 
        // Time : O(N + k) 
        // Space : O(1) 
    }

    ListNode* solve2(ListNode* head, int n) {
        ListNode* behind = head;
        ListNode* ahead = head;

        for (int i = 0; i < n; i++) ahead = ahead->next;

        if (ahead == nullptr) return head->next;

        while (ahead->next != nullptr) {
            ahead = ahead->next;
            behind = behind->next;
        }

        behind->next = behind->next->next;

        return head;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }

public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // return solve1(head, n);

        return solve2(head, n);
    }
};

void p2() {
    // Problem 2 : Leetcode 19. Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1 

    ListNode* head = new ListNode(0);
    head->setNext(1)->setNext(2)->setNext(3)->setNext(4)->setNext(5);

    // ListNode* nhead = Problem2().removeNthFromEnd(head, 1);
    // ListNode* nhead = Problem2().removeNthFromEnd(head, 5);
    // ListNode* nhead = Problem2().removeNthFromEnd(head, 3);
    // ListNode* nhead = Problem2().removeNthFromEnd(head, 2);
    ListNode* nhead = Problem2().removeNthFromEnd(head, 4);
    nhead->print();
}

class Problem3 {
public:

    ListNode* keepUniques(ListNode* head) {
        // code here
        if (head == nullptr || head->next == nullptr) return head;

        ListNode* dtemp = head;
        ListNode* temp1 = head->next;

        while (temp1 != nullptr) {
            if (temp1->val != dtemp->val) {
                dtemp->next = temp1;
                dtemp = dtemp->next;
            }
            temp1 = temp1->next;
        }

        dtemp->next = nullptr;

        return head;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }

    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return head;

        ListNode* dummy = new ListNode(-1);
        ListNode* dtemp = dummy;

        ListNode* temp1 = head;
        ListNode* temp2 = head->next;

        while (temp1 != nullptr && temp2 != nullptr) {
            if (temp1->val != temp2->val) {
                dtemp->next = temp1;
                dtemp = dtemp->next;

                temp1 = temp1->next;
                temp2 = temp2->next;
            }
            else {
                while (temp1 != nullptr && temp1->val == temp2->val) {
                    temp1 = temp1->next;
                }
                if (temp1 != nullptr) temp2 = temp1->next;
            }
        }

        dtemp->next = temp1;

        return dummy->next;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }
};

void p3() {
    // Problem 3 : Leetcode 82. Remove Duplicates from Sorted List II - https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1 

    ListNode* head = new ListNode(0);
    // head->setNext(1)->setNext(1)->setNext(1)->setNext(2)->setNext(2);
    head->setNext(0)->setNext(1)->setNext(1)->setNext(2)->setNext(2);

    // ListNode* nhead = Problem3().keepUniques(head);
    ListNode* nhead = Problem3().deleteDuplicates(head);

    nhead->print();
}

class Problem4 {
    int listLen(ListNode* head) {
        int len = 0;
        while (head != nullptr) {
            len++;
            head = head->next;
        }
        return len;
    }

public:
    ListNode* rotateLeft(ListNode* head, int k) {
        int N = listLen(head);
        if (N <= 1) return head;

        k = k % N;

        if (k == 0) return head;

        k = N - k;

        ListNode* thead = nullptr;

        ListNode* ahead = head;
        ListNode* behind = head;

        for (int i = 0; i < k; i++) ahead = ahead->next;

        while (ahead->next != nullptr) {
            ahead = ahead->next;
            behind = behind->next;
        }

        thead = behind->next;

        behind->next = nullptr;
        ahead->next = head;

        return thead;

        // Complexity analysis 
        // Time : O(2N) 
        // Space : O(1) 
    }

    ListNode* rotateRight(ListNode* head, int k) {
        int N = listLen(head);
        if (N <= 1) return head;

        k = k % N;
        if (k == 0) return head;

        ListNode* thead = nullptr;

        ListNode* ahead = head;
        ListNode* behind = head;

        for (int i = 0; i < k; i++) ahead = ahead->next;

        while (ahead->next != nullptr) {
            ahead = ahead->next;
            behind = behind->next;
        }

        thead = behind->next;

        behind->next = nullptr;
        ahead->next = head;

        return thead;

        // Complexity analysis 
        // Time : O(2N) 
        // Space : O(1) 
    }
};

void p4() {
    // Problem 4 : Leetcode 61. Rotate List - https://leetcode.com/problems/rotate-list/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/rotate-a-linked-list/1 

    ListNode* head = new ListNode(0);
    // head->setNext(1)->setNext(2)->setNext(3)->setNext(4);
    head->setNext(1)->setNext(2)->setNext(3)->setNext(4)->setNext(5);

    // ListNode*nhead = Problem4().rotateLeft(head);
    ListNode* nhead = Problem4().rotateRight(head, 7);
    nhead->print();
}


int main() {
    // Day 19 of January 2025 

    p1();

    p2();

    p3();

    p4();


    return 0;
}