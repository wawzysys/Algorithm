import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = scanner.nextInt();
        }
        int ans = 0;
        int m = scanner.nextInt();
        int[] cnt = new int[m]; // 数组模拟 Map
        
        for (int c : nums) {
            int modValue = c % m;
            cnt[modValue]++;
            ans = Math.max(ans, cnt[modValue]);
        }
        
        Arrays.sort(nums);
    
        for (int c : nums) {
            if (cnt[c % m] == ans) {
                System.out.println(c);
                break;
            }
        }
        
        scanner.close();
    }
}