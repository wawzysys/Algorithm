import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main2 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
    
        String input = sc.nextLine();
        sc.close();
        

        String[] flights = input.split(",");
        

        Arrays.sort(flights, new Comparator<String>() {
            @Override
            public int compare(String flight1, String flight2) {
                int compareFirstPart = flight1.substring(0, 2).compareTo(flight2.substring(0, 2));
                if (compareFirstPart != 0) {
                    return compareFirstPart;
                }
                return flight1.substring(2).compareTo(flight2.substring(2));
            }
        });
        System.out.println(String.join(",", flights));
    }
}
