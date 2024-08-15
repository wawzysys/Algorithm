
// 最长的指定瑕疵度的元音子串
import java.util.*;

public class C {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int target = sc.nextInt();
    String s = sc.next();

    System.out.println(f(target, s));
  }

  public static int f(int target, String s) {
    char[] yuan = { 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' };
    HashSet<Character> set = new HashSet<>();
    for (char c : yuan)
      set.add(c);

    ArrayList<Integer> idxs = new ArrayList<>();
    for (int i = 0; i < s.length(); i++) {
      if (set.contains(s.charAt(i)))
        idxs.add(i);
    }

    int ans = 0;
    int n = idxs.size();

    int l = 0;
    int r = 0;

    while (r < n) {
      // 瑕疵度计算
      int diff = idxs.get(r) - idxs.get(l) - (r - l);

      if (diff > target) {
        l++;
      } else if (diff < target) {
        r++;
      } else {
        ans = Math.max(ans, idxs.get(r) - idxs.get(l) + 1);
        r++;
      }
    }

    return ans;
  }
}