import java.util.*;

class 1111mian {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        // 新建及其初始化，第一次把房间0的钥匙存入队列，另外需要判断每个房间是否开启的数组
        int[] fj = new int[rooms.size()];
        fj[0] = 1; // 房间0默认开启
        Queue<Integer> queue = new LinkedList<>();
        List<Integer> top = rooms.get(0);
        for (Integer a : top) {
            queue.offer(a);
        }

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; ++i) {
                int roo = queue.poll();
                if (fj[roo] == 0) {
                    fj[roo] = 1;
                    List<Integer> cur = rooms.get(roo);
                    for (Integer a : cur) {
                        queue.offer(a);
                    }
                }
            }
        }

        // 检查是否所有房间都被开启
        for (int k = 0; k < fj.length; ++k) {
            if (fj[k] == 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 测试用例1
        List<List<Integer>> rooms1 = new ArrayList<>();
        rooms1.add(Arrays.asList(1, 3));
        rooms1.add(Arrays.asList(3, 0, 1));
        rooms1.add(Arrays.asList(2));
        rooms1.add(Arrays.asList(0));
        System.out.println(solution.canVisitAllRooms(rooms1)); // 输出: false

        // 测试用例2
        List<List<Integer>> rooms2 = new ArrayList<>();
        rooms2.add(Arrays.asList(1));
        rooms2.add(Arrays.asList(2));
        rooms2.add(Arrays.asList(3));
        rooms2.add(Arrays.asList());
        System.out.println(solution.canVisitAllRooms(rooms2)); // 输出: true

        // 测试用例3
        List<List<Integer>> rooms3 = new ArrayList<>();
        rooms3.add(Arrays.asList(1, 2));
        rooms3.add(Arrays.asList(2));
        rooms3.add(Arrays.asList(3));
        rooms3.add(Arrays.asList());
        System.out.println(solution.canVisitAllRooms(rooms3)); // 输出: true
    }
}