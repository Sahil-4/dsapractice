import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class Main {
    static List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> list = new ArrayList<>();
        if (root == null)
            return list;

        boolean flag = false;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            List<Integer> subList = new ArrayList<>();
            int level = queue.size();

            for (int i = 0; i < level; i++) {
                TreeNode curr = queue.remove();
                subList.add(curr.val);

                if (curr.left != null)
                    queue.add(curr.left);
                if (curr.right != null)
                    queue.add(curr.right);
            }

            if (flag)
                Collections.reverse(subList);
            flag = !flag;
            list.add(subList);
        }

        return list;
    }

    static void p1() {
        // Problem 1 : Leetcode 103. Binary Tree Zigzag Level Order Traversal -
        // https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/zigzag-tree-traversal/1

        // Tree
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right = new TreeNode(3);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);

        List<List<Integer>> list = zigzagLevelOrder(root);
        for (List<Integer> sub : list) {
            for (int e : sub) {
                System.out.print(e);
            }
            System.out.println("");
        }
    }

    static void mostLefts(ArrayList<Integer> list, TreeNode node) {
        if (node == null)
            return;
        if (node.left == null && node.right == null)
            return;

        list.add(node.val);

        if (node.left != null) {
            mostLefts(list, node.left);
        } else {
            mostLefts(list, node.right);
        }
    }

    static void leafs(ArrayList<Integer> list, TreeNode node) {
        if (node == null)
            return;
        if (node.left == null && node.right == null) {
            list.add(node.val);
            return;
        }

        leafs(list, node.left);
        leafs(list, node.right);
    }

    static void mostRights(ArrayList<Integer> list, TreeNode node) {
        if (node == null)
            return;
        if (node.left == null && node.right == null)
            return;

        if (node.right != null) {
            mostRights(list, node.right);
        } else {
            mostRights(list, node.left);
        }

        list.add(node.val);
    }

    static ArrayList<Integer> boundary(TreeNode node) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(node.val);

        if (node.left == null && node.right == null)
            return list;

        mostLefts(list, node.left);
        leafs(list, node);
        mostRights(list, node.right);

        return list;
    }

    static void p2() {
        // Problem 2 : GeeksForGeeks Tree Boundary Traversal -
        // https://www.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1

        // Tree
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right = new TreeNode(3);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);

        ArrayList<Integer> list = boundary(root);
        for (int e : list) {
            System.out.println(e);
        }
    }

    public static void main(String[] args) {
        // Day 11 of Trees

        p1();

        p2();
    }
}