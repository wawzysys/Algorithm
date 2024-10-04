let input = ''; // Initialize input before accumulating data

process.stdin.resume();
process.stdin.setEncoding('utf-8');

process.stdin.on('data', (data) => {
    input += data;
});

process.stdin.on('end', () => {
    let inputArray = input.trim().split('\n');
    
    // Begin of inserted code

    // Priority Queue implementation using a Max Heap
    class PriorityQueue {
        constructor() {
            this.heap = [];
        }

        // Swap elements at two indices
        swap(i, j) {
            [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
        }

        // Move the element at index 'i' up to maintain heap property
        bubbleUp(i) {
            while (i > 0) {
                let parent = Math.floor((i - 1) / 2);
                if (this.heap[i].danger > this.heap[parent].danger) {
                    this.swap(i, parent);
                    i = parent;
                } else {
                    break;
                }
            }
        }

        // Move the element at index 'i' down to maintain heap property
        bubbleDown(i) {
            const n = this.heap.length;
            while (true) {
                let largest = i;
                let left = 2 * i + 1;
                let right = 2 * i + 2;

                if (left < n && this.heap[left].danger > this.heap[largest].danger) {
                    largest = left;
                }

                if (right < n && this.heap[right].danger > this.heap[largest].danger) {
                    largest = right;
                }

                if (largest !== i) {
                    this.swap(i, largest);
                    i = largest;
                } else {
                    break;
                }
            }
        }

        // Insert a new node into the priority queue
        offer(node) {
            this.heap.push(node);
            this.bubbleUp(this.heap.length - 1);
        }

        // Remove and return the node with the highest danger
        poll() {
            if (this.isEmpty()) return null;
            const top = this.heap[0];
            const end = this.heap.pop();
            if (!this.isEmpty()) {
                this.heap[0] = end;
                this.bubbleDown(0);
            }
            return top;
        }

        // Check if the priority queue is empty
        isEmpty() {
            return this.heap.length === 0;
        }
    }

    // Define the Node structure
    class Node {
        constructor(x, y, danger) {
            this.x = x;
            this.y = y;
            this.danger = danger;
        }
    }

    // Parsing input
    let currentLine = 0;
    const [M, N] = inputArray[currentLine++].trim().split(' ').map(Number);
    const [a1, a2] = inputArray[currentLine++].trim().split(' ').map(Number);
    const [b1, b2] = inputArray[currentLine++].trim().split(' ').map(Number);

    // Initialize grid and d matrices
    const g = Array.from({ length: M }, () => Array(N).fill(0));
    const d = Array.from({ length: M }, () => Array(N).fill(-1));

    // List of infected cells
    let inf = [];

    for (let i = 0; i < M; i++) {
        const row = inputArray[currentLine++].trim().split(' ').map(Number);
        for (let j = 0; j < N; j++) {
            g[i][j] = row[j];
            if (g[i][j] === 2 || g[i][j] === 3) {
                d[i][j] = 0;
                inf.push([i, j]);
            }
        }
    }

    let day = 0;
    const dx = [0, 0, 1, -1];
    const dy = [1, -1, 0, 0];

    while (inf.length > 0) {
        day++;
        // Initialize D matrix for this day
        const D = Array.from({ length: M }, () => Array(N).fill(0));

        // Initialize priority queue
        const pq = new PriorityQueue();

        for (const [x, y] of inf) {
            const danger = (g[x][y] === 2) ? a2 : a1;
            pq.offer(new Node(x, y, danger));
            D[x][y] = danger;
        }

        // Spread danger using priority queue
        while (!pq.isEmpty()) {
            const current = pq.poll();
            const { x, y, danger } = current;

            for (let k = 0; k < 4; k++) {
                const nx = x + dx[k];
                const ny = y + dy[k];
                if (nx >= 0 && nx < M && ny >= 0 && ny < N && g[nx][ny] !== 1) {
                    const nd = danger - 1;
                    if (nd > 0 && D[nx][ny] < nd) {
                        D[nx][ny] = nd;
                        pq.offer(new Node(nx, ny, nd));
                    }
                }
            }
        }

        // List for new infections
        const newInf = [];
        for (let i = 0; i < M; i++) {
            for (let j = 0; j < N; j++) {
                if ((g[i][j] === 4 || g[i][j] === 5) && d[i][j] === -1) {
                    const th = (g[i][j] === 4) ? b2 : b1;
                    if (D[i][j] >= th) {
                        d[i][j] = day;
                        newInf.push([i, j]);
                    }
                }
            }
        }

        // Update grid based on new infections
        for (const [x, y] of newInf) {
            if (g[x][y] === 4) g[x][y] = 2;
            else if (g[x][y] === 5) g[x][y] = 3;
        }

        // Update inf for next day
        inf = newInf;
    }

    // Prepare and output the result
    const outputLines = [];
    for (let i = 0; i < M; i++) {
        const line = [];
        for (let j = 0; j < N; j++) {
            let res;
            if (g[i][j] === 0 || g[i][j] === 1) res = -1;
            else res = d[i][j];
            line.push(res);
        }
        outputLines.push(line.join(' '));
    }

    console.log(outputLines.join('\n'));

    // End of inserted code

    process.exit();
});
