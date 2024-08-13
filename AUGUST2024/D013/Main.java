import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.TreeMap;

class Pair {
    TreeNode node;
    int axis;

    Pair(TreeNode n, int x) {
        node = n;
        axis = x;
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class Main {
    static boolean areSymmetric(TreeNode r1, TreeNode r2) {
        if (r1 == null && r2 == null)
            return true;

        if (r1 == null || r2 == null)
            return false;

        if (r1.val != r2.val)
            return false;

        boolean b1 = areSymmetric(r2.left, r1.right);
        if (!b1)
            return false;

        boolean b2 = areSymmetric(r2.right, r1.left);

        return b2;
    }

    // return true/false denoting whether the tree is Symmetric or not
    static boolean isSymmetric(TreeNode root) {
        // add your code here;
        if (root == null)
            return true;
        return areSymmetric(root.left, root.right);
    }

    static void p1() {
        // Problem 1 : Leetcode 101. Symmetric Tree -
        // https://leetcode.com/problems/symmetric-tree/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/symmetric-tree/1

        TreeNode root = new TreeNode(0);
        root.left = new TreeNode(1);
        root.left.left = new TreeNode(2);
        root.left.right = new TreeNode(3);
        root.right = new TreeNode(1);
        root.right.right = new TreeNode(2);
        root.right.left = new TreeNode(3);

        boolean check = isSymmetric(root);
        System.out.println(check);
    }

    static void fillmap(TreeMap<Integer, Integer> index, TreeNode root) {
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(root, 0));

        while (!q.isEmpty()) {
            Pair top = q.remove();
            TreeNode n = top.node;
            index.put(top.axis, n.val);

            if (n.left != null) {
                q.add(new Pair(n.left, top.axis - 1));
            }

            if (n.right != null) {
                q.add(new Pair(n.right, top.axis + 1));
            }
        }
    }

    // Function to return a list containing the bottom view of the given tree.
    static ArrayList<Integer> bottomView(TreeNode root) {
        // Code here
        ArrayList<Integer> list = new ArrayList<>();
        if (root == null)
            return list;

        TreeMap<Integer, Integer> index = new TreeMap<>();

        fillmap(index, root);

        for (Map.Entry<Integer, Integer> entry : index.entrySet()) {
            list.add(entry.getValue());
        }

        return list;
    }

    static void p2() {
        // Problem 2 : GeeksForGeeks Bottom View of Binary Tree -
        // https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

        TreeNode root = new TreeNode(0);
        root.left = new TreeNode(1);
        root.left.left = new TreeNode(2);
        root.left.right = new TreeNode(3);
        root.right = new TreeNode(4);
        root.right.right = new TreeNode(5);
        root.right.left = new TreeNode(6);

        ArrayList<Integer> list = bottomView(root);
        for (int e : list) {
            System.out.println(e);
        }
    }

    public static void main(String[] args) {
        // Day 14 of Binary Trees

        p1();

        p2();
    }
}