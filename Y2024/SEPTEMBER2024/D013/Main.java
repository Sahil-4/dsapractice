
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.PriorityQueue;

class Post {
    int time; // simple integer 1, 2, 3, ...
    int userId; // userId of user posted tweet
    int tweetId; // actual tweet

    public Post(int time, int uId, int tId) {
        this.time = time;
        this.userId = uId;
        this.tweetId = tId;
    }
}

class Twitter {
    // User : userId: List<followId> - Map
    private final HashMap<Integer, LinkedHashSet<Integer>> users; // user -> follows

    // Tweet : num: <userId, tweetId> - PriorityQueue
    private final PriorityQueue<Post> posts; // see Post class definition
    private int currtime = 0; // taking variable to handle time state

    public Twitter() {
        users = new HashMap<>();
        posts = new PriorityQueue<>((Post p1, Post p2) -> p2.time - p1.time);

        // Complexity analysis
        // Time : O(1)
        // Space : O(1)
    }

    public void postTweet(int userId, int tweetId) {
        posts.add(new Post(++currtime, userId, tweetId));

        // Complexity analysis
        // Time : O(log(n))
        // Space : O(1)
    }

    public List<Integer> getNewsFeed(int userId) {
        List<Integer> feed = new ArrayList<>();

        // perform all operations on copy dataset
        PriorityQueue<Post> timeline = new PriorityQueue<>(posts);
        while (!timeline.isEmpty() && feed.size() < 10) {
            Post p = timeline.poll();

            if (userId == p.userId || (users.containsKey(userId) && users.get(userId).contains(p.userId))) {
                // this post belongs to user or user's follows
                feed.add(p.tweetId);
            }
        }

        return feed;

        // Complexity analysis
        // Time : O(n * log(n))
        // Space : O(n), copying complete posts dataset
    }

    public void follow(int followerId, int followeeId) {
        if (!users.containsKey(followerId)) {
            users.put(followerId, new LinkedHashSet<>());
        }

        users.get(followerId).add(followeeId);

        // Complexity analysis
        // Time : O(1), java internally hashset implementation
        // Space : O(1)
    }

    public void unfollow(int followerId, int followeeId) {
        if (!users.containsKey(followerId)) return;
        users.get(followerId).remove(followeeId);

        // Complexity analysis
        // Time : O(1), java internally hashset implementation
        // Space : O(1)
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 5 of Heaps

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 355. Design Twitter -
        // https://leetcode.com/problems/design-twitter/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/design-twitter/0

        Twitter t1 = new Twitter();
        t1.postTweet(1, 5);
        System.out.println(t1.getNewsFeed(1).toString());
        t1.follow(1, 2);
        t1.postTweet(2, 6);
        System.out.println(t1.getNewsFeed(1).toString());
        t1.unfollow(1, 2);
        System.out.println(t1.getNewsFeed(1).toString());
    }
}