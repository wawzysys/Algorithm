import java.util.Scanner;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] nums = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] pos = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int x = pos[0];
        int y = pos[1];

        int result = getResult(nums, x, y);
        System.out.println(result);
    }

    public static int getResult(int[] nums, int x, int y) {
        int rows = nums[0];
        int cols = nums[1];

        int[] graph = new int[rows * cols];
        Arrays.fill(graph, -1);

        int start = 0;
        for (int i = 2; i < nums.length; i += 2) {
            int gray = nums[i];
            int length = nums[i + 1];

            Arrays.fill(graph, start, start + length, gray);
            start += length;
        }

        return graph[x * cols + y];
    }
}
