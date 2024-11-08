import java.util.Arrays;
import java.util.Scanner;
import java.util.StringJoiner;

public class b {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int[] nums = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    System.out.println(f(nums));
  }

  public static String f(int[] nums) {
    StringJoiner sj = new StringJoiner(" ");
    int px = nums[0];
    int py = nums[1];
    int pdx = 0;
    int pdy = 0;

    for (int i = 2; i < nums.length; i += 2) {
      int cx = nums[i];
      int cy = nums[i + 1];

      int fx = cx - px;
      int fy = cy - py;
      int base = Math.max(Math.abs(fx), Math.abs(fy));
      int dx = fx / base;
      int dy = fy / base;
      if (dx != pdx || dy != pdy) {
        sj.add(px + " " + py);
      }
      px = cx;
      py = cy;
      pdx = dx;
      pdy = dy;
    }
    sj.add(px + " " + py);
    return sj.toString();
  }
}