import java.util.*;

public class Main2_1 {
    private static final long INF = (long)1e18;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        solve(sc);
        sc.close();
    }
    private static void solve(Scanner sc) {
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int n = sc.nextInt();
        long[] dp = new long[n];
        Arrays.fill(dp, INF);
        Map<Integer, List<Integer>> graph = new HashMap<>();
        List<List<Integer>> st = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            st.add(new ArrayList<>());
        }
        for (int i = 0; i < n; i++) {
            int k = sc.nextInt(); 
            for (int j = 0; j < k; j++) {
                int key = sc.nextInt();
                st.get(i).add(key);
                graph.computeIfAbsent(key, x -> new ArrayList<>()).add(i);
            }
        }
        Queue<Integer> queue = new LinkedList<>();
        List<Integer> graphB = graph.getOrDefault(b, new ArrayList<>());
        for (int idx : graphB) {
            if (dp[idx] > 0) { 
                dp[idx] = 0;
                queue.offer(idx);
            }
        }
        while (!queue.isEmpty()) {
            int current = queue.poll();
            for (int key : st.get(current)) {
                List<Integer> neighbors = graph.getOrDefault(key, new ArrayList<>());
                for (int neighbor : neighbors) {
                    if (dp[neighbor] > dp[current] + 1) {
                        dp[neighbor] = dp[current] + 1;
                        queue.offer(neighbor);
                    }
                }
            }
        }
        long t1 = INF;
        List<Integer> graphA = graph.getOrDefault(a, new ArrayList<>());
        for (int idx : graphA) {
            t1 = Math.min(t1, dp[idx]);
        }

        long t2 = INF;
        List<Integer> graphC = graph.getOrDefault(c, new ArrayList<>());
        for (int idx : graphC) {
            t2 = Math.min(t2, dp[idx]);
        }
        if (t1 == INF || t2 == INF) {
            System.out.println(-1);
        } else {
            System.out.println(t1 + t2 + 1);
        }
    }
}
