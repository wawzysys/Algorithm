///E/0Code/Algorithm/acw/ac2128.java
import java.io.*;
import java.util.StringTokenizer;
import java.util.Scanner;
public class  {
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
    static void solve(){
        int n = in.nextInt(), m = in.nextInt(), k = in.nextInt();
        char[][] c = new char[n][m];
        for (int i = 0; i < n; i++) {
            c[i] = in.nextLine().toCharArray();
        }
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