function twoSum(nums, target) {
    let prevNums = {};
    
    for(let i = 0; i < nums.length; i++) {
        let diff = target - nums[i];
        
        if(prevNums[diff] != undefined) {
            return [prevNums[diff], i];
        }
        prevNums[nums[i]] = i;
    }
};

let nums = [2,7,11,15];
console.log(
    "Result 1:",
    twoSum(nums, 9)
);

nums = [1,2,4];
console.log(
    "Result 2:",
    twoSum(nums, 6)
);

nums = [3,3];
console.log(
    "Result 3:",
    twoSum(nums, 6)
);