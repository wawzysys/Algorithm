const rl = require("readline").createInterface({ input: process.stdin });
var iter = rl[Symbol.asyncIterator]();
const readline = async () => (await iter.next()).value;
void async function(){
    const [n, m] = (await readline()).split(' ').map(Number);
    const a = (await readline()).split(' ').map(Number);
    const gcd = Array.from({ length: n }, () => Array(n).fill(0));
    for(let i = 0; i < n; i++) {
        gcd[i][i] = a[i];
        for(let j = i+1; j < n; j++) {
            gcd[i][j] = gcdFunction(gcd[i][j-1], a[j]);
        }
    }
    const dp = Array.from({ length: n+1 }, () => Array(m+1).fill(-Infinity));
    dp[0][0] = 0;
    for(let i = 1; i <= n; i++) {
        for(let j = 1; j <= Math.min(m, i); j++) {
            for(let k = j-1; k < i; k++) {
                if(dp[k][j-1] !== -Infinity) {
                    dp[i][j] = Math.max(dp[i][j], dp[k][j-1] + gcd[k][i-1]);
                }
            }
        }
    }
    console.log(dp[n][m]);
    function gcdFunction(x, y) {
        while(y !== 0) {
            let temp = y;
            y = x % y;
            x = temp;
        }
        return x;
    }
}()
