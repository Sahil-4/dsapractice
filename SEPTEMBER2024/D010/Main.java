
import java.util.PriorityQueue;

class ListNode {
    int val;
    ListNode next;

    ListNode(int val) {
        this.val = val;
    }
}

class MinHeap {
    int[] harr;
    int capacity;
    int heap_size;

    MinHeap(int cap) {
        heap_size = 0;
        capacity = cap;
        harr = new int[cap];
    }

    int parent(int i) {
        return (i - 1) / 2;
    }

    int left(int i) {
        return (2 * i + 1);
    }

    int right(int i) {
        return (2 * i + 2);
    }

    // Function to extract minimum value in heap and then to store
    // next minimum value at first index.
    int extractMin() {
        // Your code here.
        if (heap_size <= 0)
            return -1;

        int answer = harr[0];
        harr[0] = harr[--heap_size];
        MinHeapify(0);

        return answer;
    }

    // Function to insert a value in Heap.
    void insertKey(int k) {
        // Your code here.
        if (heap_size == capacity)
            return;
        decreaseKey(heap_size++, k);
    }

    // Function to delete a key at ith index.
    void deleteKey(int i) {
        // Your code here.
        if (heap_size <= 0 || heap_size <= i)
            return;
        decreaseKey(i, Integer.MIN_VALUE);
        extractMin();
    }

    // Function to change value at ith index and store that value at first index.
    void decreaseKey(int i, int new_val) {
        harr[i] = new_val;
        while (i != 0 && harr[parent(i)] > harr[i]) {
            int temp = harr[i];
            harr[i] = harr[parent(i)];
            harr[parent(i)] = temp;
            i = parent(i);
        }
    }

    /*
     * You may call below MinHeapify function in
     * above codes. Please do not delete this code
     * if you are not writing your own MinHeapify
     */
    void MinHeapify(int i) {
        int l = left(i);
        int r = right(i);
        int smallest = i;
        if (l < heap_size && harr[l] < harr[i])
            smallest = l;
        if (r < heap_size && harr[r] < harr[smallest])
            smallest = r;
        if (smallest != i) {
            int temp = harr[i];
            harr[i] = harr[smallest];
            harr[smallest] = temp;
            MinHeapify(smallest);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 2 of Heaps

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : GeeksForGeeks Binary Heap Operations -
        // https://www.geeksforgeeks.org/problems/operations-on-binary-min-heap/1

        MinHeap mh = new MinHeap(5);
        mh.insertKey(5);
        System.out.println(mh.extractMin());
        mh.insertKey(2);
        mh.insertKey(5);
        mh.insertKey(1);
        System.out.println(mh.extractMin());
        mh.insertKey(7);
        mh.insertKey(8);
        System.out.println(mh.extractMin());
        mh.deleteKey(1);
        mh.deleteKey(2);
        System.out.println(mh.extractMin());
    }

    static void p2() {
        // Problem 2 : Leetcode 23. Merge k Sorted Lists -
        // https://leetcode.com/problems/merge-k-sorted-lists/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/merge-k-sorted-arrays/1

        ListNode l1 = new ListNode(0);
        l1.next = new ListNode(5);
        l1.next.next = new ListNode(7);
        l1.next.next.next = new ListNode(12);

        ListNode l2 = new ListNode(5);
        l2.next = new ListNode(6);
        l2.next.next = new ListNode(8);
        l2.next.next.next = new ListNode(10);

        ListNode lists[] = { l1, l2 };

        ListNode root = mergeKLists(lists);
        printList(root);
    }

    static void printList(ListNode root) {
        while (root != null) {
            System.out.print(root.val + " ");
        }
        System.out.println("");
    }

    static ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0)
            return null;

        PriorityQueue<ListNode> que = new PriorityQueue<>(lists.length, (ListNode n1, ListNode n2) -> n1.val - n2.val);

        ListNode root = new ListNode(-1);
        ListNode temp = root;
        for (ListNode l : lists) {
            if (l != null) {
                que.add(l);
            }
        }

        while (!que.isEmpty()) {
            temp.next = que.poll();
            temp = temp.next;

            if (temp.next != null) {
                que.add(temp.next);
            }
        }

        return root.next;
    }
}
