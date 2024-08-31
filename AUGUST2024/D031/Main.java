
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
        // Day 32 of Binary Trees

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 114. Flatten Binary Tree to Linked List -
        // https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/binary-tree-to-dll/1

        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.left.left.left = new TreeNode(6);

        flatten_Solution1(root);
        // flatten_Solution2(root);
        // flatten_Solution3(root);
        // TreeNode newRoot = bToDLL(root); // DLL

        TreeNode newRoot = root;
        while (newRoot != null) {
            System.out.println(newRoot.val);
            newRoot = newRoot.right;
        }
    }

    static void flatten_Solution1(TreeNode root) {
        TreeNode curr = root;

        while (curr != null) {
            if (curr.left == null) {
                curr = curr.right;
            } else {
                TreeNode rightmost = curr.left;
                while (rightmost.right != null && rightmost.right != curr) {
                    rightmost = rightmost.right;
                }

                if (rightmost.right == null) {
                    rightmost.right = curr.right;
                    curr = curr.left;
                } else {
                    curr = curr.right;
                }
            }
        }

        TreeNode r = root;
        while (r != null) {
            if (r.left != null)
                r.right = r.left;

            r.left = null;
            r = r.right;
        }
    }

    static TreeNode prev = null;

    static void flatten_Solution2(TreeNode root) {
        if (root == null)
            return;

        flatten_Solution2(root.right);
        flatten_Solution2(root.left);

        root.right = prev;
        root.left = null;

        prev = root;
    }

    static void flatten_Solution3(TreeNode root) {
        TreeNode curr = root;

        while (curr != null) {
            if (curr.left != null) {
                TreeNode rightmost = curr.left;
                while (rightmost.right != null) {
                    rightmost = rightmost.right;
                }

                rightmost.right = curr.right;
                curr.right = curr.left;
                curr.left = null;
            }

            curr = curr.right;
        }
    }

    static TreeNode head = null;

    static void solve(TreeNode root) {
        if (root == null)
            return;

        solve(root.right);

        if (head != null) {
            head.left = root;
        }
        root.right = head;
        head = root;

        solve(root.left);
    }

    // Function to convert binary tree to doubly linked list and return it.
    static TreeNode bToDLL(TreeNode root) {
        // Your code here
        if (root == null)
            return null;
        solve(root);
        return head;
    }
}
