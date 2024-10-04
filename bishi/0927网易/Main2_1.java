import java.io.*;
import java.util.*;

public class Main2_1 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        int[] rm = new int[n + 1];
        int[] s = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            rm[i] = i;
            s[i] = 0;
        }


        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < q; i++) {

            st = new StringTokenizer(4
            0 3 1 3 
            0 2 3 5 
            3 3 1 2 
            3 3 1 3br.readLine());
            int t = Integer.parseInt(st.nextToken());

            if (t == 1) {
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                int tmp = rm[x];
                rm[x] = rm[y];
                rm[y] = tmp;
            } else if (t == 2) {
                int x = Integer.parseInt(st.nextToken());
                long y = Long.parseLong(st.nextToken());
                int a = (int)(y % m);
                s[x] = (s[x] + a) % m;
            } else if (t == 3) {
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                int or = rm[x];
                int sh = s[x];
                int oc = ((y - 1) + sh) % m + 1;
                long num = ((long)(or - 1) * m) + oc;
                sb.append(num).append('\n');
            }
        }
        System.out.print(sb.toString());
    }
}
