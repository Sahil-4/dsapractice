#include <iostream>
#include <map>
#include <string>

using namespace std;

bool areIsomorphic(string str1, string str2) {
    // save time dont do any calculation 
    if (str1.length() != str2.length()) return false; 

    // store mapping 
    map<char, char> charactersMap1;
    map<char, char> charactersMap2;

    // map 
    for (int i = 0; i < str1.length(); i++) {
        // mapping str1[i] to str2[i] 
        // if char already present and mapped to different char 
        if (charactersMap1.find(str1[i]) != charactersMap1.end() 
        && charactersMap1.at(str1[i]) != str2[i]) return false;

        // if char is not already present 
        if (charactersMap1.find(str1[i]) == charactersMap1.end()) {
            charactersMap1.insert({str1[i], str2[i]});
        }

        // mapping str2[i] to str1[i] 
        // if char already present and mapped to different char 
        if (charactersMap2.find(str2[i]) != charactersMap2.end() 
        && charactersMap2.at(str2[i]) != str1[i]) return false;

        // if char is not already present 
        if (charactersMap2.find(str2[i]) == charactersMap2.end()) {
            charactersMap2.insert({str2[i], str1[i]});
        }
        // second map is because it is possible that 
        // str1[i] is not mapped to any other char or mapped to str2[i] only 
        // but what is str2[i] is mapped to any char of str1 
        // in this case we will get wrong answer 
        // we can iterate through the map if we dont want to use second map 
    }

    return true;
}

void p1() {
    // Problem 1 : Isomorphic string - https://www.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1 

    // string str1 = "bab";pijthbsfy
    // string str2 = "dxd";
    string str1 = "pijthbsfy";
    string str2 = "fvladzpbf";

    bool truth = areIsomorphic(str1, str2);

    cout << truth << endl;
}

int main() {
    // Day 6 

    p1();


    return 0;
}