/**
 * @param {string} s
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var maximumGain = function (s, x, y) {
  // s = "aabbaaxybbaabb", x = 5, y = 4
  // aabbaaxybbaabb
  // aaxybb
  // [ab,ab,ab,ab]
  // s = "abbaaabbbbbaa", x = 4, y = 5
  // abbaaabbbbbaa
  // b
  // [ab, ab], [ba, ba, ba, ba]

  const removeAndGain = (str, char0, char1, score) => {
    const stack = [];
    let points = 0;

    for (const ch of str) {
      if (stack.length && stack.at(-1) === char0 && ch === char1) {
        points += score;
        stack.pop();
      } else {
        stack.push(ch);
      }
    }

    return { points, remainingString: stack.join("") };
  };

  let tpoints = 0;

  if (x >= y) {
    const pass1 = removeAndGain(s, "a", "b", x);
    const pass2 = removeAndGain(pass1.remainingString, "b", "a", y);
    tpoints = pass1.points + pass2.points;
  } else {
    const pass1 = removeAndGain(s, "b", "a", y);
    const pass2 = removeAndGain(pass1.remainingString, "a", "b", x);
    tpoints = pass1.points + pass2.points;
  }

  return tpoints;

  // Complexity analysis
  // Time : O(2N)
  // Space : O(N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1717. Maximum Score From Removing Substrings - https://leetcode.com/problems/maximum-score-from-removing-substrings/description/?envType=daily-question&envId=2025-07-23

  console.log(maximumGain("cdbcbbaaabab", 4, 5));
  console.log(maximumGain("aabbaaxybbaabb", 5, 4));
  console.log(
    maximumGain(
      "aabbabkbbbfvybssbtaobaaaabataaadabbbmakgabbaoapbbbbobaabvqhbbzbbkapabaavbbeghacabamdpaaqbqabbjbababmbakbaabajabasaabbwabrbbaabbafubayaazbbbaababbaaha",
      1926,
      4320
    )
  );
  console.log(
    maximumGain(
      "ababababababababababababababababababababababababababababababababababababababababababababababababab",
      3,
      2
    )
  );
  console.log(
    maximumGain(
      "babababababababababababababababababababababababababababababababababababababababababababababababababababa",
      6,
      7
    )
  );
  console.log(
    maximumGain(
      "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba",
      8,
      9
    )
  );
  console.log(
    maximumGain(
      "aaaaaaaabbbbbbbbbbaaaaaaaaabbbbbbbbbbaaaaaaaaabbbbbbbbbbaaaaaaaaabbbbbbbbbbaaaaaaaaabbbbbbbbbbaaaaaaaaabbbbbbbbbb",
      10,
      1
    )
  );
};

class Solution2 {
  subarraySum(arr) {
    // code here
    // TC 1
    // arr[] = [1, 2, 3]
    // [1]
    // [1,2]
    // [1,2,3]
    // [2]
    // [2,3]
    // [3]
    // TC 2
    // arr[] = [1, 2, 3, 4]
    // [1]
    // [1,2]
    // [1,2,3]
    // [1,2,3,4]
    // [2]
    // [2,3]
    // [2,3,4]
    // [3]
    // [3,4]
    // [4]
    // TC 3
    // 1 2 3 4 5 6 7
    // 1
    // 1 2
    // 1 2 3
    // 1 2 3 4
    // 1 2 3 4 5
    // 1 2 3 4 5 6
    // 1 2 3 4 5 6 7
    // 2
    // 2 3
    // 2 3 4
    // 2 3 4 5
    // 2 3 4 5 6
    // 2 3 4 5 6 7
    // 3
    // 3 4
    // 3 4 5
    // 3 4 5 6
    // 3 4 5 6 7
    // 4
    // 4 5
    // 4 5 6
    // 4 5 6 7
    // 5
    // 5 6
    // 5 6 7
    // 6
    // 6 7
    // 7

    // count of arr[0] & arr[N - 1 - 0] = (N - 0) * (1 + 0)
    // count of arr[1] & arr[N - 1 - 1] = (N - 1) * (1 + 1)
    // count of arr[2] & arr[N - 1 - 2] = (N - 2) * (1 + 2)
    // count of arr[3] & arr[N - 1 - 3] = (N - 3) * (1 + 3)
    // count of arr[4] & arr[N - 1 - 4] = (N - 4) * (1 + 4)

    const N = arr.length;

    if (N === 1) return arr[0];

    let sum = 0;

    let l = 0;
    let r = N - 1;

    while (l <= r) {
      if (l === r) {
        sum += (N - l) * (1 + l) * arr[l];
        l++;
      } else {
        sum += (N - l) * (1 + l) * arr[l];
        sum += (N - l) * (1 + l) * arr[r];
        l++;
        r--;
      }
    }

    return sum;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Sum of Subarrays - https://www.geeksforgeeks.org/problems/sum-of-subarrays2229/1

  const s2 = new Solution2();
  console.log(s2.subarraySum([1]));
  console.log(s2.subarraySum([1, 2]));
  console.log(s2.subarraySum([1, 2, 3]));
  console.log(s2.subarraySum([1, 2, 3, 5]));
  console.log(s2.subarraySum([1, 2, 3, 5, 7, 8]));
  console.log(s2.subarraySum([1, 2, 3, 5, 7, 8, 12]));
};

(() => {
  // Day 23 of July 2025

  p1();

  p2();
})();
