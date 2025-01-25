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

class Problem1 {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> out;

        if (root == nullptr) return out;

        // level order traversal 

        deque<TreeNode*> nodesDeque;
        nodesDeque.push_back(root);

        while (!nodesDeque.empty()) {
            int N = nodesDeque.size();

            TreeNode* curr = nodesDeque.front();
            out.push_back(curr->val);

            for (int i = 0; i < N; i++) {
                curr = nodesDeque.front(); nodesDeque.pop_front();
                if (curr->right != nullptr) nodesDeque.push_back(curr->right);
                if (curr->left != nullptr) nodesDeque.push_back(curr->left);
            }
        }

        return out;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(W) 
    }
};

void p1() {
    // Problem 1 : Leetcode 199. Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/right-view-of-binary-tree/1 

    TreeNode* root = TreeNode::construct({ 1,3,-1,4,-1,5,-1,6,7,8,-1 }, -1);
    vector<int> out = Problem1().rightSideView(root);
    for (int e : out) cout << e << " ";
    cout << endl;
}

class Problem2 {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> out;

        if (root == nullptr) return out;

        // level order traversal 

        deque<TreeNode*> nodesDeque;
        nodesDeque.push_back(root);

        while (!nodesDeque.empty()) {
            int N = nodesDeque.size();
            double sum = 0;

            for (int i = 0; i < N; i++) {
                TreeNode* curr = nodesDeque.front(); nodesDeque.pop_front();
                sum += curr->val;
                if (curr->right != nullptr) nodesDeque.push_back(curr->right);
                if (curr->left != nullptr) nodesDeque.push_back(curr->left);
            }

            double avg = sum / N;
            out.push_back(avg);
        }

        return out;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(W) 
    }
};

void p2() {
    // Problem 2 : Leetcode 637. Average of Levels in Binary Tree - https://leetcode.com/problems/average-of-levels-in-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/level-of-a-node-in-binary-tree/1 

    TreeNode* root = TreeNode::construct({ 1,3,-1,4,-1,5,-1,6,7,8,-1 }, -1);
    vector<double> out = Problem2().averageOfLevels(root);
    for (int e : out) cout << e << " ";
    cout << endl;
}

class Problem3 {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> out;

        if (root == nullptr) return out;

        deque<TreeNode*> nodesDeque;
        nodesDeque.push_back(root);

        while (!nodesDeque.empty()) {
            int N = nodesDeque.size();
            vector<int> v;

            for (int i = 0; i < N; i++) {
                TreeNode* curr = nodesDeque.front(); nodesDeque.pop_front();
                v.push_back(curr->val);
                if (curr->left != nullptr) nodesDeque.push_back(curr->left);
                if (curr->right != nullptr) nodesDeque.push_back(curr->right);
            }
            out.push_back(v);
        }

        return out;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(W) 
    }
};

void p3() {
    // Problem 3 : Leetcode 102. Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/level-order-traversal/1 

    TreeNode* root = TreeNode::construct({ 1,3,-1,4,-1,5,-1,6,7,8,-1 }, -1);
    vector<vector<int>> out = Problem3().levelOrder(root);
    for (vector<int> v: out) {
        for (int e: v) cout << e << " ";
        cout << endl;
    }
}

class Problem4 {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> out;

        if (root == nullptr) return out;

        deque<TreeNode*> nodesDeque;
        nodesDeque.push_back(root);

        int level = 0;

        while (!nodesDeque.empty()) {
            int N = nodesDeque.size();
            vector<int> v;

            for (int i = 0; i < N; i++) {
                TreeNode* curr = nodesDeque.front(); nodesDeque.pop_front();
                v.push_back(curr->val);
                if (curr->left != nullptr) nodesDeque.push_back(curr->left);
                if (curr->right != nullptr) nodesDeque.push_back(curr->right);
            }

            if (level++&1) reverse(v.begin(), v.end());
            out.push_back(v);
        }

        return out;

        // Complexity analysis 
        // Time : O(N) + O(W) 
        // Space : O(W) 
    }
};

void p4() {
    // Problem 4 : Leetcode 103. Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/?envType=study-plan-v2&envId=top-interview-150
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/zigzag-tree-traversal/1 

    TreeNode* root = TreeNode::construct({ 1,3,-1,4,-1,5,-1,6,7,8,-1 }, -1);
    vector<vector<int>> out = Problem4().zigzagLevelOrder(root);
    for (vector<int> v: out) {
        for (int e: v) cout << e << " ";
        cout << endl;
    }
}


int main() {
    // Day 25 of January 2025 

    p1();

    p2();

    p3();

    p4();


    return 0;
}