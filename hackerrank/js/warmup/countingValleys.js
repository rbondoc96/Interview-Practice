function countingValleys(steps, path) {
    // Write your code here
    
    let level = 0; // Starting at Sea Level
    let prevLevel = 0; // Track level at previous step
    let valleys = 0; // # of valleys
    
    for(let i = 0; i < steps; i++) {
        // Track previous level
        prevLevel = level;
        
        // Increment/decrement level
        // U = +1
        // D = -1
        if(path[i] == "U") {
            level++;
        } else if(path[i] == "D") {
            level--;
        } else {
            continue;
        }
        
        // Reached Sea Level with the current step
        if(level == 0) {
            // Previous step was below sea level
            if(prevLevel < 0) {
                valleys++;
            }
        }
    }
    
    return valleys;
}