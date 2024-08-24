import java.util.Scanner;
import java.util.StringTokenizer;

public class Test1 {

    public static int calculate(String input) {
        StringTokenizer numbers = new StringTokenizer(input, "+-", true);
        int result = 0;
        int sign = 1;

        while (numbers.hasMoreTokens()) {
            String token = numbers.nextToken();

            if (token.equals("+")) {
                sign = 1;
            } else if (token.equals("-")) {
                sign = -1;
            } else {
                result += sign * Integer.parseInt(token);
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        int result = calculate(input);
        System.out.println(result);

        sc.close();
    }
}
