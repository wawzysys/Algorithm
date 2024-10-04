const rl = require("readline").createInterface({ input: process.stdin });
var iter = rl[Symbol.asyncIterator]();
const readline = async () => (await iter.next()).value;

void async function(){

    const firstLine = (await readline()).trim().split(/\s+/).map(Number);
    const n = firstLine[0];
    const m = firstLine[1];
    

    const matrix = [];
    for(let i = 0; i < n; i++){
        const line = (await readline()).trim().split(/\s+/).map(Number);
        matrix.push(line);
    }
    

    let original_sum = 0;
    const sum_row = Array(n).fill(0);
    const row_max = Array(n).fill(-Infinity);
    const sum_col = Array(m).fill(0);
    const column_max = Array(m).fill(-Infinity);
    
    for(let i = 0; i < n; i++){
        for(let j = 0; j < m; j++){
            const val = matrix[i][j];
            original_sum += val;
            sum_row[i] += val;
            if(val > row_max[i]){
                row_max[i] = val;
            }
            sum_col[j] += val;
            if(val > column_max[j]){
                column_max[j] = val;
            }
        }
    }
    
    let max_sum = -Infinity;
    

    for(let i = 0; i < n; i++){
        for(let j = 0; j < m; j++){
            const col_max_after = Math.max(column_max[j], row_max[i]);
            
            const final_sum = original_sum
                            - sum_row[i]
                            - sum_col[j]
                            + matrix[i][j]
                            + row_max[i] * (m -1)
                            + col_max_after * n;
            
            if(final_sum > max_sum){
                max_sum = final_sum;
            }
        }
    }
    console.log(max_sum);
}()
