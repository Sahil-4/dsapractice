import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class Main {
    static void inorder(List<Integer> list, TreeNode node) {
        // recursion
        if (node == null)
            return;

        inorder(list, node.left);
        list.add(node.val);
        inorder(list, node.right);
    }

    static List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        if (root == null) return list;

        // inorder(list, root);

        Stack<TreeNode> nodes = new Stack<>();
        TreeNode current = root;

        while (current != null || !nodes.isEmpty()) {
            while (current != null) {
                nodes.push(current);
                current = current.left;
            }

            current = nodes.pop();
            list.add(current.val);
            current = current.right;
        }

        return list;

        // Complexity analysis
        // Time : O(n), n = number of nodes
        // Space : O(n), to store answers, + O(h) stack space for recursion
    }

    static void p1() {
        // Problem 1 : Leetcode 94. Binary Tree Inorder Traversal -
        // https://leetcode.com/problems/binary-tree-inorder-traversal/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/inorder-traversal/1

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
        // * 1
        // * / \
        // * 2 3
        // * / \
        // * 4 5
        // => 4 2 5 1 3

        List<Integer> list = inorderTraversal(root);
        for (int e : list) {
            System.out.println(e);
        }
    }

    public static void main(String[] args) {
        // Day 1 of August - Day 2 of Trees

        p1();
    }
}