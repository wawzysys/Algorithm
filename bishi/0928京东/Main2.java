import java.util.Scanner;

public class Main2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int[][] a = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                a[i][j] = sc.nextInt();
            }
        }
        int front = 0;
        for (int j = 0; j < m; j++) {
            int colMax = 0;
            for (int i = 0; i < n; i++) {
                colMax = Math.max(colMax, a[i][j]);
            }
            front += colMax;
        }
        int left = 0;
        for (int i = 0; i < n; i++) {
            int rowMax = 0;
            for (int j = 0; j < m; j++) {
                rowMax = Math.max(rowMax, a[i][j]);
            }
            left += rowMax;
        }
        int top = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (a[i][j] > 0) {
                    top++;
                }
            }
        }
        System.out.println(front + " " + left + " " + top);

        sc.close();
    }
}
