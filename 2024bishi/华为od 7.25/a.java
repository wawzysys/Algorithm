import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;
import java.util.StringJoiner;

public class a {
    static class St {
        String na;
        int[] r;

        public St(String na, int[] r) {
            this.na = na;
            this.r = r;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int m = sc.nextInt();
        HashMap<String, Integer> d = new HashMap<>();
        for (int i = 0; i < m; i++) {
            d.put(sc.next(), i);
        }

        ArrayList<St> e = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String na = sc.next();
            int[] r = new int[m + 1];
            int ss = 0;
            for (int j = 0; j < m; j++) {
                r[j] = sc.nextInt();
                ss += r[j];
            }

            r[m] = ss;

            e.add(new St(na, r));
        }
        int idx = d.getOrDefault(sc.next(), m);

        e.sort(
                (a, b) -> a.r[idx] != b.r[idx]
                        ? b.r[idx] - a.r[idx]
                        : a.na.compareTo(b.na));

        StringJoiner sj = new StringJoiner(" ");
        for (St student : e) {
            sj.add(student.na);
        }

        System.out.println(sj);
    }
}