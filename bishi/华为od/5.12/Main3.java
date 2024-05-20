import java.util.Scanner;;

public class Main3 {
    public static boolean check(int speed, int limit, int[] cnts, int csize) {
        int cost = 0;
        for (int i = 0; i < csize; i++) {
            int cnt = cnts[i];
            cost += cnt / speed + (cnt % speed > 0 ? 1 : 0);
            if (cost > limit) {
                return false;
            }
        }
        return true;
    }

    public static int getResult(int[] cnts, int csize, int h) {
        if (csize > h) {
            return 0;
        }
        int maxSpeed = Integer.MIN_VALUE;
        for (int i = 0; i < csize; i++) {
            maxSpeed = Math.max(maxSpeed, cnts[i]);
        }
        if (csize == h) {
            return maxSpeed;
        }
        int minSpeed = 1;
        int ans = maxSpeed;
        while (minSpeed <= maxSpeed) {
            int mid = (minSpeed + maxSpeed) >> 1;

            if (check(mid, h, cnts, csize)) {
                ans = mid;
                maxSpeed = mid - 1;
            } else {
                minSpeed = mid + 1;
            }
        }

        return ans;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] cnts = new int[10000];
        int csize = 0;

        String line = sc.nextLine();
        String[] tokens = line.split(" ");
        for (String token : tokens) {
            cnts[csize++] = Integer.parseInt(token);
        }
        int h = sc.nextInt();
        System.out.println(getResult(cnts, csize, h));
    }
}
