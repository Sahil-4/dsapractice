import java.util.HashMap;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class Main {
    static TreeNode buildTree(int[] inorder, int iStart, int iEnd, int[] postorder, int pStart, int pEnd,
            HashMap<Integer, Integer> map) {
        if (iStart > iEnd || pStart > pEnd)
            return null;

        TreeNode root = new TreeNode(postorder[pEnd]);

        int eIdx = map.get(postorder[pEnd]);
        int lefts = eIdx - iStart;

        root.left = buildTree(inorder, iStart, eIdx - 1, postorder, pStart, pStart + lefts - 1, map);
        root.right = buildTree(inorder, eIdx + 1, iEnd, postorder, pStart + lefts, pEnd - 1, map);

        return root;
    }

    static TreeNode buildTree(int[] inorder, int[] postorder) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            map.put(inorder[i], i);
        }

        return buildTree(inorder, 0, inorder.length - 1, postorder, 0, postorder.length - 1, map);
    }

    static void p1() {
        // Problem 1 : Leetcode 106. Construct Binary Tree from Inorder and Postorder Traversal -
        // https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/tree-from-postorder-and-inorder/1

        int inorder[] = { 7, 4, 2, 1, 5, 3, 8, 6 };
        int postorder[] = { 7, 4, 2, 5, 8, 6, 3, 1 };
        TreeNode root = buildTree(inorder, postorder);
    }

    public static void main(String[] args) {
        // Day 22 of Binary Trees

        p1();
    }
}
