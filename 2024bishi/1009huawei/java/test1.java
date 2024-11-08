import java.util.*;

public class test1 {
    public static int minMoves(List<List<Integer>> maze, int x, int y) {
        int n = maze.size();
        if (n == 0)
            return -1;
        int m = maze.get(0).size();
        int[][] dirs = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };

        List<int[]> coins = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (maze.get(i).get(j) == 2) {
                    coins.add(new int[] { i, j });
                }
            }
        }
        int k = coins.size();

        int tot = k + 2;
        List<int[]> points = new ArrayList<>();
        points.add(new int[] { 0, 0 });
        for (int[] coin : coins) {
            points.add(coin);
        }
        points.add(new int[] { x, y });

        int[][] dist = new int[tot][tot];
        for (int i = 0; i < tot; i++) {
            Arrays.fill(dist[i], -1);
            int[] start = points.get(i);
            boolean[][] vis = new boolean[n][m];
            Queue<int[]> queue = new LinkedList<>();
            queue.offer(new int[] { start[0], start[1], 0 });
            vis[start[0]][start[1]] = true;
            while (!queue.isEmpty()) {
                int[] cur = queue.poll();
                int r = cur[0];
                int c = cur[1];
                int steps = cur[2];
                for (int j = 0; j < tot; j++) {
                    if (points.get(j)[0] == r && points.get(j)[1] == c) {
                        dist[i][j] = steps;
                    }
                }
                for (int[] d : dirs) {
                    int nr = r + d[0];
                    int nc = c + d[1];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < m && !vis[nr][nc] && maze.get(nr).get(nc) != 1) {
                        vis[nr][nc] = true;
                        queue.offer(new int[] { nr, nc, steps + 1 });
                    }
                }
            }
        }

        for (int i = 0; i <= k; i++) {
            for (int j = 1; j <= k + 1; j++) {
                if (i == j)
                    continue;
                if (dist[i][j] == -1) {
                    return -1;
                }
            }
        }

        int size = 1 << k;
        int[][] dp = new int[size][tot];
        for (int[] row : dp)
            Arrays.fill(row, Integer.MAX_VALUE);
        int initmask = 0;
        for (int i = 0; i < k; i++) {
            if (points.get(0)[0] == coins.get(i)[0] && points.get(0)[1] == coins.get(i)[1]) {
                initmask |= (1 << i);
            }
        }
        dp[initmask][0] = 0;

        for (int mask = 0; mask < (1 << k); mask++) {
            for (int u = 0; u < tot; u++) {
                if (dp[mask][u] == Integer.MAX_VALUE)
                    continue;
                for (int c = 0; c < k; c++) {
                    if ((mask & (1 << c)) != 0)
                        continue;
                    int v = c + 1;
                    int newMask = mask | (1 << c);
                    if (dp[newMask][v] > dp[mask][u] + dist[u][v]) {
                        dp[newMask][v] = dp[mask][u] + dist[u][v];
                    }
                }
            }
        }

        int lstmask = (1 << k) - 1;
        int mi = Integer.MAX_VALUE;
        for (int u = 0; u < tot; u++) {
            if (dp[lstmask][u] == Integer.MAX_VALUE)
                continue;
            if (dist[u][k + 1] == -1)
                continue;
            mi = Math.min(mi, dp[lstmask][u] + dist[u][k + 1]);
        }

        return mi == Integer.MAX_VALUE ? -1 : mi;
    }
}
