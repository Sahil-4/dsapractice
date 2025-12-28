/**
 * @param {string} s
 * @return {string}
 */
var robotWithString = function (s) {
  const slen = s.length;

  const tstack = []; // for robot string t 
  const paper = []; // output 

  const minSuffix = new Array(slen + 1).fill('z');
  for (let i = slen - 1; i >= 0; i--) {
    minSuffix[i] = s[i] <= minSuffix[i + 1] ? s[i] : minSuffix[i + 1];
  }

  for (let i = 0; i < slen; i++) {
    tstack.push(s[i]);

    while (tstack.length && tstack.at(-1) <= minSuffix[i + 1]) {
      paper.push(tstack.pop());
    }
  }

  return paper.join("");

  // Complexity analysis 
  // Time : O(3N) 
  // Space : O(2N) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2434. Using a Robot to Print the Lexicographically Smallest String - https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/description/?envType=daily-question&envId=2025-06-06 

  console.log(robotWithString("zza"));
  console.log(robotWithString("bac"));
  console.log(robotWithString("bdda"));
  console.log(robotWithString("baca"));
};

/**
 * @param {string} pattern
 * @param {string} text
 * @returns {number[]}
 */
class Problem2 {
  search(pattern, text) {
    // Code here
    const ALPHA = 256;
    const PRIME = 101;

    const plen = pattern.length;
    const tlen = text.length;

    let phash = 0;
    let thash = 0;
    let power = 1;

    const out = [];

    for (let i = 0; i < plen - 1; i++) {
      power = (power * ALPHA) % PRIME;
    }

    // Compute initial hash values for pattern and first window of text
    for (let i = 0; i < plen; i++) {
      phash = (ALPHA * phash + pattern.charCodeAt(i)) % PRIME;
      thash = (ALPHA * thash + text.charCodeAt(i)) % PRIME;
    }

    // Slide the pattern over text one by one
    for (let i = 0; i <= tlen - plen; i++) {
      // If hash values match, check characters one by one
      if (phash === thash) {
        let match = true;
        for (let j = 0; j < plen; j++) {
          if (text[i + j] !== pattern[j]) {
            match = false;
            break;
          }
        }
        if (match) out.push(i + 1);
      }

      // Calculate hash value for the next window
      if (i < tlen - plen) {
        thash = (ALPHA * (thash - text.charCodeAt(i) * power) + text.charCodeAt(i + plen)) % PRIME;
        if (thash < 0) thash += PRIME;
      }
    }

    return out;

    // Complexity analysis 
    // Time : O(M + N) 
    // Space : O(1) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Search Pattern (Rabin-Karp Algorithm) - https://www.geeksforgeeks.org/problems/search-pattern-rabin-karp-algorithm--141631/1 

  const p2 = new Problem2();
  console.log(p2.search("birthdayboy", "birth"));
  console.log(p2.search("geeksforgeeks", "geek"));
  console.log(p2.search("geek", "geeksforgeeks"));
  console.log(p2.search("geeksforgeeks", "geeksforgeeks"));
  console.log(p2.search("azqicmrekxxsdbxwwgzjtnivtwgdkspjcmkyjjeesjeyqetjgcaxtsjhdmvzjliyyovgrtyinqbgzmtrtyiesziqzdzosmmbittmljficjhvkjvamrakttjnlewlndmiiqnqkvfuiktbwbyycdxqqfekpcbxgikgokwqflcyihdxiirwbpqgfbdghnyhqdmfqxlvkwnezywvrkhkogrndynflgymdjqdtintqdasvulzdvuojgsyicvyvybnqmjjvwwamakqvnfkyvhxhrftfvfkeypiofgcyxtnmhiqaxiqihngjerpgaxwbzkeksjnfflumbgwmeyawdlepxmikloqqezmhnuqyflsyzkpvbuxemsobkmubiicqqmjueeioyvkzalkcfymkajpnqinmhrahjsxneekspnmmdkxvtudfjvbhskyxcwkdgqpyazqicmrekxxsdbxwwgzjtnivtwgdkspjcmkyjjeesjeyqetjgcaxtsjhdmvzjliyyovgrtyinqbgzmtrtyiesziqzdzosmmbittmljficjhvkjvamrakttjnlewlndmiiqnqkvfuiktbwbyycdxqqfekpcbxgikgokwqflcyihdxiirwbpqgfbdghnyhqdmfqxlvkwnezywvrkhkogrndynflgymdjqdtintqdasvulzdvuoj", "azqicmrekxxsdbxwwgzjtnivtwgdkspjcmkyjjeesjeyqetjgcaxtsjhdmvzjliyyovgrtyinqbgzmtrtyiesziqzdzosmmbittmljficjhvkjvamrakttjnlewlndmiiqnqkvfuiktbwbyycdxqqfekpcbxgikgokwqflcyihdxiirwbpqgfbdghnyhqdmfqxlvkwnezywvrkhkogrndynflgymdjqdtintqdasvulzdvuoj"));
};


(() => {
  // Day 6 of June 2025

  p1();

  p2();
})();
