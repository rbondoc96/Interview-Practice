function longestPalindrome(s) {
    if(s.length == 1) {
        return s;
    }
    let result = "";

    for(let i = 0; i < s.length; i++) {
        
        // Odd palindromes
        let left = i;
        let right = i;
        while(left >= 0 && right < s.length && s[left] === s[right]) {
            if(right - left + 1 > result.length) {
                result = s.slice(left, right+1);
            }

            left--;
            right++;
        }

        // Even palindromes
        left = i;
        right = i+1;
        while(left >= 0 && right < s.length && s[left] === s[right]) {
            if(right - left + 1 > result.length) {
                result = s.slice(left, right+1);
            }

            left--;
            right++;
        }
    }

    return result;
}

let str = "babad"
console.log(
    "Result 1:",
    longestPalindrome(str)
)

str = "cbbd"
console.log(
    "Result 2:",
    longestPalindrome(str)
)

str = "a"
console.log(
    "Result 3:",
    longestPalindrome(str)
)

str = "ac"
console.log(
    "Result 4:",
    longestPalindrome(str)
)

str = "bb"
console.log(
    "Result 5:",
    longestPalindrome(str)
)