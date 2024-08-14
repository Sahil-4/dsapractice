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
    static void pathToLeaf(List<String> list, String path, TreeNode root) {
        if (root.left == null && root.right == null) {
            list.add(path);
            return;
        }

        if (root.left != null) {
            pathToLeaf(list, path + "->" + String.valueOf(root.left.val), root.left);
        }
        if (root.right != null) {
            pathToLeaf(list, path + "->" + String.valueOf(root.right.val), root.right);
        }
    }

    static List<String> binaryTreePaths(TreeNode root) {
        List<String> list = new ArrayList<>();

        if (root == null)
            return list;

        pathToLeaf(list, String.valueOf(root.val), root);

        return list;
    }

    static void pathToLeaf(ArrayList<ArrayList<Integer>> list, ArrayList<Integer> path, TreeNode root) {
        if (root.left == null && root.right == null) {
            list.add(new ArrayList<>(path));
            return;
        }

        if (root.left != null) {
            path.add(root.left.val);
            pathToLeaf(list, path, root.left);
            path.remove(path.size() - 1);
        }

        if (root.right != null) {
            path.add(root.right.val);
            pathToLeaf(list, path, root.right);
            path.remove(path.size() - 1);
        }
    }

    static ArrayList<ArrayList<Integer>> Paths(TreeNode root) {
        // code here
        ArrayList<ArrayList<Integer>> list = new ArrayList<>();
        ArrayList<Integer> path = new ArrayList<>();

        if (root == null)
            return list;

        path.add(root.val);

        pathToLeaf(list, path, root);

        return list;
    }

    static void p1() {
        // Problem 1 : Leetcode 257. Binary Tree Paths -
        // https://leetcode.com/problems/binary-tree-paths/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1

        TreeNode root = new TreeNode(0);
        root.left = new TreeNode(1);
        root.left.left = new TreeNode(2);
        root.left.right = new TreeNode(3);
        root.right = new TreeNode(1);
        root.right.right = new TreeNode(2);
        root.right.left = new TreeNode(3);

        List<String> list = binaryTreePaths(root);
        for (String path : list) {
            System.out.println(path);
        }

        ArrayList<ArrayList<Integer>> list2 = Paths(root);
        for (ArrayList<Integer> path : list2) {
            for (int e : path) {
                System.out.print(e);
            }
            System.out.println("");
        }
    }

    public static void main(String[] args) {
        // Day 15 of Binary Trees

        p1();
    }
}
