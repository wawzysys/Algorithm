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
            res.add(new ArrayList<>(nums)); // ������з���
            return;
        }
        for (int i = x; i < nums.size(); i++) {
            swap(i, x); // �������� nums[i] �̶��ڵ� x λ
            dfs(x + 1); // �����̶��� x + 1 λԪ��
            swap(i, x); // �ָ�����
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
        int[] input = { 1, 2, 3 }; // ��������
        List<List<Integer>> permutations = solution.permute(input);

        // ��ӡ�����������
        for (List<Integer> perm : permutations) {
            System.out.println(perm);
        }
    }
}
