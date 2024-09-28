import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;

class Pair {
    String word;
    int sequenceLength;

    Pair(String w, int l) {
        this.word = w;
        this.sequenceLength = l;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 28 of September

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 127. Word Ladder -
        // https://leetcode.com/problems/word-ladder/description/
        // GeeksForGeeks - 
        // https://www.geeksforgeeks.org/problems/word-ladder/1

        String beginWord = "";
        String endWord = "";
        List<String> wordList = new ArrayList<>();

        int len = ladderLength(beginWord, endWord, wordList);
        System.out.println(len);
    }

    static int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> dict = new HashSet<>();
        dict.addAll(wordList);
        dict.remove(beginWord);

        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(beginWord, 1));

        while (!q.isEmpty()) {
            Pair top = q.remove();

            String word = top.word;
            int sequenceLength = top.sequenceLength;

            if (word.equals(endWord)) {
                return sequenceLength;
            }

            for (int i = 0; i < word.length(); i++) {
                for (char ch = 'a'; ch <= 'z'; ch++) {
                    char[] charr = word.toCharArray();
                    charr[i] = ch;

                    String nword = new String(charr);

                    if (dict.contains(nword)) {
                        dict.remove(nword);
                        q.add(new Pair(nword, sequenceLength + 1));
                    }
                }
            }
        }

        return 0;

        // Complexity analysis
        // Time : O(wordList.length) + O(wordList.length * wordLen)
        // Space : O(wordList.length) + O(wordList.length)
    }
}
