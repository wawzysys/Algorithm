import java.util.HashMap;

public class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        hashMap.put(0, -1);
        int sum = 0;
        int res = 0;
        for (int i = 0; i < nums.length; ++i) {
            sum += nums[i];
            if (hashMap.containsKey(sum - k)) {
                res = Math.max(res, i - hashMap.get(sum - k));
            }
            if (!hashMap.containsKey(sum)) {
                hashMap.put(sum, i);
            }
        }

        return res;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] nums1 = { 1, -1, 5, -2, 3 };
        int k1 = 3;
        System.out.println("输出: " + solution.maxSubArrayLen(nums1, k1)); // 输出: 4

        int[] nums2 = { -2, -1, 2, 1 };
        int k2 = 1;
        System.out.println("输出: " + solution.maxSubArrayLen(nums2, k2)); // 输出: 2
    }
}
