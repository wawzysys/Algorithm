import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int k = scanner.nextInt();
        scanner.nextLine(); // consume the rest of the line after reading integer
        String s = scanner.nextLine();

        HashMap<Character, List<int[]>> d = new HashMap<>();
        int last = 0;
        for (int i = 1; i < n; i++) {
            if (s.charAt(i) != s.charAt(i - 1)) {
                d.putIfAbsent(s.charAt(i - 1), new ArrayList<>());
                d.get(s.charAt(i - 1)).add(new int[] { last, i - 1 });
                last = i;
            }
        }
        // Adding the last sequence
        d.putIfAbsent(s.charAt(n - 1), new ArrayList<>());
        d.get(s.charAt(n - 1)).add(new int[] { last, n - 1 });

        int ans = Integer.MIN_VALUE;
        for (char c : d.keySet()) {
            int cur = 0;
            for (int[] range : d.get(c)) {
                cur += (range[1] - range[0] + 1) / k;
            }
            ans = Math.max(ans, cur);
        }

        System.out.println(ans);
        scanner.close();
    }
}
