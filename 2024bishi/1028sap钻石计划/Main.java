import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (scanner.hasNextInt()) {
            int n = scanner.nextInt();  
            int m = scanner.nextInt();  

            double sum = 0.0;           
            double current = n;        


            for (int i = 0; i < m; i++) {
                sum += current;
                current = Math.sqrt(current);  
            }
            System.out.printf("%.2f%n", sum);
        }

        scanner.close();  
    }
}
