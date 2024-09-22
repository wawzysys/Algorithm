import java.io.*;
import java.util.*;

public class Main3 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine().trim());

        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine().trim());
            String[] parts = br.readLine().trim().split("\\s+");
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(parts[i]);
            }

            Set<Integer> st = new HashSet<>();
            for (int num : a)
                st.add(num);

            if (st.contains(0) || st.size() != n) {
                sb.append("yes\n");
            } else {
                Arrays.sort(a);
                boolean ok = false;
                outer: for (int i = 0; i < n - 2; i++) {
                    for (int j = i + 1; j < n - 1; j++) {
                        for (int k = j + 1; k < n; k++) {
                            if (a[i] + a[j] == a[k]) {
                                ok = true;
                                break outer;
                            }
                        }
                    }
                }
                sb.append(ok ? "yes\n" : "no\n");
            }
        }
        System.out.print(sb.toString());
    }
}
