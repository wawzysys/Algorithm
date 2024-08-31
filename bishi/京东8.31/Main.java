import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine().strip();
        System.out.println(solve(s));
        scanner.close();
    }

    public static String solve(String s) {
        char[] sArray = s.toCharArray();
        int n = sArray.length;

        int i = n - 1;
        while (i >= 0 && sArray[i] == 'z') {
            i--;
        }

        if (i == -1) {
            return "-1";
        }

        sArray[i] = (char) (sArray[i] + 1);
        for (int j = i + 1; j < n; j++) {
            sArray[j] = 'a';
        }
        return new String(sArray);
    }
}