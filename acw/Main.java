import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        String[] s = new String[100011];
        int top = 0;
        String input = sc.nextLine();
        String[] inputs = input.split(" ");

        for (int i = 0; i < n; i++) {
            String c = inputs[i];// 你好
            s[++top] = c;
            while (top >= 3) {
                if (s[top - 1].equals(s[top]) && s[top - 2].equals(s[top - 1])) {
                    top -= 3;
                } else {
                    break;
                }
            }
        }

        if (top == 0) {
            System.out.println(0);
        } else {
            for (int i = 1; i < top; i++) {
                System.out.print(s[i] + " ");
            }
            System.out.print(s[top]);
        }
        sc.close();
    }
}
