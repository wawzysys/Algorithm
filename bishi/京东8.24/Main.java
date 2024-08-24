
// TreeMap ģ�� SortedList �Ĺ��ܣ�ʵ����һ������ļ��ϣ����Է�����ҵ���Сֵ�����ֵ����һ��ֵ����һ��ֵ�ȿ����ظ���
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
        int[] maxRange = { 0, 0 }; // ��¼��������ʼ�ͽ���λ��

        for (int end = 1; end < n; end++) {
            addElement(numSet, arr[end]);

            // �����ǰ���䲻��������������������
            while (!isValid(numSet)) {
                removeElement(numSet, arr[start]);
                start++;
            }

            // ���������
            if (end - start > maxRange[1] - maxRange[0]) {
                maxRange[0] = start;
                maxRange[1] = end;
            }
        }

        // �������������������1��ʼ
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
