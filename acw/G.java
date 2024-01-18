import java.io.*;
import java.util.StringTokenizer;

public class G {
    public static Reader in;
    public static PrintWriter out;

    public static void main(String[] args) {
        out = new PrintWriter(new BufferedOutputStream(System.out));
        in = new Reader();
        int t = in.nextInt();
        while (t-- > 0)
            solve();
        out.close();
    }

    static void solve() {
        int n = in.nextInt(), m = in.nextInt(), k = in.nextInt();
        char[][] c = new char[n][m];
        for (int i = 0; i < n; i++) {
            c[i] = in.nextLine().toCharArray();
        }
        if (n > m) {
            // rev
            char[][] cc = new char[m][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    cc[j][i] = c[i][j];
                }
            }
            c = cc;
            int t = n;
            n = m;
            m = t;
        }
        int[][] ps = new int[n][m + 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                ps[i][j + 1] = ps[i][j];
                if (c[i][j] == '#')
                    ps[i][j + 1]++;
            }
        }
        int re = 0;
        {

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    int tmp = 0;
                    for (int l = 0; l <= k; l++) {
                        if (i + l >= n)
                            break;
                        int up = Math.min(m, j + k - l + 1);
                        tmp += ps[i + l][up] - ps[i + l][j];
                    }
                    re = Math.max(re, tmp);
                }
            }

        }
        {

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    int tmp = 0;
                    for (int l = 0; l <= k; l++) {
                        if (i - l < 0)
                            break;
                        int up = Math.min(m, j + k - l + 1);
                        tmp += ps[i - l][up] - ps[i - l][j];
                    }
                    re = Math.max(re, tmp);
                }
            }

        }
        {

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    int tmp = 0;
                    for (int l = 0; l <= k; l++) {
                        if (i + l >= n)
                            break;
                        int down = Math.max(0, j - k + l);
                        tmp += ps[i + l][j + 1] - ps[i + l][down];
                    }
                    re = Math.max(re, tmp);
                }
            }
        }
        {

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    int tmp = 0;
                    for (int l = 0; l <= k; l++) {
                        if (i - l < 0)
                            break;
                        int down = Math.max(0, j - k + l);
                        tmp += ps[i - l][j + 1] - ps[i - l][down];
                    }
                    re = Math.max(re, tmp);
                }
            }

        }
        out.println(re);

    }

    static int qmi(long a, int b, int p) {
        long ans = 1;
        a = (a % p + p) % p;
        for (; b > 0; b >>= 1) {
            if ((b & 1) != 0)
                ans = (a * ans) % p;
            a = (a * a) % p;
        }
        return (int) ans;
    }

    static class Reader {
        private BufferedReader br;
        private StringTokenizer st;

        Reader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        boolean hasNext() {
            try {
                while (st == null || !st.hasMoreElements()) {
                    st = new StringTokenizer(br.readLine());
                }
            } catch (Exception e) {
                return false;
            }
            return true;
        }

        String next() {
            try {
                while (st == null || !st.hasMoreTokens()) {
                    st = new StringTokenizer(br.readLine());
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        int[] nextIntArray(int n) {
            int[] arr = new int[n];
            for (int i = 0; i < n; i++)
                arr[i] = nextInt();
            return arr;
        }

        long[] nextLongArray(int n) {
            long[] arr = new long[n];
            for (int i = 0; i < n; i++)
                arr[i] = nextLong();
            return arr;
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        String nextLine() {
            String s = "";
            try {
                s = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return s;
        }
    }
}