import java.util.*;
import java.util.function.BiConsumer;
import java.util.function.BiPredicate;

public class Main2 {
    static final int INF = 0x3f3f3f3f;
    static int[] dirs = { -1, 0, 1, 0, -1 };

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        solve(sc);
    }

    public static void solve(Scanner sc) {
        int n = sc.nextInt();
        int m = sc.nextInt();
        sc.nextLine(); // Consume the newline

        String[][] s = new String[n][m];
        int[][] f = new int[n][m];
        int[][] g = new int[n][m];
        int[][] digit = new int[n][m];

        for (int[] row : f)
            Arrays.fill(row, INF);
        for (int[] row : g)
            Arrays.fill(row, INF);

        PriorityQueue<int[]> pq1 = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        PriorityQueue<int[]> pq2 = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));

        for (int i = 0; i < n; ++i) {
            s[i] = sc.nextLine().split(" ");
            for (int j = 0; j < m; ++j) {
                if (s[i][j].equals("S")) {
                    f[i][j] = 0;
                    pq1.add(new int[] { 0, i * m + j });
                } else if (s[i][j].equals("E")) {
                    g[i][j] = 0;
                    pq2.add(new int[] { 0, i * m + j });
                } else if (!s[i][j].equals("C") && !s[i][j].equals("B")) {
                    digit[i][j] = Integer.parseInt(s[i][j]);
                }
            }
        }

        BiPredicate<Integer, Integer> check = (i, j) -> digit[i][j] != 0 || !s[i][j].equals("B");

        BiConsumer<int[][], PriorityQueue<int[]>> update = (dp, pq) -> {
            while (!pq.isEmpty()) {
                int[] t = pq.poll();
                int d = t[0], x = t[1] / m, y = t[1] % m;
                for (int k = 0; k < 4; ++k) {
                    int nx = x + dirs[k], ny = y + dirs[k + 1];
                    if (0 <= nx && nx < n && 0 <= ny && ny < m && check.test(nx, ny)) {
                        if (digit[nx][ny] != 0) {
                            int w = digit[nx][ny];
                            if (dp[nx][ny] > dp[x][y] + w) {
                                dp[nx][ny] = dp[x][y] + w;
                                pq.add(new int[] { -dp[nx][ny], nx * m + ny });
                            }
                        } else {
                            if (dp[nx][ny] > dp[x][y]) {
                                dp[nx][ny] = dp[x][y];
                                pq.add(new int[] { -dp[nx][ny], nx * m + ny });
                            }
                        }
                    }
                }
            }
        };

        update.accept(f, pq1);
        update.accept(g, pq2);

        int ans = INF;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (s[i][j].equals("C") && f[i][j] != INF && g[i][j] != INF) {
                    ans = Math.min(ans, f[i][j] + g[i][j]);
                }
            }
        }
        if (ans == INF)
            ans = -1;
        System.out.println(ans);
    }
}
