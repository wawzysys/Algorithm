import java.util.*;
import java.io.*;

public class Main {
    static class Edge {
        int to, rev;
        long cap;

        Edge(int to, int rev, long cap) {
            this.to = to;
            this.rev = rev;
            this.cap = cap;
        }
    }

    static class MaxFlow {
        int n;
        ArrayList<Edge>[] graph;
        int[] level;
        int[] ptr;

        MaxFlow(int size) {
            n = size;
            graph = new ArrayList[n + 1];
            for (int i = 0; i <= n; i++)
                graph[i] = new ArrayList<>();
            level = new int[n + 1];
            ptr = new int[n + 1];
        }

        void addEdge(int from, int to, long cap) {
            graph[from].add(new Edge(to, graph[to].size(), cap));
            graph[to].add(new Edge(from, graph[from].size() - 1, 0));
        }

        boolean bfs(int s, int t) {
            Arrays.fill(level, -1);
            Queue<Integer> q = new LinkedList<>();
            q.add(s);
            level[s] = 0;
            while (!q.isEmpty()) {
                int u = q.poll();
                for (Edge e : graph[u]) {
                    if (e.cap > 0 && level[e.to] == -1) {
                        level[e.to] = level[u] + 1;
                        q.add(e.to);
                        if (e.to == t)
                            return true;
                    }
                }
            }
            return false;
        }

        long dfs(int u, int t, long flow) {
            if (u == t)
                return flow;
            for (; ptr[u] < graph[u].size(); ptr[u]++) {
                Edge e = graph[u].get(ptr[u]);
                if (e.cap > 0 && level[e.to] == level[u] + 1) {
                    long pushed = dfs(e.to, t, Math.min(flow, e.cap));
                    if (pushed > 0) {
                        e.cap -= pushed;
                        graph[e.to].get(e.rev).cap += pushed;
                        return pushed;
                    }
                }
            }
            return 0;
        }

        long maxFlow(int s, int t) {
            long flow = 0;
            while (bfs(s, t)) {
                Arrays.fill(ptr, 0);
                while (true) {
                    long pushed = dfs(s, t, Long.MAX_VALUE);
                    if (pushed == 0)
                        break;
                    flow += pushed;
                }
            }
            return flow;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] first = br.readLine().split(" ");
        int n = Integer.parseInt(first[0]);
        int m = Integer.parseInt(first[1]);
        MaxFlow mf = new MaxFlow(n);
        for (int i = 0; i < m; i++) {
            String[] parts = br.readLine().split(" ");
            int a = Integer.parseInt(parts[0]);
            int b = Integer.parseInt(parts[1]);
            long c = Long.parseLong(parts[2]);
            mf.addEdge(a, b, c);
        }
        System.out.println(mf.maxFlow(1, n));
    }
}
