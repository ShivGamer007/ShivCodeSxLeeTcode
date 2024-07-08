/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findTheWinner = function(n, k) {
    win = 0;
    for(let i=1; i<=n; i++){
        win = (win + k) % i;
    }
    return win + 1;
    
};