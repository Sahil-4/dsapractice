import java.util.Map;
import java.util.TreeMap;

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
        // Day 31 of Binary Trees

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal -
        // https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/construct-tree-1/1

        int preorder[] = { 9, 12, 18, 15, 7 };
        int inorder[] = { 12, 9, 15, 18, 7 };
        TreeNode root = buildTree(preorder, inorder);
    }

    static TreeNode buildTree(int[] preorder, int preStart, int preEnd, int[] inorder, int inStart, int inEnd,
            Map<Integer, Integer> inmap) {
        if (preStart > preEnd || inStart > inEnd)
            return null;

        TreeNode root = new TreeNode(preorder[preStart]);

        int n = inmap.get(preorder[preStart]) - inStart;

        root.left = buildTree(preorder, preStart + 1, preStart + n, inorder, inStart, inStart + n, inmap);
        root.right = buildTree(preorder, preStart + n + 1, preEnd, inorder, inStart + n + 1, inEnd, inmap);

        return root;
    }

    static TreeNode buildTree(int[] preorder, int[] inorder) {
        // pre - root | left | right
        // in - left | root | right
        Map<Integer, Integer> inmap = new TreeMap<>();
        for (int i = 0; i < inorder.length; i++) {
            inmap.put(inorder[i], i);
        }

        return buildTree(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1, inmap);
    }
}