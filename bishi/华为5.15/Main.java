import java.util.*;

public class Main {
    public static String parseToAbPattern(String pattern) {
        int i = 0;
        StringBuilder result = new StringBuilder();
        while (i < pattern.length()) {
            if (pattern.charAt(i) == 'N') {
                result.append('b');
                i++;
            } else if (pattern.charAt(i) == 'A') {
                result.append('a');
                i++;
            } else if (Character.isDigit(pattern.charAt(i))) {
                int j = i;
                while (j < pattern.length() && Character.isDigit(pattern.charAt(j))) {
                    j++;
                }
                int count = Integer.parseInt(pattern.substring(i, j));
                if (j < pattern.length() && pattern.charAt(j) == '(') {
                    int depth = 1;
                    int k = j + 1;
                    while (k < pattern.length() && depth > 0) {
                        if (pattern.charAt(k) == '(') {
                            depth++;
                        } else if (pattern.charAt(k) == ')') {
                            depth--;
                        }
                        k++;
                    }
                    String subpattern = parseToAbPattern(pattern.substring(j + 1, k - 1));
                    for (int c = 0; c < count; ++c) {
                        result.append(subpattern);
                    }
                    i = k;
                } else {
                    result.append("{").append(count).append("}");
                    i = j;
                }
            } else {
                i++;
            }
        }
        return result.toString();
    }

    public static long getHash(long[] h, long[] p, int l, int r, long mod) {
        long res = (h[r] - h[l - 1] * p[r - l + 1] % mod + mod) % mod;
        return res;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String pattern = scanner.nextLine();
        pattern = parseToAbPattern(pattern);

        String s = scanner.nextLine();

        StringBuilder tep = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                tep.append('b');
            } else {
                tep.append('a');
            }
        }

        int n = tep.length();
        int n2 = pattern.length();
        long base = 131;
        long mod = 1000000007;

        long[] h = new long[n + 1];
        long[] p = new long[n + 1];
        p[0] = 1;

        if (n2 > n) {
            System.out.println("!");
            return;
        }

        for (int i = 1; i <= n; ++i) {
            p[i] = p[i - 1] * base % mod;
            h[i] = (h[i - 1] * base + tep.charAt(i - 1)) % mod;
        }

        long[] h1 = new long[n2 + 1];
        for (int i = 1; i <= n2; ++i) {
            h1[i] = (h1[i - 1] * base + pattern.charAt(i - 1)) % mod;
        }

        boolean flag = false;
        for (int i = 1; i <= n - n2 + 1; ++i) {
            int j = i + n2 - 1;
            if (j > n) {
                break;
            }
            if (getHash(h, p, i, j, mod) == h1[n2]) {
                flag = true;
                System.out.println(s.substring(i - 1, i - 1 + n2));
                break;
            }
        }

        if (!flag) {
            System.out.println("!");
        }
    }
}
