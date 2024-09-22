import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line1;
        while ((line1 = br.readLine()) != null) {
            line1 = line1.trim();
            if (line1.isEmpty()) {
                continue;
            }
            String line2 = br.readLine();
            if (line2 == null) {
                break;
            }
            line2 = line2.trim();
            int[] seqA = parseLine(line1);
            int[] seqB = parseLine(line2);
            int lcsLength = computeLCS(seqA, seqB);
            System.out.println(lcsLength);
        }
    }

    private static int[] parseLine(String line) {
        if (line.isEmpty()) {
            return new int[0];
        }
        String[] tokens = line.split("\\s+");
        int[] seq = new int[tokens.length];
        for (int i = 0; i < tokens.length; i++) {
            seq[i] = Integer.parseInt(tokens[i]);
        }
        return seq;
    }

    private static int computeLCS(int[] A, int[] B) {
        int n = A.length;
        int m = B.length;
        int[] previous = new int[m + 1];
        int[] current = new int[m + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (A[i - 1] == B[j - 1]) {
                    current[j] = previous[j - 1] + 1;
                } else {
                    current[j] = Math.max(previous[j], current[j - 1]);
                }
            }
            int[] temp = previous;
            previous = current;
            current = temp;
        }
        return previous[m];
    }
}
