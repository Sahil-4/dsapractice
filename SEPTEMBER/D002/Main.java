
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
        // Day 2 of BST

        p1();

        p3();
    }

    static void p1() {
        // Problem 1 : GeeksForGeeks Ceil in BST -
        // https://www.geeksforgeeks.org/problems/implementing-ceil-in-bst/1
        // Problem 2 : GeeksForGeeks Floor in BST -
        // https://www.geeksforgeeks.org/problems/floor-in-bst/1

        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(7);
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);

        int c = findCeil(root, 5);
        int f = floor(root, 5);
        System.out.println(c);
        System.out.println(f);
    }

    // Function to return the ceil of given number in BST.
    static int findCeil(TreeNode root, int key) {
        // Code here
        int ceil = -1;
        TreeNode curr = root;

        while (curr != null) {
            if (curr.val == key)
                return key;
            else if (curr.val < key)
                curr = curr.right;
            else {
                ceil = curr.val;
                curr = curr.left;
            }
        }

        return ceil;
    }

    static int floor(TreeNode root, int key) {
        // Code here
        int ceil = -1;
        TreeNode curr = root;

        while (curr != null) {
            if (curr.val == key)
                return key;
            else if (curr.val > key)
                curr = curr.left;
            else {
                ceil = curr.val;
                curr = curr.right;
            }
        }

        return ceil;
    }

    static void p3() {
        // Problem 3 : Leetcode 701. Insert into a Binary Search Tree -
        // https://leetcode.com/problems/insert-into-a-binary-search-tree/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/insert-a-node-in-a-bst/1

        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(7);
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);

        insertIntoBST(root, 1);
        insertIntoBST_Solution2(root, 18);
    }

    static TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null)
            return new TreeNode(val);

        if (root.val > val) {
            root.left = insertIntoBST(root.left, val);
        } else {
            root.right = insertIntoBST(root.right, val);
        }

        return root;

        // Complexity Analysis
        // Time : O(h)
        // Space : O(1) + O(n) for stack space
    }

    static TreeNode insertIntoBST_Solution2(TreeNode root, int val) {
        if (root == null)
            return new TreeNode(val);

        TreeNode curr = root;
        while (true) {
            if (curr.val > val) {
                if (curr.left == null) {
                    curr.left = new TreeNode(val);
                    break;
                } else {
                    curr = curr.left;
                }
            } else {
                if (curr.right == null) {
                    curr.right = new TreeNode(val);
                    break;
                } else {
                    curr = curr.right;
                }
            }
        }

        return root;

        // Complexity Analysis
        // Time : O(h)
        // Space : O(1)
    }
}
