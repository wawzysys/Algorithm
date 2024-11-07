import java.util.*;
import java.io.*;

public class Main3 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        String[] s1 = br.readLine().trim().split(" ");
        String[] s2 = br.readLine().trim().split(" "); 
        if(s1.length != n || s2.length != n){
            System.out.println(-1);
            return;
        }
        List<Integer> S = new ArrayList<>();
        long sum = 0;
        Map<Integer, Integer> cnt = new HashMap<>();
        for(int i=0;i<n;i++){
            int n1 = Integer.parseInt(s1[i]);
            int n2 = Integer.parseInt(s2[i]);
            if(n1 == n2){
                S.add(i);
                sum += i;
                cnt.put(n1, cnt.getOrDefault(n1, 0) +1);
            }
        }
        
        int l = S.size();
        if(l ==0){
            System.out.println(0);
            return;
        }
        if(l %2 !=0){
            System.out.println(-1);
            return;
        }
        boolean p = true;
        for(Map.Entry<Integer, Integer> entry: cnt.entrySet()){
            if(entry.getValue() > l /2){
                p = false;
                break;
            }
        }
        if(p){
            System.out.println(sum);
        }
        else{
            System.out.println(-1);
        }
    }
}
