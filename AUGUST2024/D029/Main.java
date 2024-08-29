import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
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
        // Day 30 of Binary Trees

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 987. Vertical Order Traversal of a Binary Tree -
        // https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1

        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.left.left.left = new TreeNode(6);

        List<List<Integer>> list = verticalTraversal(root);
        for (List<Integer> l : list) {
            for (int e : l) {
                System.out.println(e);
            }
        }
    }

    static void fillTable(TreeNode root, Map<Integer, Map<Integer, List<Integer>>> table, int x, int y) {
        if (root == null)
            return;

        if (!table.containsKey(x)) {
            table.put(x, new TreeMap<>());
        }

        if (!table.get(x).containsKey(y)) {
            table.get(x).put(y, new ArrayList<>());
        }

        table.get(x).get(y).add(root.val);

        fillTable(root.left, table, x - 1, y + 1);
        fillTable(root.right, table, x + 1, y + 1);
    }

    static void fillList(List<List<Integer>> list, Map<Integer, Map<Integer, List<Integer>>> table) {
        for (Map<Integer, List<Integer>> index : table.values()) {
            list.add(new ArrayList<>());

            for (List<Integer> ls : index.values()) {
                Collections.sort(ls);
                list.get(list.size() - 1).addAll(ls);
            }
        }
    }

    static List<List<Integer>> verticalTraversal(TreeNode root) {
        List<List<Integer>> list = new ArrayList<>();
        Map<Integer, Map<Integer, List<Integer>>> table = new TreeMap<>();

        fillTable(root, table, 0, 0);
        fillList(list, table);

        return list;
    }
}
