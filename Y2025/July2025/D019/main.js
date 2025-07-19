/**
 * @param {string[]} folder
 * @return {string[]}
 */
var removeSubfolders = function (folder) {
  // keep a set of parent folders
  // sort the folder[], based on length (in ASC order)
  // go to folder[i], say folder[i] = '/a/b/c'
  // split folder[i] on '/', splits = ['', 'a', 'b', 'c']
  // starting from splits[1] go till splits[LAST_INDEX]
  // check '/' + splits[1] in parent folder, if present discard folder[i]
  // else check '/' + splits[1] + '/' + splits[2], then check '/' + splits[1] + '/' + splits[2] + '/' + splits[3] and so on
  // if no one found add folder[i], in parent folder (set)
  // at the end return array of parent folder
  // NOTE : This can be solved using trie data structure
  // but as the constraints are low and sorting is still needed
  // this approach is sufficient for now
  // but if constraints grows consider using custom trie

  const comparator = (f1, f2) => f1.length - f2.length;
  const folders = [...folder].sort(comparator);

  const parents = new Set();

  for (const folder of folders) {
    let flag = true;
    const splits = folder.split("/");
    for (let s = 2; s <= splits.length; s++) {
      const key = "/" + splits.slice(1, s).join("/");
      if (parents.has(key)) {
        flag = false;
        break;
      }
    }

    if (flag) parents.add(folder);
  }

  return Array.from(parents);

  // Complexity analysis
  // Time : O(N) + O(N * Log(N)) + O(N * M) + O(N)
  // Space : O(N) + O(N + M)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1233. Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/?envType=daily-question&envId=2025-07-19

  console.log(removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]));
  console.log(removeSubfolders(["/a", "/a/b/c", "/a/b/d"]));
  console.log(removeSubfolders(["/a/b/c", "/a/b/ca", "/a/b/d"]));
  console.log(removeSubfolders(["/ah/al/am", "/ah/al"]));
};

// @param {string}
// @return {number}
class Solution2 {
  vowelCount(s) {
    // code here
    // count frequency of a, e, i, o, u
    // comn = 1
    // if freq(vowel) != 0
    // comb * = freq(vowel);
    // then perm = fact(numberOfVowel)
    // return comb * perm

    // simplified code
    const vowels = ["a", "e", "i", "o", "u"];

    const freq = { a: 0, e: 0, i: 0, o: 0, u: 0 };
    for (let c of s) {
      if (!vowels.includes(c)) continue;
      freq[c]++;
    }

    let comb = 1;
    let perm = 1;
    let vowelCount = 0;

    for (let v of vowels) {
      if (freq[v] === 0) continue;
      comb *= freq[v]; // combination (f1 * f2 * ...)
      vowelCount++;
      perm *= vowelCount; // just computing factorial (1 * 1 * 2 * ...)
    }

    return vowelCount !== 0 ? perm * comb : 0;

    // Complexity analysis
    // Time : O(N) + O(5) for building final output
    // Space : O(1) + used some arrays to store vowels and frequency
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Count Unique Vowel Strings - https://www.geeksforgeeks.org/problems/count-unique-vowel-strings/1

  const s2 = new Solution2();
  console.log(s2.vowelCount("aeiou"));
  console.log(s2.vowelCount("ae"));
  console.log(s2.vowelCount("aabcef"));
  console.log(s2.vowelCount("a"));
  console.log(s2.vowelCount("x"));
};

(() => {
  // Day 19 of July 2025

  p1();

  p2();
})();
