package org.example;

import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T=in.nextInt();
        while (T-- > 0){
            int N= in.nextInt();
            int n = in.nextInt();
            int c = in.nextInt();
            int[] a = new int[n];
            for(int i=0;i<n;i++){
                a[i] = in.nextInt();
            }
            boolean[] dp = new boolean[N+1];
            dp[0]=true;
            for (int i = 0; i < n; i++) {
                for (int j = N; j >= a[i] ; j--) {
                    if(dp[j-a[i]]){
                        dp[j]=true;
                    }
                }
            }
            String ans ="No";
            for (int k=0;k<=N;k++){
                if(dp[k]){
                    int gap = N-k;
                    if(gap >= 0 && gap<=c){
                        ans = "YES";
                        break;
                    }
                }
            }
            System.out.println(ans);
        }
    }
}