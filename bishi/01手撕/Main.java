import java.util.*;

public class Main {
    List<Integer> nums;
    List<List<Integer>> res;

    void swap(int a, int b) {
        int tmp = nums.get(a);
        nums.set(a, nums.get(b));
        nums.set(b, tmp);
    }

    void dfs(int x) {
        if (x == nums.size() - 1) {
            res.add(new ArrayList<>(nums)); // ??????
            return;
        }
        HashSet<Integer> set = new HashSet<>();
        for (int i = x; i < nums.size(); i++) {
            if (set.contains(nums.get(i)))
                continue; // ???????
            set.add(nums.get(i));
            swap(i, x); // ???? nums[i] ???? x ?
            dfs(x + 1); // ????? x + 1 ???
            swap(i, x); // ????
        }
    }

    public List<List<Integer>> permuteUnique(int[] nums) {
        this.res = new ArrayList<>();
        this.nums = new ArrayList<>();
        for (int num : nums) {
            this.nums.add(num);
        }
        dfs(0);
        return res;
    }

    public static void main(String[] args) {
        Main sol = new Main();
        int[] nums = { 1, 1, 2 };
        List<List<Integer>> results = sol.permuteUnique(nums);
        for (List<Integer> result : results) {
            System.out.println(result);
        }
    }
}
