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
        // Day 28 of Binary Trees

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 199. Binary Tree Right Side View -
        // https://leetcode.com/problems/binary-tree-right-side-view/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/right-view-of-binary-tree/1

        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.left.left.left = new TreeNode(6);

        List<Integer> list = rightSideView(root);
        for (int e : list) {
            System.out.println(e);
        }
    }

    static void rightView(TreeNode root, List<Integer> list, int level) {
        if (root == null)
            return;

        if (list.size() == level)
            list.add(root.val);

        rightView(root.right, list, level + 1);
        rightView(root.left, list, level + 1);
    }

    static List<Integer> rightSideView(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        rightView(root, list, 0);
        return list;
    }
}
