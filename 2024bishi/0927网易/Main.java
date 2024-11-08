import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {

    static class Item {
        long profit;
        long maxSell;

        public Item(long profit, long maxSell) {
            this.profit = profit;
            this.maxSell = maxSell;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        long k = sc.nextLong();

        long[] a = new long[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextLong();
        }

        long[] b = new long[n];
        for (int i = 0; i < n; i++) {
            b[i] = sc.nextLong();
        }

        long[] c = new long[n];
        for (int i = 0; i < n; i++) {
            c[i] = sc.nextLong();
        }

        Item[] items = new Item[n];
        for (int i = 0; i < n; i++) {
            long profit = b[i] - a[i];
            items[i] = new Item(profit, c[i]);
        }

        Arrays.sort(items, new Comparator<Item>() {
            @Override
            public int compare(Item o1, Item o2) {

                return Long.compare(o2.profit, o1.profit);
            }
        });

        long totalProfit = 0;
        long remaining = k;

        for (int i = 0; i < n; i++) {
            if (remaining == 0) {
                break;
            }
            if (items[i].profit <= 0) {
                continue;
            }
            long sellCount = Math.min(items[i].maxSell, remaining);
            totalProfit += sellCount * items[i].profit;
            remaining -= sellCount;
        }
        System.out.println(totalProfit);
    }
}
