process.stdin.resume();
process.stdin.setEncoding('utf-8');

let input = '';

process.stdin.on('data', (data) => {
    input += data;
});


process.stdin.on('end',()=>{
    let inputArray = input.split('\n');
    let n = parseInt(inputArray[0].trim());
    let adj = Array.from({ length: n }, () => []);

    for (let i = 0; i < n; i++) {
        let line = inputArray[i + 1] ? inputArray[i + 1].trim() : '';
        if (line !== '') {
            let parts = line.split(/\s+/);
            for (let part of parts) {
                let neighbor = parseInt(part);
                adj[i].push(neighbor);
            }
            adj[i].sort((a, b) => a - b);
        }
    }

    let color = Array(n).fill(-1);
    let possible = true;
    for (let i = 0; i < n && possible; i++) {
        if (color[i] === -1) {
            let queue = [];
            color[i] = 0;
            queue.push(i);

            while (queue.length > 0 && possible) {
                let u = queue.shift();
                for (let v of adj[u]) {
                    if (color[v] === -1) {
                        color[v] = 1 - color[u];
                        queue.push(v);
                    } else if (color[v] === color[u]) {
                        possible = false;
                        break;
                    }
                }
            }
        }
    }
    if (!possible) {
        console.log("-1");
    } else {
        let group0 = [];
        let group1 = [];
        for (let i = 0; i < n; i++) {
            if (color[i] === 0) {
                group0.push(i);
            } else {
                group1.push(i);
            }
        }

        group0.sort((a, b) => a - b);
        group1.sort((a, b) => a - b);

        printList(group0);
        printList(group1);
    }
    function printList(list) {
        if (list.length === 0) {
            console.log();
            return;
        }
        console.log(list.join(' '));
    }
    process.exit();
});
