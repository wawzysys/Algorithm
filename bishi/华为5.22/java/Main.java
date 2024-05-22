import java.util.*;
import java.io.*;

public class Main {
    public static List<Integer> parseInput(String input) {
        List<Integer> list = new ArrayList<>();
        String[] tokens = input.split(" ");
        for (String token : tokens) {
            list.add(Integer.parseInt(token));
        }
        return list;
    }

    public static String solve(List<Integer> list1, List<Integer> list2) {
        int len1 = list1.size();
        int len2 = list2.size();
        int maxLen = 0;
        int endIdx1 = -1;

        for (int i = 0; i < len1; ++i) {
            for (int j = 0; j < len2; ++j) {
                int k = 0;
                while (i + k < len1 && j + k < len2 && list1.get(i + k).equals(list2.get(j + k))) {
                    ++k;
                }
                if (k > maxLen) {
                    maxLen = k;
                    endIdx1 = i + k - 1;
                }
            }
        }

        if (maxLen == 0) {
            return "-1";
        } else {
            StringBuilder result = new StringBuilder();
            for (int i = endIdx1 - maxLen + 1; i <= endIdx1; ++i) {
                if (result.length() > 0) {
                    result.append(" ");
                }
                result.append(list1.get(i));
            }
            return result.toString();
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String input1 = reader.readLine();
        String input2 = reader.readLine();

        List<Integer> list1 = parseInput(input1);
        List<Integer> list2 = parseInput(input2);

        String result = solve(list1, list2);
        System.out.println(result);
    }
}
