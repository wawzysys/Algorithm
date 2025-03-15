import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String s = sc.next();
        sc.close();

        long[] prefixCount = new long[n + 1];
        long[] sumPos = new long[26];
        long[] count = new long[26];

        for (int i = 1; i <= n; i++) {
            char c = s.charAt(i - 1);
            int idx = c - 'a';
            long newPal = count[idx] * (i - 1L) - sumPos[idx];
            prefixCount[i] = prefixCount[i - 1] + newPal;
            count[idx]++;
            sumPos[idx] += i;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            sb.append(prefixCount[i]);
            if (i < n) sb.append(" ");
        }
        System.out.println(sb);
    }
}
