
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 3 of BST

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Leetcode 450. Delete Node in a BST -
        // https://leetcode.com/problems/delete-node-in-a-bst/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/delete-a-node-from-bst/1

        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(7);
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);

        preorderPrint(root);
        root = deleteNode(root, 7);
        root = deleteNode(root, 5);
        preorderPrint(root);
    }

    static void preorderPrint(TreeNode root) {
        if (root == null)
            return;

        preorderPrint(root.left);
        System.out.println(root.val);
        preorderPrint(root.right);
    }

    static TreeNode deleteNode(TreeNode root, int key) {
        // if root null
        if (root == null)
            return root;
        // if root have to delete
        if (root.val == key)
            return connect(root);

        // search node to delete
        TreeNode parent = searchParent(root, key);
        if (parent == null)
            return root;

        if (parent.left != null && parent.left.val == key) {
            // delete - parent.left
            // connect sub tree
            // leftSub to right most node of parent.left
            parent.left = connect(parent.left);
        } else {
            // delete - parent.right
            // connect sub tree
            // leftSub to right most node of parent.right
            parent.right = connect(parent.right);
        }

        return root;
    }

    // search parent of the node that has to be deleted
    static TreeNode searchParent(TreeNode root, int key) {
        TreeNode parent = root;
        TreeNode search = root;

        while (search != null && search.val != key) {
            parent = search;
            if (search.val > key) {
                search = search.left;
            } else {
                search = search.right;
            }
        }

        if (search == null)
            return null;
        return parent;
    }

    // connect the left subtree to right of new left sub tree
    static TreeNode connect(TreeNode root) {
        if (root.left == null)
            return root.right;
        if (root.right == null)
            return root.left;

        TreeNode right = root.right;
        TreeNode rightest = root.left;
        while (rightest.right != null) {
            rightest = rightest.right;
        }
        rightest.right = right;

        return root.left;
    }

    static void p2() {
        // Problem 2 : Leetcode 230. Kth Smallest Element in a BST -
        // https://leetcode.com/problems/kth-smallest-element-in-a-bst/
        // Problem 3 : GeeksForGeeks Kth largest element in BST -
        // https://www.geeksforgeeks.org/problems/kth-largest-element-in-bst/1

        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(7);
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);

        ans = -1;
        count = 0;
        int s = kthSmallest(root, 1);
        System.out.println(s);

        ans = -1;
        count = 0;
        int l = kthLargest(root, 1);
        System.out.println(l);
    }

    static int ans = -1;
    static int count = 0;

    static int kthSmallest(TreeNode root, int k) {
        if (root == null)
            return ans;

        kthSmallest(root.left, k);
        if (++count == k)
            ans = root.val;
        kthSmallest(root.right, k);

        return ans;
    }

    static int kthLargest(TreeNode root, int k) {
        if (root == null)
            return ans;

        kthLargest(root.right, k);
        if (++count == k)
            ans = root.val;
        kthLargest(root.left, k);

        return ans;
    }
}