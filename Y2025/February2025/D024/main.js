class User {
  constructor(userId) {
    this.userId = userId;
  }
}

class Tweet {
  constructor(tweetId, userId, index) {
    this.tweetId = tweetId;
    this.userId = userId;
    this.index = index;
  }
}

class Twitter {
  constructor() {
    this.index = 0;
    this.posts = new Map();
    this.followings = new Map();
  }

  /**
   * @param {number} userId
   * @param {number} tweetId
   * @return {void}
   */
  postTweet(userId, tweetId) {
    if (!this.posts.has(userId)) {
      this.posts.set(userId, new Array());
    }

    this.posts.get(userId).unshift(new Tweet(tweetId, userId, this.index));
    this.index++;

    // Complexity analysis
    // Time : O(N), N = number of tweets, considering array's general implemention
    // Space : O(1)
  }

  /**
   * @param {number} userId
   * @return {number[]}
   */
  getNewsFeed(userId) {
    const followings = this.followings.get(userId) || [];
    followings.push(userId);

    const t = followings.length;

    let pointers = new Array(t).fill(0);
    const postsSet = new Set();

    while (postsSet.size < 10) {
      let mini = -1; // index of following user who has most latest post

      for (let i = 0; i < t; i++) {
        if (!this.posts.get(followings[i]) || this.posts.get(followings[i]).length <= pointers[i]) continue;

        if (
          mini === -1 ||
          this.posts.get(followings[i])[pointers[i]].index > this.posts.get(followings[mini])[pointers[mini]].index
        ) {
          mini = i;
        }
      }

      if (mini === -1) break;

      postsSet.add(this.posts.get(followings[mini])[pointers[mini]].tweetId);
      pointers[mini] = pointers[mini] + 1;
    }

    return Array.from(postsSet);

    // Complexity analysis
    // Time : O(10T), T = number of followings
    // Space : O(1)
  }

  /**
   * @param {number} followerId
   * @param {number} followeeId
   * @return {void}
   */
  follow(followerId, followeeId) {
    if (!this.followings.has(followerId)) {
      this.followings.set(followerId, new Array());
    }

    this.followings.get(followerId).push(followeeId);

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @param {number} followerId
   * @param {number} followeeId
   * @return {void}
   */
  unfollow(followerId, followeeId) {
    const narr = this.followings.get(followerId)?.filter((fid) => fid !== followeeId) || [];
    this.followings.set(followerId, narr);

    // Complexity analysis
    // Time : O(FN), FN = number of followers
    // Space : O(1)
  }
}

const p1 = () => {
  // Problem 1 : Leetcode 355. Design Twitter - https://leetcode.com/problems/design-twitter/description/?envType=problem-list-v2&envId=2vp6ojv1
  // Geeksforgeeks - https://www.geeksforgeeks.org/problems/design-twitter/1

  const twitter = new Twitter();
  console.log(twitter.getNewsFeed(1));
  twitter.postTweet(1, 1);
  console.log(twitter.getNewsFeed(1));
  twitter.postTweet(2, 2);
  twitter.postTweet(2, 3);
  twitter.postTweet(2, 5);
  console.log(twitter.getNewsFeed(1));
  twitter.follow(1, 2);
  console.log(twitter.getNewsFeed(1));
  twitter.unfollow(1, 2);
  console.log(twitter.getNewsFeed(1));
};

class CustomStack {
  /**
   * @param {number} maxSize
   */
  constructor(maxSize) {
    this.capacity = maxSize;
    this.arr = new Array();
  }

  /**
   * @param {number} x
   * @return {void}
   */
  push(x) {
    if (this.arr.length === this.capacity) return;
    this.arr.push(x);

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @return {number}
   */
  pop() {
    if (this.arr.length === 0) return -1;
    return this.arr.pop();

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @param {number} k
   * @param {number} val
   * @return {void}
   */
  increment(k, val) {
    for (let i = 0; i < Math.min(k, this.arr.length); i++) {
      this.arr[i] += val;
    }

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : Leetcode 1381. Design a Stack With Increment Operation - https://leetcode.com/problems/design-a-stack-with-increment-operation/description/?envType=problem-list-v2&envId=2vp6ojv1

  const stack = new CustomStack();
  stack.push(1);
  stack.push(2);
  stack.push(3);
  console.log(stack.pop());
  stack.increment(1, 100);
  console.log(stack.pop());
  console.log(stack.pop());
};

(() => {
  // Day 24 of February 2025

  p1();

  p2();
})();
