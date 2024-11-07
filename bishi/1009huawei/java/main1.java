import java.util.*;

public class main1 {
    // 定义节点类，用于存储坐标和当前距离
    static class Node {
        int x, y, d;

        Node(int x, int y, int d) {
            this.x = x;
            this.y = y;
            this.d = d;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 读取矩阵的宽度和高度
        int m = sc.nextInt();
        int n = sc.nextInt();

        // 读取起点（机房）坐标
        int a1 = sc.nextInt();
        int a2 = sc.nextInt();

        // 读取终点（小区）坐标
        int b1 = sc.nextInt();
        int b2 = sc.nextInt();

        // 读取不允许经过的节点数量
        int k = sc.nextInt();
        boolean[][] blocked = new boolean[m][n];

        // 标记所有不允许经过的节点
        for (int i = 0; i < k; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            if (x >= 0 && x < m && y >= 0 && y < n) {
                blocked[x][y] = true;
            }
        }

        // 如果起点和终点相同，最短距离为0
        if (a1 == b1 && a2 == b2) {
            System.out.println(0);
            return;
        }

        // 检查起点和终点是否在有效范围内且未被阻塞
        if (a1 < 0 || a1 >= m || a2 < 0 || a2 >= n || b1 < 0 || b1 >= m || b2 < 0 || b2 >= n || blocked[a1][a2]
                || blocked[b1][b2]) {
            System.out.println(-1);
            return;
        }

        // 初始化访问数组，记录已访问的节点
        boolean[][] visited = new boolean[m][n];
        Queue<Node> q = new LinkedList<>();

        // 将起点加入队列并标记为已访问
        q.add(new Node(a1, a2, 0));
        visited[a1][a2] = true;

        // 定义四个可能的移动方向：上下左右
        int[][] dirs = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };

        // 开始广度优先搜索
        while (!q.isEmpty()) {
            Node current = q.poll();

            // 如果当前节点是终点，输出距离并结束
            if (current.x == b1 && current.y == b2) {
                System.out.println(current.d);
                return;
            }

            // 遍历所有可能的移动方向
            for (int[] dir : dirs) {
                int nx = current.x + dir[0];
                int ny = current.y + dir[1];

                // 检查新位置是否在有效范围内、未被阻塞且未被访问
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && !blocked[nx][ny] && !visited[nx][ny]) {
                    visited[nx][ny] = true; // 标记为已访问
                    q.add(new Node(nx, ny, current.d + 1)); // 将新节点加入队列，距离加1
                }
            }
        }

        // 如果无法到达终点，输出-1
        System.out.println(-1);
    }
}
