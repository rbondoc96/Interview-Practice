function jumpingOnClouds(c) {
    // Write your code here
    
    let idx = 0;
    let jumps = 0;
    
    while(idx < c.length - 1) {
        if(c[idx + 2] == 0) {
            idx+=2;
            jumps++;
        }
        else if(c[idx + 1] == 0 && c[idx + 2] == 1) {
            idx++;
            jumps++;
        }
        else if(c[idx + 1] == 0 && (idx+2) == c.length) {
            idx++;
            jumps++;
        }
    }

    return jumps;
}