package org.example.t2;

import java.util.Scanner;

public class Main {
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        while(T-- > 0){
            int n = in.nextInt();
            int[] a = new int[n];
            int[] b = new int[n];
            for(int i=0;i<n;i++){
                a[i] = in.nextInt();
            }
            for(int i=0;i<n;i++){
                b[i] = in.nextInt();
            }
            if (solve(a,b)){
                System.out.println("YES");
            }else{
                System.out.println("NO");
            }

        }
    }
    public static boolean solve(int[] a, int[] b){
        return canMakeSorted(a,b,1) || canMakeSorted(b,a,1) ||
                canMakeSorted(a,b,-1) || canMakeSorted(b,a,-1);
    }
    public static boolean canMakeSorted(int[] a, int[] b, int order){
        int n =a.length;
        int prev;
        if (order == 1){
            prev = Integer.MIN_VALUE;
            for (int i = 0; i < n; i++) {
                int val1 = a[i],val2 = b[i];
                boolean canPickVal1 = val1 >= prev;
                boolean canPickVal2 = val2 >= prev;
                if (!canPickVal1 && !canPickVal2){
                    return false;
                }
                if (canPickVal1 && canPickVal2){
                    prev = Math.min(val1,val2);
                } else if(canPickVal1){
                    prev = val1;
                } else{
                    prev = val2;
                }

            }
            return true;
        }else{
            prev = Integer.MAX_VALUE;
            for (int i = 0; i < n; i++) {
                int val1 = a[i],val2 = b[i];
                boolean canPickVal1 = val1 <= prev;
                boolean canPickVal2 = val2 <= prev;
                if (!canPickVal1 && !canPickVal2){
                    return false;
                }
                if (canPickVal1 && canPickVal2){
                    prev = Math.max(val1,val2);
                } else if(canPickVal1){
                    prev = val1;
                } else{
                    prev = val2;
                }

            }
            return true;
        }

    }

}
