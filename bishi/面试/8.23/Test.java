// 加减法输入String(只有数字、加减号)
// 例如:11+2+3-6
// 输出int 10

import java.util.Scanner;

public class Test {
    public static int calculate(String input) {
        int result = 0;
        int currentNumber = 0;
        int sign = 1;
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);

            if (Character.isDigit(c)) {
                currentNumber = currentNumber * 10 + (c - '0');
            } else if (c == '+') {
                result += sign * currentNumber;
                currentNumber = 0;
                sign = 1;
            } else if (c == '-') {
                result += sign * currentNumber;
                currentNumber = 0;
                sign = -1;
            }
        }
        result += sign * currentNumber;

        return result;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        sc.close();
        int result = calculate(input);
        System.out.println(result);
    }
}
