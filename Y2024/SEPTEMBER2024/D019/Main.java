
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
        // Day 1 of BST - revisiting

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Leetcode 701. Insert into a Binary Search Tree -
        // https://leetcode.com/problems/insert-into-a-binary-search-tree/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/insert-a-node-in-a-bst/1

        TreeNode root = insertIntoBST(null, 30);
        insertIntoBST(root, 22);
        insertIntoBST(root, 25);
        insertIntoBST(root, 35);

        System.out.println(root.val);
        System.out.println(root.left.val);
        System.out.println(root.right.val);
        System.out.println(root.left.right.val);
    }

    static TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null)
            return new TreeNode(val);

        TreeNode ptr = root;
        while (ptr != null) {
            if (ptr.val < val) {
                if (ptr.right == null) {
                    ptr.right = new TreeNode(val);
                    break;
                } else {
                    ptr = ptr.right;
                }
            } else {
                if (ptr.left == null) {
                    ptr.left = new TreeNode(val);
                    break;
                } else {
                    ptr = ptr.left;
                }
            }
        }

        return root;

        // Complexity analysis
        // Time : O(h), h = hight of tree
        // Space : O(1)
    }

    static void p2() {
        // Problem 2 : Leetcode 450. Delete Node in a BST -
        // https://leetcode.com/problems/delete-node-in-a-bst/description/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/delete-a-node-from-bst/1

        int key = 12;
        TreeNode root = null;
        deleteNode(root, key);

        root = insertIntoBST(root, 30);
        insertIntoBST(root, 22);
        insertIntoBST(root, 35);

        key = 35;
        deleteNode(root, key);
    }

    static TreeNode rightMostNode(TreeNode root) {
        while (root.right != null) {
            root = root.right;
        }

        return root;
    }

    static TreeNode deleteHelper(TreeNode root) {
        if (root.left == null) {
            return root.right;
        } else if (root.right == null) {
            return root.left;
        } else {
            TreeNode right = root.right;
            TreeNode lr = rightMostNode(root.left);
            lr.right = right;
            return root.left;
        }
    }

    static TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) {
            return root;
        }
        if (root.val == key) {
            return deleteHelper(root);
        }

        TreeNode curr = root;
        while (curr != null) {
            if (curr.val > key) {
                if (curr.left != null && curr.left.val == key) {
                    curr.left = deleteHelper(curr.left);
                    break;
                } else {
                    curr = curr.left;
                }
            } else {
                if (curr.right != null && curr.right.val == key) {
                    curr.right = deleteHelper(curr.right);
                    break;
                } else {
                    curr = curr.right;
                }
            }
        }

        return root;
    }
}
