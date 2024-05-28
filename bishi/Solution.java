import java.util.ArrayList;
import java.util.List;

class Solution {
    List<Integer> nums;
    List<List<Integer>> res;

    void swap(int a, int b) {
        int tmp = nums.get(a);
        nums.set(a, nums.get(b));
        nums.set(b, tmp);
    }

    void dfs(int x) {
        if (x == nums.size() - 1) {
            res.add(new ArrayList<>(nums)); // 添加排列方案
            return;
        }
        for (int i = x; i < nums.size(); i++) {
            swap(i, x); // 交换，将 nums[i] 固定在第 x 位
            dfs(x + 1); // 开启固定第 x + 1 位元素
            swap(i, x); // 恢复交换
        }
    }

    public List<List<Integer>> permute(int[] nums) {
        this.res = new ArrayList<>();
        this.nums = new ArrayList<>();
        for (int num : nums) {
            this.nums.add(num);
        }
        dfs(0);
        return res;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] input = { 1, 2, 3 }; // 输入数组
        List<List<Integer>> permutations = solution.permute(input);

        // 打印输出所有排列
        for (List<Integer> perm : permutations) {
            System.out.println(perm);
        }
    }
}
