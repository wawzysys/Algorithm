import java.util.*;
import java.io.*;

public class Main3 {
    static class Edge {
        int to;
        int w;
        Edge(int to, int w) {
            this.to = to;
            this.w = w;
        }
    }

    static class Pair implements Comparable<Pair> {
        long cost;
        int node;
        Pair(long cost, int node) {
            this.cost = cost;
            this.node = node;
        }
        public int compareTo(Pair other) {
            return Long.compare(this.cost, other.cost);
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        int m = sc.nextInt();
        ArrayList<Long> points = new ArrayList<>();
        points.add(1L);
        points.add(n);
        long[][] tele = new long[m][2];
        for(int i=0;i<m;i++) {
            tele[i][0] = sc.nextLong();
            tele[i][1] = sc.nextLong();
            points.add(tele[i][0]);
            points.add(tele[i][1]);
        }
        Collections.sort(points);
        ArrayList<Long> lst = new ArrayList<>();
        lst.add(points.get(0));
        for(int i=1;i<points.size();i++) {
            if(!points.get(i).equals(points.get(i-1))) {
                lst.add(points.get(i));
            }
        }
        int size = lst.size();
        HashMap<Long, Integer> map = new HashMap<>();
        for(int i=0;i<size;i++) {
            map.put(lst.get(i), i);
        }
        ArrayList<ArrayList<Edge>> graph = new ArrayList<>();
        for(int i=0;i<size;i++) graph.add(new ArrayList<>());
        for(int i=0;i<size-1;i++) {
            long diff = lst.get(i+1) - lst.get(i);
            graph.get(i).add(new Edge(i+1, (int)diff));
            graph.get(i+1).add(new Edge(i, (int)diff));
        }
        for(int i=0;i<m;i++) {
            int u = map.get(tele[i][0]);
            int v = map.get(tele[i][1]);
            graph.get(u).add(new Edge(v, 0));
            graph.get(v).add(new Edge(u, 0));
        }
        long[] dist = new long[size];
        Arrays.fill(dist, Long.MAX_VALUE);
        int start = map.get(1L);
        int end = map.get(n);
        dist[start] = 0;
        PriorityQueue<Pair> pq = new PriorityQueue<>();
        pq.offer(new Pair(0, start));
        boolean[] visited = new boolean[size];
        while(!pq.isEmpty()) {
            Pair current = pq.poll();
            long cost = current.cost;
            int u = current.node;
            if(visited[u]) continue;
            visited[u] = true;
            if(u == end) {
                System.out.println(cost);
                return;
            }
            for(Edge edge : graph.get(u)) {
                int v = edge.to;
                long nc = cost + edge.w;
                if(nc < dist[v]) {
                    dist[v] = nc;
                    pq.offer(new Pair(nc, v));
                }
            }
        }
        System.out.println(-1);
    }
}
