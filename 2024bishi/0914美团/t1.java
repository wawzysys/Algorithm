import java.util.Scanner;

public class t1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        int n = s.length();
        int[] component = new int[n];
        int comp_id = 0;

        int[] positions = { -1, -1, -1 };
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == 'R' || c == 'B' || c == 'G') {
                positions["RBG".indexOf(c)] = i;
            }
            if (c == '#') {
                component[i] = -1;
            } else {
                if (i > 0 && component[i - 1] != -1) {
                    component[i] = component[i - 1];
                } else {
                    component[i] = comp_id++;
                }
            }
        }

        StringBuilder results = new StringBuilder();
        String[] seekers = { "R", "B", "G" };
        for (String seeker : seekers) {
            int a = "RBG".indexOf(seeker);
            int b = positions[a];
            int c = component[b];
            int minTime = Integer.MAX_VALUE;
            boolean found = false;
            for (int i = 0; i < positions.length; i++) {
                if (i != a) {
                    int hide = positions[i];
                    if (hide != -1 && component[hide] == c) {
                        int time = Math.abs(b - hide);
                        if (time < minTime) {
                            minTime = time;
                            found = true;
                        }
                    }
                }
            }
            if (found) {
                results.append(minTime).append(" ");
            } else {
                results.append("-1 ");
            }
        }

        System.out.println(results.toString().trim());
        scanner.close();
    }
}
