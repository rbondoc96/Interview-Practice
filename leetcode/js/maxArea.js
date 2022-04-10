function maxArea(height) {
    //  BRUTE FORCE - O(n^2)
    // if(height.length == 2) {
    //     return Math.min(height[0], height[1]);
    // }

    // let area = 0;
    // for(let i = 0; i < height.length; i++) {
    //     let heightI = height[i];
    //     for(let j = 1; j < height.length; j++) {
    //         let heightJ = height[j];

    //         area = Math.max(area,
    //             ((j - i) * Math.min(heightI, heightJ))   
    //         )
    //     }
    // }
    // return area;

    if(height.length == 2) {
        return Math.min(height[0], height[1]);
    }

    let area = 0;
    let i = 0, j = height.length - 1;

    while(i < j) {
        let width = j - i;

        area = Math.max(area,
            (width * Math.min(height[i], height[j]))   
        )

        if(height[i] < height[j]) {
            i++;
        } else {
            j--;
        }
    }

    return area;
}

let height = [1,8,6,2,5,4,8,3,7];
console.log(
    "Result 1:",
    maxArea(height)
)

height = [1,1];
console.log(
    "Result 2:",
    maxArea(height)
)

height = [4,3,2,1,4];
console.log(
    "Result 3:",
    maxArea(height)
)
height = [1,2,1];
console.log(
    "Result 4:",
    maxArea(height)
)

height = [1,2];
console.log(
    "Result 4:",
    maxArea(height)
)