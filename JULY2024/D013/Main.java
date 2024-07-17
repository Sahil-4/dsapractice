import java.util.AbstractMap.SimpleEntry;
import java.util.Map;
import java.util.Stack;

class StockSpanner {
    Stack<Map.Entry<Integer, Integer>> prices = new Stack<>();

    public StockSpanner() {}
    
    public int next(int price) {
        int span = 0;

        while (!prices.isEmpty() && prices.peek().getKey() <= price) {
            span += prices.peek().getValue(); prices.pop();
        }

        if (prices.isEmpty() || prices.peek().getKey() > price) {
            Map.Entry<Integer, Integer> p = new SimpleEntry<>(price, ++span);
            prices.push(p);
        }

        return span;
    }
}

public class Main {
    public static void p1() {
        // Problem 1 : Leetcode 901. Online Stock Span - https://leetcode.com/problems/online-stock-span/ 
        // Geeksforgeeks - https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1 

        int arr[] = { 10, 4, 5, 90, 120, 80 };
        int spans[] = {};
        StockSpanner ss = new StockSpanner();
        for (int i = 0; i < arr.length; i++) spans[i] = ss.next(arr[i]);
        for (int i = 0; i < arr.length; i++) System.out.println(spans[i]);
    }

    public static void main(String args[]) {
        // Day 13 of July 

        p1();
    }
}