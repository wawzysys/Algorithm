
// TreeMap 模仿 SortedList 的功能，实现了一个有序的集合，可以方便地找到最小值、最大值、下一个值、上一个值等可以重复。
import java.util.Scanner;
import java.util.TreeMap;

public class Main {
    public static boolean isValid(TreeMap<Integer, Integer> numSet) {
        int smallest = numSet.firstKey();
        int secondSmallest = numSet.higherKey(smallest);
        if (numSet.get(smallest) >= 2) {
            secondSmallest = smallest;
        }
        int largest = numSet.lastKey();
        return smallest + secondSmallest > largest;
    }

    public static void solve() {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        scanner.close();
        TreeMap<Integer, Integer> numSet = new TreeMap<>();
        addElement(numSet, arr[0]);

        int start = 0;
        int[] maxRange = { 0, 0 }; // 记录最长区间的起始和结束位置

        for (int end = 1; end < n; end++) {
            addElement(numSet, arr[end]);

            // 如果当前区间不满足条件，则收缩区间
            while (!isValid(numSet)) {
                removeElement(numSet, arr[start]);
                start++;
            }

            // 更新最长区间
            if (end - start > maxRange[1] - maxRange[0]) {
                maxRange[0] = start;
                maxRange[1] = end;
            }
        }

        // 输出结果，区间的索引从1开始
        System.out.println((maxRange[0] + 1) + " " + (maxRange[1] + 1));
    }

    public static void addElement(TreeMap<Integer, Integer> map, int key) {
        map.put(key, map.getOrDefault(key, 0) + 1);
    }

    public static void removeElement(TreeMap<Integer, Integer> map, int key) {
        if (map.containsKey(key)) {
            if (map.get(key) > 1) {
                map.put(key, map.get(key) - 1);
            } else {
                map.remove(key);
            }
        }
    }

    public static void main(String[] args) {
        solve();
    }
}
