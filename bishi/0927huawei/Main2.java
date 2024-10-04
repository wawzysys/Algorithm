import java.util.*;

public class Main2 {
    static class Node {
        int x, y, danger;

        Node(int x, int y, int danger) {
            this.x = x;
            this.y = y;
            this.danger = danger;
        }
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int M = s.nextInt(), N = s.nextInt();
        int a1 = s.nextInt(), a2 = s.nextInt();
        int b1 = s.nextInt(), b2 = s.nextInt();
        int[][] g = new int[M][N];
        int[][] d = new int[M][N];
        List<int[]> inf = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                g[i][j] = s.nextInt();
                if (g[i][j] == 2 || g[i][j] == 3) {
                    d[i][j] = 0;
                    inf.add(new int[]{i, j});
                } else {
                    d[i][j] = -1;
                }
            }
        }
        int day = 0;
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        while (!inf.isEmpty()) {
            day++;
            int[][] D = new int[M][N];
            for (int[] row : D) Arrays.fill(row, 0);
            PriorityQueue<Node> q = new PriorityQueue<>((n1, n2) -> n2.danger - n1.danger);
            for (int[] p : inf) {
                int x = p[0], y = p[1];
                int danger = (g[x][y] == 2) ? a2 : a1;
                q.offer(new Node(x, y, danger));
                D[x][y] = danger;
            }
            while (!q.isEmpty()) {
                Node n = q.poll();
                int x = n.x, y = n.y, danger = n.danger;
                for (int k = 0; k < 4; k++) {
                    int nx = x + dx[k], ny = y + dy[k];
                    if (nx >= 0 && nx < M && ny >= 0 && ny < N && g[nx][ny] != 1) {
                        int nd = danger - 1;
                        if (nd > 0 && D[nx][ny] < nd) {
                            D[nx][ny] = nd;
                            q.offer(new Node(nx, ny, nd));
                        }
                    }
                }
            }
            List<int[]> newInf = new ArrayList<>();
            for (int i = 0; i < M; i++) {
                for (int j = 0; j < N; j++) {
                    if ((g[i][j] == 4 || g[i][j] == 5) && d[i][j] == -1) {
                        int th = (g[i][j] == 4) ? b2 : b1;
                        if (D[i][j] >= th) {
                            d[i][j] = day;
                            newInf.add(new int[]{i, j});
                        }
                    }
                }
            }
            for (int[] p : newInf) {
                int x = p[0], y = p[1];
                if (g[x][y] == 4) g[x][y] = 2;
                else if (g[x][y] == 5) g[x][y] = 3;
            }
            inf = newInf;
        }
        for (int i = 0; i < M; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < N; j++) {
                int res;
                if (g[i][j] == 0 || g[i][j] == 1) res = -1;
                else res = d[i][j];
                sb.append(res).append(j == N - 1 ? "" : " ");
            }
            System.out.println(sb.toString());
        }
    }
}
