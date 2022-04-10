function twoStrings(s1, s2) {
    /**
     * Problem: Is there a matching substring between s1 and s2? 1 character counts as a substring
     * 
     * 1. Create map for s1
     * 2. Loop through s2 and see if there are characters in s2 that match keys in s1
     */

    let map1 = {};

    for(let i = 0; i < s1.length; i++) {
        let char = s1[i];

        map1[char] = true;
    }

    for(let i = 0; i < s2.length; i++) {
        let char = s2[i];

        if(map1[char]) {
            return "YES";
        }
    }

    return "NO";
}

console.log(
    "Result 1:",
    twoStrings("hello", "world")
);

console.log(
    "Result 2:",
    twoStrings("be", "cat")
);