import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); 
        sc.nextLine(); 
        String[] s = new String[100011]; 
        String[] inputs = sc.nextLine().split(" ");
        int top = 0;
        for (int i = 0; i < n; i++) {
            String c = inputs[i];
            if (top >= 2 && s[top].equals(c) && s[top - 1].equals(c)) {
                top -= 2;
            } else {
                s[++top] = c;
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
