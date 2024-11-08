import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] values = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
        }
        int res = minGroup(n, k, values);
        System.out.println(res);
    }

    private static int minGroup(int n, int k, int[] values) {
        Deque<Integer> maxDeque = new ArrayDeque<>();
        Deque<Integer> minDeque = new ArrayDeque<>();

        int groups = 0;
        int left = 0;

        for (int right = 0; right < n; right++) {
            while (!maxDeque.isEmpty() && values[right] > values[maxDeque.peekLast()]) {
                maxDeque.pollLast();
            }
            maxDeque.offerLast(right);

            while (!minDeque.isEmpty() && values[right] < values[minDeque.peekLast()]) {
                minDeque.pollLast();
            }
            minDeque.offerLast(right);

            if (values[maxDeque.peekFirst()] - values[minDeque.peekFirst()] > k) {
                groups++;
                left = right;

                maxDeque.clear();
                minDeque.clear();
                maxDeque.offerLast(right);
                minDeque.offerLast(right);
            }
        }

        if (left < n) {
            groups++;
        }

        return groups;
    }
}