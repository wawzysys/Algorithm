///E/0Code/Algorithm/acw/1128.java
import java.io.*;
import java.util.StringTokenizer;
import java.util.Scanner;
public class acw1128 {
    public static Reader in;
    public static PrintWriter out;
    static int INF = 0x3f3f3f3f;
    public static void main(String[] args) {
        out = new PrintWriter(new BufferedOutputStream(System.out));
        in = new Reader();
        // int t = in.nextInt();
        // while (t-- > 0)
            solve();
        out.close();
    }
    static void solve(){
        int n = in.nextInt(), m = in.nextInt();
        int N = n + 5;
        int[][] g= new int[N][N];
        for (int i = 0; i < N; i ++ )
        	for (int j = 0; j < N; j ++ )
        		g[i][j] = INF;
        g[1][1] = 0;
        int mm = 0;
        for (int i = 0; i < m; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            int c = in.nextInt();
            g[a][b] = Math.min(g[a][b], c);
            g[b][a] = Math.min(g[b][a], c);
        }
        for (int k = 1; k <= n; k ++ )
        	for (int i = 1; i <= n; i ++ )
        		for (int j = 1; j <= n; j ++ )
        			g[i][j] = Math.min(g[i][j], g[i][k] + g[k][j]);
        for (int i = 1; i <= n; i ++ )

        	if (g[1][i] == INF){
        		mm = -1;
        		out.println(-1);
        		return;
        	}
        	else{
        		mm = Math.max(mm, g[1][i]);
        	}
        out.println(mm);
        return;
    }
 
    static class Reader {
        private BufferedReader br;
        private StringTokenizer st;
 
        Reader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }
 
        boolean hasNext(){
            try {
                while (st == null || !st.hasMoreElements()) {
                    st = new StringTokenizer(br.readLine());
                }
            }catch (Exception e){
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