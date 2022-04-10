function repeatedString(s, n) {
    // Write your code here
    if(s == "a") {
        return n;
    }
    
    let numAs = s.split("").filter(c => c === "a").length;
    
    if(s.length == n) {
        return numAs;
    }
    
    let timesToRepeat = Math.floor(n / s.length);
    let trailingChars = n % s.length;
    
    return (numAs * timesToRepeat) + (s.slice(0, trailingChars).split("").filter(c => c == "a").length)
}