import java.util.Scanner;

public class t2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for (int testCase = 0; testCase < T; testCase++) {
            long a = sc.nextLong();
            long b = sc.nextLong();
            long c = sc.nextLong();
            long x = sc.nextLong();
            long y = sc.nextLong();
            System.out.println(maxSets(a, b, c, x, y));
        }
    }

    public static long maxSets(long a, long b, long c, long x, long y) {
        long left = 0;
        long right = a + b + c;
        while (left < right) {
            long mid = (left + right + 1) / 2;
            long l_min = Math.max(0, mid - c);
            long k_min = Math.max(0, mid + y * l_min - b);
            long k_max = (a - mid) / x;
            if (k_min <= k_max) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
}
