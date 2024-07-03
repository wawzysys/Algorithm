import java.util.List;
import java.util.ArrayList;
import java.util.HashSet;

public class Main {

    public static List<Integer> getRecommendedFriends(int n, List<List<Integer>> friendships) {
        List<HashSet<Integer>> g = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            g.add(new HashSet<>());
        }
        for (List<Integer> pair : friendships) {
            int a = pair.get(0);
            int b = pair.get(1);
            g.get(a).add(b);
            g.get(b).add(a);
        }

        // 初始化推荐好友列表
        List<Integer> re = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            re.add(-1);  // 默认没有推荐
        }

        // 遍历每个用户以寻找推荐好友
        for (int cur = 0; cur < n; cur++) {
            HashSet<Integer> curUser = g.get(cur);
            int mmax = -1;
            int be = -1;

            // 检查所有其他用户作为潜在的推荐好友
            for (int i = 0; i < n; i++) {
                if (cur != i && !curUser.contains(i)) {
                    // 计算共同好友数量
                    HashSet<Integer> other = g.get(i);
                    int comm = 0;
                    for (Integer friend : curUser) {
                        if (other.contains(friend)) {
                            comm++;
                        }
                    }

                    // 更新最佳推荐
                    if (comm > mmax || (comm == mmax && i < be)) {
                        mmax = comm;
                        be = i;
                    }
                }
            }

            // 设置该用户的推荐好友
            if (mmax > 0) {  // 只有当有共同好友时才推荐
                re.set(cur, be);
            }
        }

        return re;
    }

    public static void main(String[] args) {
        // 示例输入
        int n = 3;
        List<List<Integer>> friendships = List.of(
            // List.of(0, 1), List.of(0, 2), List.of(1, 3),
            // List.of(2, 3), List.of(3, 4)
            List.of(0, 1), List.of(1, 2), List.of(2, 0)
        );

        // 获取并打印推荐结果
        List<Integer> result = getRecommendedFriends(n, friendships);
        System.out.println(result);
    }
}
