import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.TreeMap;

class TreeNode {
    int data;
    TreeNode left;
    TreeNode right;

    TreeNode(int data) {
        this.data = data;
        left = null;
        right = null;
    }
}

class Pair {
    TreeNode node;
    int xAxis;

    Pair(TreeNode n, int x) {
        node = n;
        xAxis = x;
    }
}

public class Main {
    static void fillmap(Map<Integer, Integer> index, TreeNode root) {
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(root, 0));

        while (!q.isEmpty()) {
            Pair top = q.remove();
            TreeNode n = top.node;

            if (!index.containsKey(top.xAxis)) {
                index.put(top.xAxis, n.data);
            }

            if (n.left != null) {
                q.add(new Pair(n.left, top.xAxis - 1));
            }
            if (n.right != null) {
                q.add(new Pair(n.right, top.xAxis + 1));
            }
        }
    }

    // Function to return a list of nodes visible from the top view
    // from left to right in Binary Tree.
    static ArrayList<Integer> topView(TreeNode root) {
        // add your code
        ArrayList<Integer> list = new ArrayList<>();
        if (root == null)
            return list;

        Map<Integer, Integer> index = new TreeMap<>();

        fillmap(index, root);

        for (Map.Entry<Integer, Integer> entry : index.entrySet()) {
            list.add(entry.getValue());
        }

        return list;
    }

    public static void p1() {
        // Problem 1 : GeeksForGeeks Top View of Binary Tree -
        // https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1

        TreeNode root = new TreeNode(0);
        root.left = new TreeNode(1);
        root.right = new TreeNode(2);
        root.left.left = new TreeNode(3);
        root.left.right = new TreeNode(4);
        root.right.left = new TreeNode(5);
        root.right.right = new TreeNode(6);

        ArrayList<Integer> list = topView(root);
        for (int e : list) {
            System.out.println(e);
        }
    }

    static void rightView(TreeNode root, List<Integer> list, int level) {
        if (root == null)
            return;

        if (list.size() == level) {
            list.add(root.data);
        }

        rightView(root.right, list, level + 1);
        rightView(root.left, list, level + 1);
    }

    static List<Integer> rightSideView(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        rightView(root, list, 0);

        return list;

        // Recursive solution will be good assuming that the tree is not skewed
    }

    static void p2() {
        // Problem 2 : Leetcode 199. Binary Tree Right Side View -
        // https://leetcode.com/problems/binary-tree-right-side-view/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/right-view-of-binary-tree/1

        TreeNode root = new TreeNode(0);
        root.left = new TreeNode(1);
        root.right = new TreeNode(2);
        root.left.left = new TreeNode(3);
        root.left.right = new TreeNode(4);
        root.right.left = new TreeNode(5);
        root.right.right = new TreeNode(6);

        List<Integer> list = rightSideView(root);
        for (int e : list) {
            System.out.println(e);
        }
    }

    public static void main(String[] args) {
        // Day 13 of Binary Trees

        p1();

        p2();
    }
}