#include <bits/stdc++.h>

using namespace std;

class TreeNode {
public:
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}

    static void print(TreeNode* node) {
        // pre order traversal 
        if (node == nullptr) return;

        cout << node->val << " ";

        print(node->left);
        print(node->right);
    }

    static TreeNode* construct(vector<int> v, int MARK) {
        if (v.size() == 0 || v[0] == MARK) return nullptr;

        TreeNode* root = new TreeNode(v[0]);

        deque<TreeNode*> dq;
        dq.push_back(root);

        for (int i = 1; i < v.size();) {
            TreeNode* r = dq.front(); dq.pop_front();
            if (v[i] != MARK) {
                r->left = new TreeNode(v[i]);
                dq.push_back(r->left);
            }
            i++;
            if (v[i] != MARK) {
                r->right = new TreeNode(v[i]);
                dq.push_back(r->right);
            }
            i++;
        }

        return root;
    }
};

class BSTIterator {
    stack<TreeNode*> stk;

    void pushLefts(TreeNode* node) {
        while (node != nullptr) {
            stk.push(node);
            node = node->left;
        }
    }

public:
    BSTIterator(TreeNode* root) {
        pushLefts(root);
    }

    int next() {
        TreeNode* cn = stk.top(); stk.pop();
        pushLefts(cn->right);
        return cn->val;
    }

    bool hasNext() {
        return !stk.empty();
    }

    // Complexity analysis 
    // Time : O(1) average 
    // space : O(H) 
};

void p1() {
    // Problem 1 : Leetcode 173. Binary Search Tree Iterator - https://leetcode.com/problems/binary-search-tree-iterator/description/?envType=study-plan-v2&envId=top-interview-150 

    TreeNode* root = TreeNode::construct({ 7, 3, 15, -1, -1, 9, 20 }, -1);
    TreeNode::print(root); cout << endl;

    BSTIterator bsti = BSTIterator(root);
    while (bsti.hasNext()) {
        cout << bsti.next() << " ";
    } cout << endl;
}

class Problem2 {
    int countNodes1(TreeNode* root) {
        if (root == nullptr) return 0;

        int l = countNodes1(root->left);
        int r = countNodes1(root->right);

        return 1 + l + r;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(H) 
    }

    int lHeight(TreeNode* node) {
        int h = 0;
        while (node != nullptr) {
            node = node->left; h++;
        }
        return h;
    }

    int rHeight(TreeNode* node) {
        int h = 0;
        while (node != nullptr) {
            node = node->right; h++;
        }
        return h;
    }

    int countNodes2(TreeNode* root) {
        if (root == nullptr) return 0;

        int lh = lHeight(root);
        int rh = rHeight(root);
        if (lh == rh) return pow(2, lh) - 1;

        lh = countNodes2(root->left);
        rh = countNodes2(root->right);
        return 1 + lh + rh;

        // Complexity analysis 
        // Time : O(<N) or O(H^2) or O(Log(N)^2) 
        // Space : O(H) 
    }

public:
    int countNodes(TreeNode* root) {
        // return countNodes1(root);

        return countNodes2(root);
    }
};

void p2() {
    // Problem 2 : Leetcode 222. Count Complete Tree Nodes - https://leetcode.com/problems/count-complete-tree-nodes/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/count-number-of-nodes-in-a-binary-tree/0 

    TreeNode* root = TreeNode::construct({ 0,1,2,3,4,5,6,7,8,9 }, -1);
    TreeNode::print(root); cout << endl;
    cout << Problem2().countNodes(root);
}

class Problem3 {
    bool buildPath(TreeNode* root, TreeNode* x, stack<TreeNode*>& xpath) {
        if (root == nullptr) return false;

        if (root->val == x->val) {
            xpath.push(root);
            return true;
        }

        bool lcheck = buildPath(root->left, x, xpath);
        bool rcheck = buildPath(root->right, x, xpath);

        if (lcheck || rcheck) {
            xpath.push(root);
            return true;
        }

        return false;
    }

public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // trace path of p and q 
        stack<TreeNode*> ppath, qpath;
        bool pcheck = buildPath(root, p, ppath);
        bool qcheck = buildPath(root, q, qpath);

        // case : if not sure p, q exist in root 
        // if (!pcheck || !qcheck) return nullptr;

        // now we will keep checking the same nodes 
        // last same node will be lca that we will return 

        TreeNode* lca = root;
        while (!ppath.empty() && !qpath.empty()) {
            if (ppath.top()->val != qpath.top()->val) break;
            lca = ppath.top();
            ppath.pop(); qpath.pop();
        }

        return lca;

        // Complexity analysis 
        // Time : O(2H) + O(H) 
        // Space : O(2H) + O(H) 
    }
};

void p3() {
    // Problem 3 : Leetcode 236. Lowest Common Ancestor of a Binary Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/1 

    TreeNode* root = TreeNode::construct({ 0,1,2,3,4,5,6,7,8,9 }, -1);
    TreeNode::print(root); cout << endl;

    TreeNode* lca = Problem3().lowestCommonAncestor(root, root->left->left, root->left->right);
    cout << lca->val << endl;
}


int main() {
    // Day 24 of January 2025 

    p1();

    p2();

    p3();


    return 0;
}