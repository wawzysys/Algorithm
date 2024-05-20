import java.util.Scanner;

public class Main {
    private static int ans = 0;
    private static int m;
    private static int n;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        m = scanner.nextInt();
        n = scanner.nextInt();
        scanner.close();

        System.out.println(getResult());
    }

    private static void recursive(int l, int ll, int h, int r) {
        if (l == m - 1) {
            if (r - ll <= 3) {
                ans += 1;
            }
            return;
        }

        for (int i = ll; i <= h; i++) {
            r -= i;
            recursive(l + 1, i, Math.min(i + 3, r / (m - l - 1)), r);
            r += i;
        }
    }

    private static int getResult() {
        if (m == 1) {
            return 1;
        } else {
            recursive(0, 1, n / m, n);
            return ans;
        }
    }
}
