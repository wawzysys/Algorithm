const rl = require("readline").createInterface({ input: process.stdin });
var iter = rl[Symbol.asyncIterator]();
const readline = async () => (await iter.next()).value;

void async function(){
    let line = await readline();
    if (line === undefined) {
        console.log("0.00B");
        process.exit(0);
    }

    let bytes = parseInt(line.trim(), 10);

    const units = [
        {name: 'GB', bytes: 1024 ** 3},
        {name: 'MB', bytes: 1024 ** 2},
        {name: 'KB', bytes: 1024},
        {name: 'B', bytes: 1}
    ];

    let result = '';

    for(let unit of units){
        if(bytes >= unit.bytes){
            let value = bytes / unit.bytes;
            let roundedValue = value.toFixed(2);
            result = `${roundedValue}${unit.name}`;
            break;
        }
    }

    if(result === ''){
        let roundedValue = bytes.toFixed(2);
        result = `${roundedValue}B`;
    }

    console.log(result);
}();
