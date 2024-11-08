import java.util.*;

public class Main2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine());
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(scanner.nextLine());
        }
        int[] nums2 = nums.clone();
        Arrays.sort(nums2);

        Map<Integer, Integer> dic = new HashMap<>();
        for (int i = 0; i < n; i++) {
            dic.put(nums2[i], i);
        }

        int s = 0;
        for (int i = 0; i < n; i++) {
            if (i % 2 != dic.get(nums[i]) % 2) {
                s += 1;
            }
        }
        System.out.println(s / 2);
    }
}