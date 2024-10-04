import java.util.*;

public class Main1 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int a = s.nextInt(), b = s.nextInt(), c = s.nextInt();
        int m = s.nextInt();
        int[][] r = new int[m][];
        Map<Integer, List<Integer>> st = new HashMap<>();
        boolean[] A = new boolean[m];
        boolean[] B = new boolean[m];
        boolean[] C = new boolean[m];
        for (int i = 0; i < m; i++) {
            int k = s.nextInt();
            r[i] = new int[k];
            for (int j = 0; j < k; j++) {
                int x = s.nextInt();
                r[i][j] = x;
                st.computeIfAbsent(x, y -> new ArrayList<>()).add(i);
                if (x == a) A[i] = true;
                if (x == b) B[i] = true;
                if (x == c) C[i] = true;
            }
        }
        List<Integer>[] adj = new List[m];
        for (int i = 0; i < m; i++) adj[i] = new ArrayList<>();
        for (List<Integer> l : st.values()) {
            for (int i = 0; i < l.size(); i++) {
                int u = l.get(i);
                for (int j = i + 1; j < l.size(); j++) {
                    int v = l.get(j);
                    adj[u].add(v);
                    adj[v].add(u);
                }
            }
        }
        Queue<int[]> q = new LinkedList<>();
        boolean[][] vis = new boolean[m][2];
        for (int i = 0; i < m; i++) {
            if (A[i]) {
                int f = B[i] ? 1 : 0;
                q.offer(new int[]{i, f, 1});
                vis[i][f] = true;
            }
        }
        while (!q.isEmpty()) {
            int[] p = q.poll();
            int u = p[0], f = p[1], d = p[2];
            if (C[u] && f == 1) {
                System.out.println(d);
                return;
            }
            for (int v : adj[u]) {
                int nf = f;
                if (B[v]) nf = 1;
                if (!vis[v][nf]) {
                    vis[v][nf] = true;
                    q.offer(new int[]{v, nf, d + 1});
                }
            }
        }
        System.out.println("-1");
    }
}
