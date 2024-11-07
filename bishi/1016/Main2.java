import java.util.*;

public class Main2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        long res = 0;
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
            res += a[i];
        }
        double ans = (double) res / 7;
        int j = 0;
        long s = 0;
        long best = res;
        for (int r = 0; r < n; r++) {
            s += a[r];
            while (s > ans && j <= r) {
                long t = Math.max(res - s, 6 * s);
                if (t < best) {
                    best = t;
                }
                s -= a[j++];
            }
            long t = Math.max(res - s, 6 * s);
            if (t < best) {
                best = t;
            }
        }
        System.out.println(best);
    }
}
