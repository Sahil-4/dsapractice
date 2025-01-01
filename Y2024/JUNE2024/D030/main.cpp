#include <iostream>
#include <vector>

using namespace std;

class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

Node* copyRandomList(Node* head) {
    Node *temp = head;

    // making copy nodes 
    while (temp != NULL) {
        Node *n = new Node(temp->val);
        n->next = temp->next;
        temp->next = n;

        temp = temp->next->next;
    }

    // updating random pointers 
    temp = head;
    while (temp != NULL) {
        if (temp->random == NULL) {
            temp->next->random = temp->random;
        } else {
            temp->next->random = temp->random->next;
        }

        temp = temp->next->next;
    }

    // splitting both lists 
    temp = head;
    Node *l2 = NULL;
    Node *l2_ptr = NULL;
    while (temp != NULL) {
        if (l2 == NULL) {
            l2 = temp->next;
            l2_ptr = l2;
        } else {
            l2_ptr->next = temp->next;
            l2_ptr = l2_ptr->next;
        }

        temp->next = temp->next->next;
        temp = temp->next;
    }

    return l2;
}

void p1() {
    // Problem 1 : Leetcode 138. Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1 

    Node *head = new Node(1);
    Node *n2 = new Node(6);
    Node *n3 = new Node(9);
    Node *n4 = new Node(4);
    head->next = n2; n2->next = n3; n3->next = n4; n4->next = NULL;
    head->random = n4; n2->random = NULL; n3->random = head; n4->random = n3;

    Node *copyList = copyRandomList(head);
}

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

int getListLength(ListNode *head) {
    int len = 0;

    while (head != NULL) {
        head = head->next;
        len++;
    }

    return len;
}

vector<ListNode*> splitListToParts(ListNode* head, int k) {
    vector<ListNode*> out(k, NULL);
    int index = 0;

    int list_len = getListLength(head);

    int sub_list_len = list_len / k;
    int first_nk = list_len % k;

    ListNode *start = head;
    int nodes_count = 1;
    while (head != NULL) {
        ListNode *nnext = head->next;

        if ((index < first_nk && nodes_count == sub_list_len + 1) || (index >= first_nk && nodes_count == sub_list_len)) {
            head->next = NULL;
            out[index] = start;

            index++;
            start = nnext;
            nodes_count = 0;
        }

        head = nnext;
        nodes_count++;
    }

    return out;
}

void p2() {
    // Problem 2 : Leetcode 725. Split Linked List in Parts - https://leetcode.com/problems/split-linked-list-in-parts/ 

    ListNode *head = new ListNode(1);
    ListNode *n2 = new ListNode(6);
    ListNode *n3 = new ListNode(9);
    ListNode *n4 = new ListNode(4);
    ListNode *n5 = new ListNode(5);
    head->next = n2; n2->next = n3; n3->next = n4; n4->next = n5; n5->next = NULL;

    vector<ListNode*> splits = splitListToParts(head, 3);
    for (int i = 0; i < splits.size(); i++) {
        ListNode *temp_head = splits[i];
        while (temp_head != NULL) {
            cout << temp_head->val << " ";
        } cout << endl;
    }
}


int main() {
    // Day 30 

    p1();

    p2();


    return 0;
}