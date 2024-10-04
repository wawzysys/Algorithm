const rl = require("readline").createInterface({ input: process.stdin });
var iter = rl[Symbol.asyncIterator]();
const readline = async () => (await iter.next()).value;
void async function(){
    class MinHeap {
        constructor() {
            this.heap = [];
        }
        swap(i, j) {
            [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
        }
        push(item) {
            this.heap.push(item);
            this.bubbleUp(this.heap.length - 1);
        }

        pop() {
            if (this.heap.length === 0) return null;
            const min = this.heap[0];
            const end = this.heap.pop();
            if (this.heap.length > 0) {
                this.heap[0] = end;
                this.bubbleDown(0);
            }
            return min;
        }
        peek() {
            return this.heap.length > 0 ? this.heap[0] : null;
        }

        bubbleUp(idx) {
            while (idx > 0) {
                let parent = Math.floor((idx - 1) / 2);
                if (this.heap[parent][0] > this.heap[idx][0]) {
                    this.swap(parent, idx);
                    idx = parent;
                } else {
                    break;
                }
            }
        }
        bubbleDown(idx) {
            const length = this.heap.length;
            while (true) {
                let smallest = idx;
                let left = 2 * idx + 1;
                let right = 2 * idx + 2;

                if (left < length && this.heap[left][0] < this.heap[smallest][0]) {
                    smallest = left;
                }

                if (right < length && this.heap[right][0] < this.heap[smallest][0]) {
                    smallest = right;
                }

                if (smallest !== idx) {
                    this.swap(idx, smallest);
                    idx = smallest;
                } else {
                    break;
                }
            }
        }

        size() {
            return this.heap.length;
        }
    }
    function minCost(n, m, a, roads, s, t) {
        const graph = Array.from({ length: n + 1 }, () => []);
        for (let i = 0; i < m; i++) {
            const [u, v, l, w] = roads[i];
            const cost = BigInt(a) * BigInt(l) + BigInt(w);
            graph[u].push([v, cost]);
            graph[v].push([u, cost]);
        }

        const INF = BigInt("1000000000000000000"); 
        const dist = Array(n + 1).fill(INF);
        dist[s] = BigInt(0);

        const heap = new MinHeap();
        heap.push([dist[s], s]);

        while (heap.size() > 0) {
            const [currentCost, u] = heap.pop();

            if (u === t) {
                return currentCost.toString();
            }

            if (currentCost > dist[u]) continue;
            for (const [v, cost] of graph[u]) {
                const newCost = currentCost + cost;
                if (newCost < dist[v]) {
                    dist[v] = newCost;
                    heap.push([newCost, v]);
                }
            }
        }
        return dist[t] === INF ? "-1" : dist[t].toString();
    }

    const input = [];
    for await (const line of rl) {
        if (line.trim() !== "") {
            input.push(line.trim());
        }
    }

    let idx = 0;
    const [n, m, a] = input[idx++].split(' ').map(Number);

    const roads = [];
    for (let i = 0; i < m; i++) {
        const [u, v, l, w] = input[idx++].split(' ').map(Number);
        roads.push([u, v, l, w]);
    }

    const [s, t] = input[idx++].split(' ').map(Number);
    const result = minCost(n, m, a, roads, s, t);
    console.log(result);
}();
