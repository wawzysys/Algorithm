process.stdin.resume();
process.stdin.setEncoding('utf-8');

process.stdin.on('data', (data) => {
    input += data;
});


process.stdin.on('end',()=>{
    let inputArray =input.split('\n');
    写在这
    process.exit();
});