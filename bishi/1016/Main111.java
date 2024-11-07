import java.util.*;
public class Main{
    static class Task{
        int t, i;
        Task(int t, int i){this.t=t; this.i=i;}
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int m=sc.nextInt();
        PriorityQueue<Task> pq=new PriorityQueue<>((a,b)->{
            if(b.t !=a.t) return b.t -a.t;
            return a.i -b.i;
        });
        for(int i=0;i<m;i++){
            if(!sc.hasNextInt()) break;
            int ti=sc.nextInt();
            if(pq.size()<n){
                pq.offer(new Task(ti,i));
            }
            else{
                Task top=pq.peek();
                if(ti > top.t){
                    continue;
                }
                else{
                    pq.poll();
                    pq.offer(new Task(ti,i));
                }
            }
        }
        int maxT=-1, res=-1;
        for(Task t:pq){
            if(t.t > maxT){
                maxT = t.t;
                res = t.i;
            }
            else if(t.t == maxT && t.i > res){
                res = t.i;
            }
        }
        System.out.println(res);
    }
}
