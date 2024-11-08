import java.util.*;
public class Main{
    static int N=200005;
    static int n,q;
    static int[] a=new int[N];
    static int[] res0=new int[N<<2];
    static int[] res1=new int[N<<2];
    static int[] len=new int[N<<2];
    static void build(int i,int l,int r){
        if(l==r){
            res0[i]=res1[i]=a[l];
            len[i]=1;
            return;
        }
        int m=(l+r)>>1;
        build(i<<1,l,m);
        build(i<<1|1,m+1,r);
        len[i]=len[i<<1]+len[i<<1|1];
        for(int op=0;op<2;++op){
            if(len[i<<1]%2==1){
                if(op==0)
                    res0[i]=res0[i<<1]&res0[i<<1|1];
                else
                    res1[i]=res1[i<<1]|res1[i<<1|1];
            }else{
                if(op==0)
                    res0[i]=res0[i<<1]|res0[i<<1|1];
                else
                    res1[i]=res1[i<<1]&res1[i<<1|1];
            }
        }
    }
    static int[] query(int i,int l,int r,int x,int y){
        if(x<=l&&r<=y)return new int[]{res0[i],res1[i],len[i]};
        int m=(l+r)>>1;
        if(y<=m)return query(i<<1,l,m,x,y);
        else if(x>m)return query(i<<1|1,m+1,r,x,y);
        else{
            int[] left=query(i<<1,l,m,x,y);
            int[] right=query(i<<1|1,m+1,r,x,y);
            int[] res=new int[3];
            res[2]=left[2]+right[2];
            for(int op=0;op<2;++op){
                if(left[2]%2==1){
                    if(op==0)
                        res[op]=left[op]&right[op];
                    else
                        res[op]=left[op]|right[op];
                }else{
                    if(op==0)
                        res[op]=left[op]|right[op];
                    else
                        res[op]=left[op]&right[op];
                }
            }
            return res;
        }
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();q=sc.nextInt();
        for(int i=1;i<=n;++i)a[i]=sc.nextInt();
        build(1,1,n);
        while(q-->0){
            int op,l,r;
            op=sc.nextInt();l=sc.nextInt();r=sc.nextInt();
            int[] res=query(1,1,n,l,r);
            System.out.println(res[op-1]);
        }
    }
}
