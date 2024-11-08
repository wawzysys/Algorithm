const rl = require("readline").createInterface({ input: process.stdin });
var iter = rl[Symbol.asyncIterator]();
const readline = async () => (await iter.next()).value;
void async function () {
    const nStr = await readline();
    let n = BigInt(nStr);
    let days = 0;
    while (n > 0n) {
        let eat;
        if (isPrime(n)) {
            eat = n / 3n + 1n;
        } else {
            eat = n / 2n + 1n;
        }
        n -= eat;
        days++;
    }
    console.log(days);

    function isPrime(n) {
        if (n <= 1n) return false;
        if (n === 2n) return true;
        if (n % 2n === 0n) return false;
        const sqrtN = sqrt(n);
        for (let i = 3n; i <= sqrtN; i += 2n) {
            if (n % i === 0n) return false;
        }
        return true;
    }

    function sqrt(value) {
        if (value < 0n) {
            throw ''
        }
        if (value < 2n) {
            return value;
        }

        function newtonIteration(n, x0) {
            const x1 = (n / x0 + x0) >> 1n;
            if (x0 === x1 || x0 === x1 - 1n) {
                return x0;
            }
            return newtonIteration(n, x1);
        }

        return newtonIteration(value, 1n);
    }
}()
