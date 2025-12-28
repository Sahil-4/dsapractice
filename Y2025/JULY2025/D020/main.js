/**
 * @param {string[][]} paths
 * @return {string[][]}
 */
var deleteDuplicateFolder = function (paths) {
  class Node {
    constructor(val) {
      this.val = val; // folder name
      this.subFolder = ""; // serialized subfolder structure
      this.children = new Map(); // children: Map<string, Node>
    }
  }

  function getNode(val) {
    return new Node(val);
  }

  function insert(root, path) {
    for (let folder of path) {
      if (!root.children.has(folder)) {
        root.children.set(folder, getNode(folder));
      }
      root = root.children.get(folder);
    }
  }

  function populateNodes(root, subFolderMap) {
    let subFolderPaths = [];

    for (let [childName, childNode] of root.children) {
      const subFolderResult = populateNodes(childNode, subFolderMap);
      subFolderPaths.push([childName, subFolderResult]);
    }

    subFolderPaths.sort((a, b) => a[0].localeCompare(b[0]));

    let completePath = "";
    for (let [childName, childPath] of subFolderPaths) {
      completePath += `(${childName}${childPath})`;
    }

    root.subFolder = completePath;

    if (completePath !== "") {
      subFolderMap.set(completePath, (subFolderMap.get(completePath) || 0) + 1);
    }

    return completePath;
  }

  function removeDuplicates(root, subFolderMap) {
    for (let [childName, childNode] of Array.from(root.children)) {
      if (childNode.subFolder !== "" && subFolderMap.get(childNode.subFolder) > 1) {
        root.children.delete(childName);
      } else {
        removeDuplicates(childNode, subFolderMap);
      }
    }
  }

  function constructResult(root, path, result) {
    for (let [childName, childNode] of root.children) {
      path.push(childName);
      result.push([...path]);
      constructResult(childNode, path, result);
      path.pop();
    }
  }

  // Main logic
  const root = getNode("/");
  for (let path of paths) {
    insert(root, path);
  }

  const subFolderMap = new Map();
  populateNodes(root, subFolderMap);

  removeDuplicates(root, subFolderMap);

  const result = [];
  const currentPath = [];
  constructResult(root, currentPath, result);
  return result;
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1948. Delete Duplicate Folders in System - https://leetcode.com/problems/delete-duplicate-folders-in-system/description/?envType=daily-question&envId=2025-07-20

  console.log(deleteDuplicateFolder([["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]));
  console.log(
    deleteDuplicateFolder([
      ["a"],
      ["c"],
      ["a", "b"],
      ["c", "b"],
      ["a", "b", "x"],
      ["a", "b", "x", "y"],
      ["w"],
      ["w", "y"],
    ])
  );
  console.log(deleteDuplicateFolder([["a", "b"], ["c", "d"], ["c"], ["a"]]));
};

/**
 * @param {number} n
 * @param {number[]} arr
 * @returns {number}
 */
class Solution2 {
  countValid(n, arr) {
    // code here
    // n = 1, arr = [1, 2, 3]
    // Total = 9
    // INV = 6
    // VAL = 3 (output)
    // n = 2, arr[] = [3, 5]
    // Total = 9 * 10 = 90
    // INV = 7 * 8 = 56
    // VAL = 34
    // n = 5, arr[] = [1,2,3,5]
    // Total = 9 * 10^4 = 90000
    // INV = 5 * 6^4 = 6480
    // VAL = 83520

    const pow = Math.pow;
    const m = arr.length;
    const zero = arr.reduce((acc, e) => (e == 0 ? 1 : acc), 0);

    const Total = 9 * pow(10, n - 1);
    const INVALID = (9 - m + zero) * pow(10 - m, n - 1);
    const VALID = Total - INVALID;
    return VALID;

    // Complexity analysis
    // Time : O(Log(N)) for calculating power
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Count Numbers Containing Specific Digits - https://www.geeksforgeeks.org/problems/count-numbers-containing-specific-digits/1

  const s2 = new Solution2();
  console.log(s2.countValid(1, [1, 2, 5]));
  console.log(s2.countValid(1, [1, 2, 0, 5]));
  console.log(s2.countValid(2, [1, 2, 5]));
  console.log(s2.countValid(2, [1, 2, 0, 5]));
  console.log(s2.countValid(5, [1, 2, 5]));
  console.log(s2.countValid(5, [1, 2, 0, 5]));
  console.log(s2.countValid(9, [1, 0, 3]));
  console.log(s2.countValid(9, [1, 0, 3, 2, 4, 5, 6, 7, 8, 9]));
};

(() => {
  // Day 20 of July 2025

  p1();

  p2();
})();
