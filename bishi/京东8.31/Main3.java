import java.util.*;

public class Main3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        int[][] a = new int[2][n];
        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < n; ++j) {
                a[i][j] = scanner.nextInt();
            }
        }

        int[][] r = new int[2][n];
        int[][] dp = new int[2][n];
        dp[1][n - 1] = a[1][n - 1];
        dp[0][n - 1] = a[0][n - 1] + dp[1][n - 1];

        for (int j = n - 2; j >= 0; --j) {
            for (int i = 0; i < 2; ++i) {
                r[i][j] = dp[i][j + 1] + a[i][j];
            }
            for (int i = 0; i < 2; ++i) {
                if ((i + j) % 2 != 0) {
                    dp[i][j] = Math.max(dp[i][j + 1], r[i ^ 1][j]) + a[i][j];
                } else {
                    dp[i][j] = Math.min(dp[i][j + 1], r[i ^ 1][j]) + a[i][j];
                }
            }
        }

        System.out.println(dp[0][0]);
    }
}