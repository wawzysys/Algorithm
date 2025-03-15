import java.util.*;

public class kama {
    static Map<Integer, Integer> map = new HashMap();

    public static void main(String[] args) {
        int n = 5;
        int[][] relations = {
                { 1, 3 },
                { 2, 4 },
                { 3, 5 },
                { 4, 6 },
                { 5, 6 }
        };
        for (int i = 0; i < n; i++) {
            int a = relations[i][0];
            int b = relations[i][1];
            map.put(a, b);
        }
        int xiaoming = 1;
        int count1 = 0;
        while (map.containsKey(xiaoming)) {
            xiaoming = map.get(xiaoming);
            count1++;
        }

        int xiaoyu = 2;
        int count2 = 0;
        while (map.containsKey(xiaoyu)) {
            xiaoyu = map.get(xiaoyu);
            count2++;
        }

        if (count1 < count2) {
            System.out.println("You are my younger");
        } else if (count1 > count2) {
            System.out.println("You are my elder");
        } else {
            System.out.println("You are my brother");
        }
    }
}