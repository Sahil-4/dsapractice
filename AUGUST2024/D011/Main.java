import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
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
    static void fillIndex(TreeMap<Integer, TreeMap<Integer, PriorityQueue<Integer>>> index, TreeNode node, int x, int y) {
        if (node == null)
            return;

        if (!index.containsKey(y)) {
            index.put(y, new TreeMap<>());
        }

        if (!index.get(y).containsKey(x)) {
            index.get(y).put(x, new PriorityQueue<>());
        }

        index.get(y).get(x).offer(node.val);

        fillIndex(index, node.left, x + 1, y - 1);
        fillIndex(index, node.right, x + 1, y + 1);
    }

    static void fillList(List<List<Integer>> list, TreeMap<Integer, TreeMap<Integer, PriorityQueue<Integer>>> index) {
        for (TreeMap<Integer, PriorityQueue<Integer>> sub : index.values()) {
            list.add(new ArrayList<>());
            for (PriorityQueue<Integer> pq : sub.values()) {
                while (!pq.isEmpty()) {
                    list.get(list.size() - 1).add(pq.poll());
                }
            }
        }
    }

    static List<List<Integer>> verticalTraversal(TreeNode root) {
        List<List<Integer>> list = new ArrayList<>();
        TreeMap<Integer, TreeMap<Integer, PriorityQueue<Integer>>> index = new TreeMap<>();

        fillIndex(index, root, 0, 0);
        fillList(list, index);

        return list;

        // Complexity analysis
        // Time : O(n) + O(log(n)) + O(n), n = number of nodes
        // Space : O(n) + O(n)
    }

    static void p1() {
        // Problem 1 : Leetcode 987. Vertical Order Traversal of a Binary Tree -
        // https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1

        TreeNode root = new TreeNode(0);
        List<List<Integer>> list = verticalTraversal(root);
        for (List<Integer> ls : list) {
            for (int e : ls) {
                System.out.println(e);
            }
        }
    }

    public static void main(String[] args) {
        // Day 12 of Binary Trees

        p1();
    }
}