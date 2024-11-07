import java.util.*;

public class Main {
    static class Node {
        int x;
        int y;
        int dist;

        Node(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        int a1 = sc.nextInt();
        int a2 = sc.nextInt();
        int b1 = sc.nextInt();
        int b2 = sc.nextInt();
        int k = sc.nextInt();
        Set<String> blocked = new HashSet<>();
        for (int i = 0; i < k; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            blocked.add(x + "," + y);
        }
        if (a1 == b1 && a2 == b2) {
            System.out.println(0);
            return;
        }
        if (blocked.contains(a1 + "," + a2) || blocked.contains(b1 + "," + b2)) {
            System.out.println(-1);
            return;
        }
        boolean[][] visited = new boolean[m][n];
        visited[a1][a2] = true;
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(a1, a2, 0));
        int[][] directions = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };
        while (!queue.isEmpty()) {
            Node current = queue.poll();
            if (current.x == b1 && current.y == b2) {
                System.out.println(current.dist);
                return;
            }
            for (int[] dir : directions) {
                int nx = current.x + dir[0];
                int ny = current.y + dir[1];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n &&
                        !visited[nx][ny] && !blocked.contains(nx + "," + ny)) {
                    visited[nx][ny] = true;
                    queue.add(new Node(nx, ny, current.dist + 1));
                }
            }
        }
        System.out.println(-1);
    }
}
