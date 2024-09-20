import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class VersionComparator implements Comparator<String> {
    @Override
    public int compare(String version1, String version2) {
        String[] levels1 = version1.split("\\.");
        String[] levels2 = version2.split("\\.");

        int length = Math.max(levels1.length, levels2.length);
        for (int i = 0; i < length; i++) {
            Integer v1 = i < levels1.length ? Integer.parseInt(levels1[i]) : 0;
            Integer v2 = i < levels2.length ? Integer.parseInt(levels2[i]) : 0;

            int compare = v1.compareTo(v2);
            if (compare != 0) {
                return compare;
            }
        }
        return 0;
    }
}

public class 1111 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine(); 

        String[] versions = new String[n];
        for (int i = 0; i < n; i++) {
            versions[i] = scanner.nextLine();
        }
        Arrays.sort(versions, new VersionComparator());
        for (String version : versions) {
            System.out.println(version);
        }
    }
}
