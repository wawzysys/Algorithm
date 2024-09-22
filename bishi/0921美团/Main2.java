import java.util.Scanner;

public class Main2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] ai = new int[n]; 
        long[] bi = new long[n]; 
        long[] ci = new long[n]; 
        long ciSum = 0; 


        for (int i = 0; i < n; i++) {
            ai[i] = sc.nextInt();
        }


        for (int i = 0; i < n; i++) {
            bi[i] = sc.nextLong();
        }


        for (int i = 0; i < n; i++) {
            ci[i] = sc.nextLong();
            ciSum += ci[i];
        }

        long[] maxGain = new long[m + 1]; 
        for (int i = 1; i <= m; i++) {
            maxGain[i] = Long.MIN_VALUE;
        }


        for (int i = 0; i < n; i++) {
            long gain = bi[i] - ci[i];
            int label = ai[i];
            if (gain > maxGain[label]) {
                maxGain[label] = gain;
            }
        }

        long totalGain = 0;
        for (int i = 1; i <= m; i++) {
            if (maxGain[i] > 0) {
                totalGain += maxGain[i];
            }
        }

        long totalBeauty = ciSum + totalGain;

        System.out.println(totalBeauty);

        sc.close();
    }
}
