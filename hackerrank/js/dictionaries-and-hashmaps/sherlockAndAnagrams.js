// O(n^2), but |str| is constrained to 100 characters
function getAllSubstrings(str) {
    let result = [];

    for(let i = 0; i < str.length; i++) {

        // Add +1 since slice() does not include the character at the last index
        for(let j = i + 1; j < str.length + 1; j++) {
            result.push(str.slice(i, j));
        }
    }

    return result;
}

function charCounter(str) {
    const dict = {};

    for(let i = 0; i < str.length; i++) {
        const char = str[i];

        if(dict[char]) {
            dict[char]++;
        } else {
            dict[char] = 1;
        }
    }

    return dict;
}

function isAnagram(str1, str2) {
    if(str1.length != str2.length) {
        return false;
    }

    const str1Count = charCounter(str1);

    for(let j = 0; j < str2.length; j++) {
        const char = str2[j];

        // If the character in str2 is in the dictionary, subtract an occurence
        if(str1Count[char]) {
            str1Count[char]--;
        } else {
            return false;
        }
    }

    return true;
}

function sherlockAndAnagrams(s) {
    /** 
     * Problem: Find # of pairs of substrings of the string s that are anagrams of each other
     * Returns: <number>: # of unordered anagrammatic pairs of substrings
     * 
     * Constraints: 2 <= |s| <= 100
     * 
     * Anagram 
     *  - |s1| == |s2|
     *  - s1 and s2 contain the same characters
     * 
     * 1. Look at different lengths of substrings
     * 2. Make all possible combinations and put into pairs
     * 3. If they contain the same characters, it is an anagram
     * 2. Make words of characters, without re-using an index
     * 3. If words contain the same characters & same # of characters, is anagram
     *  - Increment # of anagrams
     */    

    // If there are no duplicate characters, there are no anagrams
    const numDupes = s.split("").filter((char, idx) => s.indexOf(char) != idx).length
    if(numDupes === 0) {
        return 0;
    }

    const substrings = getAllSubstrings(s);
    
    let numAnagrams = 0;
    for(let i = 0; i < substrings.length; i++) {
        let substr = substrings[i];
        let otherSubstrings = substrings.slice(i+1);

        for(let j = 0; j < otherSubstrings.length; j++) {
            let oSubstr = otherSubstrings[j];
            if(isAnagram(substr, oSubstr)) {
                numAnagrams++;
            }
        }
    }

    return numAnagrams;
}

console.log(
    "Result 1:",
    sherlockAndAnagrams("abba")
);

console.log(
    "Result 2:",
    sherlockAndAnagrams("abcd")
);

console.log(
    "Result 3:",
    sherlockAndAnagrams("ifailuhkqq")
);

console.log(
    "Result 4:",
    sherlockAndAnagrams("kkkk")
);

console.log(
    "Result 5:",
    sherlockAndAnagrams("cdcd")
);