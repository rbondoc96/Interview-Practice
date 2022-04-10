function sockMerchant(n, ar) {
    // Write your code here
    if(n == 1) {
        return 0;
    }
    
    let socks = [ar[0]];
    let numPairs = 0;
    
    for(let i = 1; i < n; i++) {
        let sock = ar[i];
        if(socks.includes(sock)) {
            let index = socks.indexOf(sock);
            socks.splice(index, 1);
            numPairs++;
        } else {
            socks.push(sock);
        }
    }

    return numPairs;
}