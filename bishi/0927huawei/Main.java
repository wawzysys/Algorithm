import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        s.nextLine();
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
            String line = s.nextLine();
            if (!line.isEmpty()) {
                String[] parts = line.trim().split("\\s+");
                for (String part : parts) {
                    int neighbor = Integer.parseInt(part);
                    adj[i].add(neighbor);
                }
            }
            Collections.sort(adj[i]);
        }
        int[] color = new int[n];
        Arrays.fill(color, -1);
        boolean possible = true;
        for (int i = 0; i < n && possible; i++) {
            if (color[i] == -1) {
                Queue<Integer> q = new LinkedList<>();
                color[i] = 0;
                q.offer(i);
                while (!q.isEmpty() && possible) {
                    int u = q.poll();
                    for (int v : adj[u]) {
                        if (color[v] == -1) {
                            color[v] = 1 - color[u];
                            q.offer(v);
                        } else if (color[v] == color[u]) {
                            possible = false;
                            break;
                        }
                    }
                }
            }
        }
        if (!possible) {
            System.out.println("-1");
        } else {
            List<Integer> group0 = new ArrayList<>();
            List<Integer> group1 = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (color[i] == 0) {
                    group0.add(i);
                } else {
                    group1.add(i);
                }
            }
            Collections.sort(group0);
            Collections.sort(group1);
            printList(group0);
            printList(group1);
        }
    }
    static void printList(List<Integer> list) {
        if (list.isEmpty()) {
            System.out.println();
            return;
        }
        StringBuilder sb = new StringBuilder();
        for (int num : list) {
            sb.append(num).append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}
