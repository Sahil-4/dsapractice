import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

class Word {
    String word;
    ArrayList<String> path;

    Word(String w, ArrayList<String> prevPath) {
        this.word = w;
        this.path = new ArrayList(prevPath);
        path.add(w);
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 29 of September

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 126. Word Ladder II -
        // https://leetcode.com/problems/word-ladder-ii/description/
        // GeeksForGeeks - 
        // https://www.geeksforgeeks.org/problems/word-ladder-ii/1

        String beginWord = "hit";
        String endWord = "cog";
        String[] wordList = { "hot", "dot", "dog", "lot", "log", "cog" };

        ArrayList<ArrayList<String>> paths = findSequences(beginWord, endWord, wordList);
        List<List<String>> ladders = findLadders(beginWord, endWord, Arrays.asList(wordList));
        for (ArrayList<String> path : paths) {
            System.out.println(path.toString());
        }
        for (List<String> path : ladders) {
            System.out.println(path.toString());
        }
    }

    static ArrayList<ArrayList<String>> findSequences(String beginWord, String endWord, String[] wordList) {
        // Code here
        ArrayList<ArrayList<String>> output = new ArrayList<>();

        Set<String> dict = new HashSet<>();
        dict.addAll(Arrays.asList(wordList));

        Queue<Word> q = new LinkedList<>();
        q.add(new Word(beginWord, new ArrayList<>()));

        int level = 0;
        ArrayList<String> used = new ArrayList<>();
        used.add(beginWord);

        while (!q.isEmpty()) {
            // last Word
            Word top = q.remove();
            String word = top.word;
            ArrayList<String> path = top.path;

            // erasing words in dict used on prev level
            if (level < path.size()) {
                level++;
                for (String s : used) {
                    dict.remove(s);
                }
            }

            // if we have got the end word
            if (word.equals(endWord)) {
                if (output.isEmpty() || output.get(0).size() == path.size()) {
                    output.add(path);
                }
            }

            // create next word
            for (int i = 0; i < word.length(); i++) {
                for (char ch = 'a'; ch <= 'z'; ch++) {
                    char[] charr = word.toCharArray();
                    charr[i] = ch;
                    String nword = new String(charr);

                    if (dict.contains(nword)) {
                        used.add(nword);
                        q.add(new Word(nword, path));
                    }
                }
            }
        }

        return output;

        // Complexity analysis
        // Time : O(n * n), depends upon input
        // Space : O(n) + O(n * n) approx
    }

    static String start;
    static Map<String, Integer> level;
    static List<List<String>> output;

    static void dfs(String word, List<String> path) {
        if (word.equals(start)) {
            List<String> p1 = new ArrayList<>(path);
            Collections.reverse(p1);
            output.add(p1);
            return;
        }

        int steps = level.get(word);
        int wordLen = word.length();

        for (int i = 0; i < wordLen; i++) {
            for (char ch = 'a'; ch <= 'z'; ch++) {
                char[] charr = word.toCharArray();
                charr[i] = ch;

                String nword = new String(charr);

                if (level.containsKey(nword) && steps - level.get(nword) == 1) {
                    path.add(nword);
                    dfs(nword, path);
                    path.remove(path.size() - 1);
                }
            }
        }
    }

    static List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        output = new ArrayList<>();
        level = new HashMap<>();
        start = beginWord;

        Set<String> dict = new HashSet<>();
        dict.addAll(wordList);
        dict.remove(beginWord);

        Queue<String> q = new LinkedList<>();
        q.add(beginWord);

        int wordLen = beginWord.length();

        level.put(beginWord, 1);

        while (!q.isEmpty()) {
            String top = q.remove();
            int steps = level.get(top);

            if (top.equals(endWord)) {
                break;
            }

            for (int i = 0; i < wordLen; i++) {
                for (char ch = 'a'; ch <= 'z'; ch++) {
                    char[] charr = top.toCharArray();
                    charr[i] = ch;

                    String nword = new String(charr);

                    if (dict.contains(nword)) {
                        q.add(nword);
                        dict.remove(nword);
                        level.put(nword, steps + 1);
                    }
                }
            }
        }

        if (level.containsKey(endWord)) {
            List<String> path = new ArrayList<>();
            path.add(endWord);
            dfs(endWord, path);
        }

        return output;

        // Complexity analysis
        // Time : O(n * n)
        // Space : O(n) + O(n) + O(n)
    }
}
