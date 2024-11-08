import java.util.*;
import java.io.*;

public class Main3 {
    static class Seal {
        long L, R, T, D;
        Seal(long L, long R, long T, long D){
            this.L = L;
            this.R = R;
            this.T = T;
            this.D = D;
        }
    }
    
    static class Event implements Comparable<Event>{
        long time;
        int idx;
        Event(long time, int idx){
            this.time = time;
            this.idx = idx;
        }
        public int compareTo(Event other){
            return Long.compare(this.time, other.time);
        }
    }
    
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Seal[] seals = new Seal[n];
        for(int i=0;i<n;i++) {
            long L = sc.nextLong();
            long R = sc.nextLong();
            long T = sc.nextLong();
            long D = sc.nextLong();
            seals[i] = new Seal(L, R, T, D);
        }
        Arrays.sort(seals, new Comparator<Seal>(){
            public int compare(Seal a, Seal b){
                if(a.L != b.L) return Long.compare(a.L, b.L);
                return Long.compare(a.R, b.R);
            }
        });
        PriorityQueue<Event> pq = new PriorityQueue<>();
        long s = 0;
        long t = 0;
        int p = 0;
        while(p < n && seals[p].L <= s && s <= seals[p].R){
            pq.offer(new Event(t + seals[p].T, p));
            p++;
        }
        while(!pq.isEmpty()){
            Event e = pq.poll();
            long ft = e.time;
            t = ft;
            long sumD = 0;
            sumD += seals[e.idx].D;
            while(!pq.isEmpty() && pq.peek().time == ft){
                sumD += seals[pq.poll().idx].D;
            }
            s += sumD;
            Iterator<Event> it = pq.iterator();
            while(it.hasNext()){
                Event ev = it.next();
                Seal seal = seals[ev.idx];
                if(!(seal.L <= s && s <= seal.R)){
                    it.remove();
                }
            }
            while(p < n && seals[p].L <= s && s <= seals[p].R){
                pq.offer(new Event(t + seals[p].T, p));
                p++;
            }
        }
        System.out.println(s);
    }
}
