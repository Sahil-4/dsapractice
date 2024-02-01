#include <conio.h>
#include <stdio.h>
#include <stdlib.h>

void p1() {
    // Problem 1 : Two Sum - https://www.codingninjas.com/studio/problems/two-sum_839653 

	// sort the array 
    int arr[] = {2, 7, 11, 13};
    int n = 4, target = 9;

    int ans[n][2];
    int i = 0;

	// assuming that array is sorted now // by any O(n * log(n)) algorithm 

	int l = 0, h = n-1;

	while (l < h) {
		if (arr[l] + arr[h] == target) {
			ans[i][0] = arr[l];
			ans[i][1] = arr[h];
			l++;
			h--;
            i++;
			continue;
		}

		if (arr[l] + arr[h] > target) {
			h--;
		} else {
			l++;
		}
	}

	if (i == 0) {
		ans[i][0] = -1;
        ans[i][1] = -1;
	}

    for (int o = 0; o < i; o++) {
        printf("%d %d\n", ans[o][0], ans[o][1]);
    }
}

void p2() {
    // Problem 2 : Count characters - https://www.codingninjas.com/studio/problems/count-vowels-consonants-and-spaces_5026361 

    // count : vowels, consonants and spaces 
    // means : {a, e, i, o, u}, {b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z}, {' '} 
    // and {A, E, I, O, U}, {B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z}, {' '} 

    char str[] = "This is Alpha";
    int i = 0;
    int vowels_count = 0;
    int consonants_count = 0;
    int spaces_count = 0;

    while (str[i] != '\0') {
        if (str[i] == ' ') spaces_count++;
        if (str[i] >= 'A' && str[i] <= 'Z' || str[i] >= 'a' && str[i] <= 'z') {
            // capital letter 
            if (str[i] == 'A' || str[i] == 'E' || str[i] == 'I' || str[i] == 'O' || str[i] == 'U'
            || str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u') {
                vowels_count++;
            } else {
                consonants_count++;
            }
        }
        i++;
    }

    printf("Total vowels : %d consonants : %d and spaces : %d", vowels_count, consonants_count, spaces_count);
}

void p3() {
    // Problem 3 : lower case to upper case - https://www.geeksforgeeks.org/problems/lower-case-to-upper-case3410/1 

    // convert {a-z} to {A-Z} 
    // ASCII of {a-z} is {97-122} 
    // and {A-Z} is {65-90} 
    // so first we have to check the char whether it is in this range or not 
    // if char is not in this range do not perform any operation on it 
    // if char is in this range then range also we have to just change lower case to upper case 
    // so in this also we have to target chars in the range {97-122} 
    // now we have to convert them to upper case 
    // for example we have to change 97 to 65 and 122 to 90 
    // means we have to subtract 32 

    char str[] = "This is Alpha";
    int i = 0;

    while (str[i] != '\0') {
        if (str[i] >= 'a' && str[i] <= 'z') {
            str[i] = str[i] - 32;
        }
        i++;
    }

    printf("%s", str);
}


int main() {
    // Day 23 

    // p1();

    // p2();

    // p3();


    return 0;
}