import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        int v = sc.nextInt();
        sc.close();
        System.out.println(getResult(n, a, v));
    }

    public static int getResult(int n, int[] a, int v) {
        int ans = 0;
        int l = 0;
        int r = 0;
        int ss = 0;

        while (r < n) {
            ss += a[r];
            while (ss > v) {
                ss -= a[l];
                l++;
            }
            if (ss <= v) {
                ans = Math.max(ans, r - l + 1);
            }
            r++;
        }
        return ans;
    }
}
