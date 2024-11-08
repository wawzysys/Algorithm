import java.util.*;

public class Main1 {
    static class Task{
        int t,i;
        Task(int t,int i){
            this.t = t;
            this.i = i;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        PriorityQueue<Task> pq = new PriorityQueue<>((a,b)->{
            if(b.t != a.t) return b.t - a.t;
            return b.i - a.i;
        });
        for(int i = 0; i < m; i++){
            if(!sc.hasNextInt()) break;
            int ti = sc.nextInt();
            if(pq.size()<n){
                pq.offer(new Task(ti,i));
            }else{
                Task top = pq.peek();
                if(ti>top.t){
                    continue;
                }
                else{
                    pq.poll();
                    pq.offer(new Task(ti,i));
                }
            }
        }
        
        int max = -1;
        int ans = -1;
        for(Task t :pq){
            if(t.t>max){
                max=t.t;
                ans=t.i;
            }
            else if(t.t == max && t.i>ans){
                ans=t.i;
            }
        }
        System.out.println(ans);
   

    }
}
