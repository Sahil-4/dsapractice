/**
 * @param {string[]} recipes
 * @param {string[][]} ingredients
 * @param {string[]} supplies
 * @return {string[]}
 */
var findAllRecipes = function (recipes, ingredients, supplies) {
  let answer = [];
  const RN = recipes.length;

  // map of recipe and set of supplies - for O(1) look up
  const recipeMap = recipes.reduce((acc, e, i) => acc.set(e, i) && acc, new Map());
  const suppliesSet = new Set(supplies);

  // function to make a recipe
  const makeRecipe = (i, path) => {
    // look for ingreds in supplies
    // if all ingreds found
    // make the food, add it into ingreds, and answer
    // then return

    path.add(i);

    for (let ingredient of ingredients[i]) {
      if (!suppliesSet.has(ingredient)) {
        // make ingredient, if we have recipe of it
        let ni = recipeMap.get(ingredient);
        let check = ni && !path.has(ni) && makeRecipe(recipeMap.get(ingredient), path);

        if (!check) return false;
      }
    }

    // recipe is completed
    suppliesSet.add(recipes[i]);
    answer.push(recipes[i]);
    return true;
  };

  for (let i = 0; i < RN; i++) {
    if (suppliesSet.has(recipes[i])) continue;
    makeRecipe(i, new Set());
  }

  return answer;

  // Complexity analysis
  // Time : O(RN) + O(S) + O(RN * IG) ~
  // Space : O(RN) + O(S) + O(RN) stack
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2115. Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/?envType=daily-question&envId=2025-03-21

  console.log(findAllRecipes(["bread"], [["yeast", "flour"]], ["yeast", "flour", "corn"]));
  console.log(
    findAllRecipes(
      ["x", "zpmcz", "h", "q"],
      [
        ["cpivl", "zpmcz", "h", "e", "fzjnm", "ju"],
        ["h", "fzjnm", "e", "q", "x"],
        ["d", "hveml", "cpivl", "q", "zpmcz", "ju", "e", "x"],
        ["f", "hveml", "cpivl"],
      ],
      ["f", "hveml", "cpivl", "d"],
    ),
  );
  console.log(
    findAllRecipes(
      ["bread", "sandwich", "burger"],
      [
        ["yeast", "flour"],
        ["bread", "meat"],
        ["sandwich", "meat", "bread"],
      ],
      ["yeast", "flour", "meat"],
    ),
  );
};

/**
 * @param {number[]} arr
 * @returns {number}
 */
class Problem2 {
  findMaxSum(arr) {
    // code here

    // return this.recursion(arr, -1);

    // const n = arr.length;
    // const memo = new Array(n+1).fill(-1);
    // return this.memoize(arr, 0, memo);

    return this.tabulation(arr);
  }

  recursion(arr, i) {
    if (i >= arr.length) return 0;

    let not_pick = this.recursion(arr, i + 1);
    let pick = i == -1 ? 0 : arr[i] + this.recursion(arr, i + 2);

    return Math.max(not_pick, pick);

    // Complexity analysis
    // Time : O(2^N)
    // Space : O(N) stack space
  }

  memoize(arr, i, memo) {
    if (i > arr.length) return 0;

    if (memo[i] != -1) return memo[i];

    let not_pick = this.memoize(arr, i + 1, memo);
    let pick = i == 0 ? 0 : arr[i - 1] + this.memoize(arr, i + 2, memo);

    return (memo[i] = Math.max(not_pick, pick));

    // Complexity analysis
    // Time : O(2*N)
    // Space : O(N) stack space + O(N) memory
  }

  tabulation(arr) {
    const n = arr.length;
    const memo = new Array(n + 3).fill(0);

    for (let i = n; i >= 0; i--) {
      let not_pick = memo[i + 1];
      let pick = i == 0 ? 0 : arr[i - 1] + memo[i + 2];
      memo[i] = Math.max(not_pick, pick);
    }

    return memo[0];

    // Complexity analysis
    // Time : O(N)
    // Space : O(N) memory
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Stickler Thief - https://www.geeksforgeeks.org/problems/stickler-theif-1587115621/1

  console.log(new Problem2().findMaxSum([6, 5, 5, 7, 4]));
  console.log(new Problem2().findMaxSum([1, 5, 3]));
  console.log(new Problem2().findMaxSum([4, 4, 4, 4]));
};

(() => {
  // Day 21 of March 2025

  p1();

  p2();
})();
