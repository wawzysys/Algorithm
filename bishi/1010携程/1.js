const rl = require("readline").createInterface({ input: process.stdin });
var iter = rl[Symbol.asyncIterator]();
const readline = async () => (await iter.next()).value;
void async function(){
    const T = parseInt(await readline());
    for(let i = 0; i < T; i++) {
        let s = await readline();
        let words = s.split(/[_ ]+/);
        let pascalCase = words.map(word => word.charAt(0).toUpperCase() + word.slice(1)).join('');
        console.log(pascalCase);
    }
}()
