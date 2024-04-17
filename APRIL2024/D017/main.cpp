#include <iostream>

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

    Node(int _val, Node *_nextl, Node *_random) {
        val = _val;
        next = _nextl;
        random = _random;
    }
};

Node* copyRandomList(Node* head) {
    Node *newHead = new Node(-1);

    Node* temp = head;
    while (temp != NULL) {
        Node *n = new Node(temp->val);
        n->next = temp->next;
        temp->next = n;
        temp = temp->next->next;
    }

    temp = head;
    while (temp != NULL) {
        if (temp->next != NULL && temp->random != NULL) temp->next->random = temp->random->next;
        temp = temp->next->next;
    }

    Node *temp2 = newHead;
    temp = head;
    while (temp != NULL) {
        temp2->next = temp->next;
        temp->next = temp->next->next;
        temp2 = temp2->next;
        temp = temp->next;
    }

    return newHead->next;
}

void p1() {
    // Problem 1 : L 138. Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/ 

    Node *n4 = new Node(1, NULL, NULL);
    Node *n3 = new Node(10, n4, NULL);
    Node *n2 = new Node(11, n3, NULL);
    Node *n1 = new Node(13, n2, NULL);
    Node *head = new Node(7, n1, NULL);
    head->random = NULL, n1->random = head, n2->random = n4, n3->random = n2, n4->random = head;

    Node *copy = copyRandomList(head);
    Node *temp = head;
    Node *temp2 = copy;
    while (temp != NULL) {
        cout << "temp val " << temp->val << " ";
        cout << "copy val " << copy->val << " ";
        cout << "temp next addr " << temp->next << " ";
        cout << "copy next addr " << copy->next << " ";
        cout << "temp random  addr " << temp->random << " ";
        cout << "copy random  addr " << copy->random << " ";

        temp = temp->next;
        copy = copy->next;
    }
}


int main() {
    // Day 17 
    
    p1();


    return 0;
}