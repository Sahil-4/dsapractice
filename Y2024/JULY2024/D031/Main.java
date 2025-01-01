import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Main {
    public static List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        if (root == null)
            return list;

        Stack<TreeNode> nodes = new Stack<>();
        nodes.add(root);

        while (!nodes.isEmpty()) {
            TreeNode last = nodes.pop();
            list.add(last.val);
            if (last.right != null) {
                nodes.push(last.right);
            }
            if (last.left != null) {
                nodes.push(last.left);
            }
        }

        return list;

        // Complexity analysis
        // Time : O(n), n = number of nodes
        // Space : O(n), to store answers + O(|d|), d is the depth of tree
    }

    static void p1() {
        // Problem 1 : Leetcode 144. Binary Tree Preorder Traversal -
        // https://leetcode.com/problems/binary-tree-preorder-traversal/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/preorder-traversal/1

        // Create the nodes
        TreeNode root = new TreeNode(1);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(3);
        TreeNode node4 = new TreeNode(4);
        TreeNode node5 = new TreeNode(5);

        // Connect the nodes
        root.left = node2;
        root.right = node3;
        node2.left = node4;
        node2.right = node5;

        // The tree structure is now:
        //*           1
        //*          / \
        //*        2    3
        //*       / \
        //*     4   5
        // => 1 2 4 5 3 
        List<Integer> list = preorderTraversal(root);
        for (int e : list) {
            System.out.println(e);
        }
    }

    public static void main(String[] args) {
        // Day 31 - Day 1 of Trees

        p1();
    }
}