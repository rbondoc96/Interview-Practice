function lengthOfLongestSubstring(s) {
    if(s.length === 0 || s.length === 1) {
        return s.length;
    }
    
    let charSet = new Set();
    let left = 0;
    let maxLen = 0;

    for(let right = 0; right < s.length; right++) {
        let rightChar = s[right];

        while(charSet.has(rightChar)) {
            charSet.delete(s[left++]);
        }
        charSet.add(rightChar);  
        maxLen = Math.max(maxLen, charSet.size);
    }

    return maxLen;
};

let str = "abcabcbb"
console.log(
    "Result 1:",
    lengthOfLongestSubstring(str)
);

str = "bbbbb"
console.log(
    "Result 2:",
    lengthOfLongestSubstring(str)
);

str = ""
console.log(
    "Result 3:",
    lengthOfLongestSubstring(str)
);