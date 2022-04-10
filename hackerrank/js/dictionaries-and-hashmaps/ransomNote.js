function checkMagazine(magazine, note) {
    /**
     * Problem: Check if the <<note>> can be re-created using the words in <<magazine>>
     *  - Words are case-sensitive
     *  - Words cannot be re-used
     * 
     * 1. Create dictionary with:
     *  - Keys are the words in the magazine
     *  - Values are the # of occurences
     * 
     * 2. Check words in note:
     *  - If word exists in magazine dict, subtract -1 from value @ the key
     *  - If it doesn't, fail condition
     */
    let magDict = {};
    
    // Fill dictionary with number of occurences of each key
    for(let i = 0; i < magazine.length; i++) {
        if(!magDict[magazine[i]]) {
            magDict[magazine[i]] = 1;
        } else {
            magDict[magazine[i]]++;
        }
    }
    
    for(let i = 0; i < note.length; i++) {
        let word = note[i];
        
        if(magDict[word] == undefined || magDict[word] == 0) {
            return console.log("No");
        }
        else {
            magDict[word]--;
        }
    }

    console.log("Yes");
}

const input0 = ["two", "times", "three", "is", "not", "four"];
const input1 = ["two", "times", "two", "is", "four"];

process.stdout.write("Result 1: ");
checkMagazine(input0, input1);