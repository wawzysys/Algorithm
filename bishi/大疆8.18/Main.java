import java.util.*;

class Solution {
    public int numberOfPatrolBlocks1(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }
        int[] dx = { 0, 1, 0, -1 };
        int[] dy = { 1, 0, -1, 0 };
        int direction = 0;
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] vis = new boolean[m][n];
        int x = 0, y = 0;
        int patrolCount = 0;
        while (true) {
            if (!vis[x][y]) {
                vis[x][y] = true;
                patrolCount++;
                System.out.println("x: " + x + " y: " + y);
            }
            int nextX = x + dx[direction];
            int nextY = y + dy[direction];
            if (nextX < 0 || nextX >= m || nextY < 0 || nextY >= n || grid[nextX][nextY] == 1) {

                direction = (direction + 1) % 4;
                nextX = x + dx[direction];
                nextY = y + dy[direction];
                if (nextX < 0 || nextX >= m || nextY < 0 || nextY >= n || grid[nextX][nextY] == 1
                        || vis[nextX][nextY]) {
                    break;
                }
            }
            x = nextX;
            y = nextY;
        }
        return patrolCount;
    }

    public int numberOfPatrolBlocks2(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }

        Map<Integer, Integer> dx = new HashMap<>();
        Map<Integer, Integer> dy = new HashMap<>();

        dx.put(0, 0);
        dy.put(0, 1); // 向东
        dx.put(1, 1);
        dy.put(1, 0); // 向南
        dx.put(2, 0);
        dy.put(2, -1); // 向西
        dx.put(3, -1);
        dy.put(3, 0); // 向北

        int direction = 0;
        int m = grid.length;
        int n = grid[0].length;
        boolean[][][] vis = new boolean[m][n][4];
        boolean[][] vis1 = new boolean[m][n];
        int x = 0, y = 0;
        int patrolCount = 0;
        while (true) {
            if (!vis[x][y][direction]) {
                vis[x][y][direction] = true;
                if (!vis1[x][y]) {
                    vis1[x][y] = true;
                    patrolCount++;
                }
            }
            int nextX = x + dx.get(direction);
            int nextY = y + dy.get(direction);
            if (nextX < 0 || nextX >= m || nextY < 0 || nextY >= n || grid[nextX][nextY] == 1) {

                direction = (direction + 1) % 4;
                nextX = x + dx.get(direction);
                nextY = y + dy.get(direction);
                if (nextX < 0 || nextX >= m || nextY < 0 || nextY >= n || grid[nextX][nextY] == 1
                        || vis[nextX][nextY][direction]) {
                    break;
                }
            }
            x = nextX;
            y = nextY;
        }
        return patrolCount;
    }
}

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int block_rows = 0;
        int block_cols = 0;
        block_rows = in.nextInt();
        block_cols = in.nextInt();

        Solution dp = new Solution();
        int[][] grid = new int[block_rows][block_cols];

        for (int i = 0; i < block_rows; i++) {
            for (int j = 0; j < block_cols; j++) {
                grid[i][j] = in.nextInt();
            }
        }
        in.close();
        // int[][] block1 = {
        // { 0, 0, 1, 0 },
        // { 0, 0, 0, 0 },
        // { 0, 1, 0, 0 }
        // };
        System.out.println(dp.numberOfPatrolBlocks1(grid));
        System.out.println(dp.numberOfPatrolBlocks2(grid));
    }
}
