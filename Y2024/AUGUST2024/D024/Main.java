import java.util.ArrayList;
import java.util.List;

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
        // Day 25 of Binary trees

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 144. Binary Tree Preorder Traversal -
        // https://leetcode.com/problems/binary-tree-preorder-traversal/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/preorder-traversal/1

        // Create the nodes
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);

        List<Integer> list = preorderTraversal(root);
        for (int e : list) {
            System.out.println(e);
        }
    }

    static List<Integer> preorderTraversal(TreeNode root) {
        // pre order morris traversal -> root left right
        List<Integer> list = new ArrayList<>();

        TreeNode curr = root;

        while (curr != null) {
            if (curr.left == null) {
                list.add(curr.val);
                curr = curr.right;
            } else {
                TreeNode rightmost = curr.left;

                while (rightmost.right != null && rightmost.right != curr) {
                    rightmost = rightmost.right;
                }

                if (rightmost.right == null) {
                    list.add(curr.val);
                    rightmost.right = curr;
                    curr = curr.left;
                } else {
                    rightmost.right = null;
                    curr = curr.right;
                }
            }
        }

        return list;

        // Complexity analysis
        // Time : O(n) + amortised O(n) for setting thread pointer
        // Space : O(1)
    }
}