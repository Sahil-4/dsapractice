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
    static TreeNode buildTree(int preorder[], int pStart, int pEnd, int inorder[], int iStart, int iEnd,
            HashMap<Integer, Integer> map) {
        // base condition
        if (pStart > pEnd || iStart > iEnd)
            return null;

        // create root
        TreeNode root = new TreeNode(preorder[pStart]);

        // find mid index to divide lists into left and right list
        int rootIndex = map.get(preorder[pStart]);
        int leftN = rootIndex - iStart;

        // build left and right sub tree
        root.left = buildTree(preorder, pStart + 1, pStart + leftN, inorder, iStart, rootIndex - 1, map);
        root.right = buildTree(preorder, pStart + leftN + 1, pEnd, inorder, rootIndex + 1, iEnd, map);

        // return root after getting left and right nodes
        return root;
    }

    static TreeNode buildTree(int[] preorder, int[] inorder) {
        // code goes here
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            map.put(inorder[i], i);
        }

        return buildTree(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1, map);
    }

    static void p1() {
        // Problem 1 : Leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal -
        // https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/construct-tree-1/1

        int preorder[] = { 3, 9, 20, 15, 7 };
        int inorder[] = { 9, 3, 15, 20, 7 };
        TreeNode root = buildTree(preorder, inorder);
    }

    public static void main(String[] args) {
        // Day 21 of Binary Trees

        p1();
    }
}