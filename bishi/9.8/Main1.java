import java.util.*;
public class Main1{
    public static void main(String[] args)
    {
        Scanner scanner =new Scanner(System.in);
        int n=Integer.parseInt(scanner.nextLine());
        String[] data=scanner.nextLine().split(" ");
        Map<Integer,List<Integer>>hp=new HashMap<>();
        for(int i=0;i<n;i++)
        {
            int v=Integer.parseInt(data[i]);
            int cnt=Integer.bitCount(v);
            hp.computeIfAbsent(cnt,k->new ArrayList<>()).add(v);
        }
        int res=0;
        for(Map.Entry<Integer,List<Integer>>entry:hp.entrySet())
        {
            int nk = entry.getKey();
            List<Integer> lst = entry.getValue();
            lst.sort(Comparator.naturalOrder());

            Map<Integer, Integer> dp = new HashMap<>();
            for (int v : lst) {
                dp.put(v, 1);
            }

            for(int v:lst)
            {
                int z = dp.get(v);
                res = Math.max(res, z);
                int low = v & -v;
                int nv = v + low;
                int n1 = Integer.bitCount(nv);
                for(int i=0;i<30;i++)
                {
                    if(n1>nk)
                    {
                        break;
                    }
                    if((nv&(1<<i))==0)
                    {
                        nv|=(1<<i);
                        n1++;
                    }
                }
                if(dp.containsKey(nv)){
                    dp.put(nv,Math.max(dp.get(nv),z+1));
                }
            }
            
        }
        System.out.println(res);
    }
}