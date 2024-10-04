import java.util.*;

public class Main2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int q = sc.nextInt();

        int[] rm = new int[n + 1];
        int[] s = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            rm[i] = i;
            s[i] = 0;
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < q; i++) {
            int t = sc.nextInt();
            if (t == 1) {
                int x = sc.nextInt();
                int y = sc.nextInt();
                int tmp = rm[x];
                rm[x] = rm[y];
                rm[y] = tmp;
            } else if (t == 2) {
                int x = sc.nextInt();
                long y = sc.nextLong();
                if (m == 0)
                    continue;
                int a = (int) (y % m);
                s[x] = (s[x] + a) % m;
            } else if (t == 3) {
                int x = sc.nextInt();
                int y = sc.nextInt();
                int or = rm[x];
                int sh = s[x];
                int oc = ((y - 1) + sh) % m + 1;
                long num = ((long) (or - 1) * m) + oc;
                sb.append(num).append('\n');
            }
        }
        System.out.print(sb.toString());
    }
}
