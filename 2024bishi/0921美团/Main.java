import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for (int t = 0; t < T; t++) {
            long n = sc.nextLong();
            long ans;

            if (n == 1) {
                ans = 1;
            } else {
                int steps = calculateSteps(n - 1);
                ans = 2 + steps;
            }

            System.out.println(ans);
        }

        sc.close();
    }

    static int calculateSteps(long x) {
        int ans = 0;
        x--;
        while (x > 0) {
            x >>= 1;
            ans++;
        }
        return ans;
    }
}
