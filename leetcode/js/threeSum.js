function threeSum(nums) {
    nums.sort();

    let prevA, prevB;
    let triplets = [];

    for(let i = 0; i < nums.length; i++) {
        // Ignore duplicate numbers
        if(prevA != nums[i]) {
            let target = 0 - nums[i];

            let left = i+1;
            let right = nums.length - 1;

            while(left < right) {
                if(nums[left] != prevB) {
                    let sum = nums[left] + nums[right];
                    if(sum == target) {
                        triplets.push([
                            nums[i],
                            nums[left],
                            nums[right]
                        ])
                    }
                }
                prevB = nums[left++];
                right--;
            }
        }

        prevA = nums[i];

        // // Search for 2 numbers that add up to the target
        // for(let x = i + 1; x < nums.length; x++) {
        //     let diff = target - nums[x];

        //     if(prevMap[diff] != undefined) {
        //         triplets.push(
        //             [
        //                 nums[i], 
        //                 nums[x],
        //                 nums[prevMap[diff]]
        //             ]
        //         )
        //     } else {
        //         prevMap[nums[x]] = x;
        //     }
        // }
    }

    return triplets;
}

let nums = [-1, 0, 1, 2, -1, -4];
console.log(
    "Result 1:",
    threeSum(nums)
);