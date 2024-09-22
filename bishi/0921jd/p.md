# 1
有几个物品，第i个物品的价值为 q。现在要给这些物品分组，每一组必须是一个下标连续的区间。同时，每一组内的物品差距不能太大，即任意一组内物品的最大价值减去最小价值不能超过某个给定的常数k。
给定这些物品，请问最少要分几组?
输入描述：
第一行两个整数 n,k(1 < n < 10^5 , 0 <= k <= 10^9)，表示物品的数量及给定的常数。
第二行n个整数ai(0 < ai 10^9),表示物品的价值.
输出描述：
输出一行一个整数，表示最少的分组数。
示例1：
输入：
4 1
1 3 1 4
输出：
4
示例2：
4 2
1 3 14
输出：
2
```java
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int k=sc.nextInt();
        int[] values=new int[n];
        for(int i=0;i<n;i++){
            values[i]=sc.nextInt();
        }
        int res=minGroup(n,k,values);
        System.out.println(res);
    }
private static int minGroup(int n,int k, int[] values){
    Arrays.sort(values);
    int groups=0;
    int l=0;
    while(l<n){       
        int r = l;
        while(r<n && values[r]-values[l]<=k){
            r++;          
        }
        groups++;
        l=r;
        
    }
    return groups;
}
}

```
# 2
一条单向单车道的道路上有 n 辆车，第讠辆车位于xi速度大小为vi
显然，如果车辆保持此速度行驶下去，在大多数情况下都会发生碰撞，
现在牛牛想知道，至少需要移除几辆车，才能让这些车不发生碰撞?
输入描述：
第一行一个整数 n(1 < n < 10^5)，表示车的数量。
接下来几 行，每行两个整数 xi,vi(|xi| |ui|< 10^9)，表示车的位置和速度的大小。
数据保证xi互不相同。
输出描述：
输出一行一个整数，表示需要移除车的数量。
示例1：
输入：
3
-1 -1
0 0
1 1
输出
0

示例2：
3
-1 1
0 0
1 -1
输出：
2

# 3
【背景】:一家公司想要了解 2023 年全年所有商品的盈利情况。
【原始表】:
sales orders(销售订单)表:
order_id(订单 ID): 订单的唯一标识符
product_id (商品 ID): 商品的唯一标识符
quantity(销售数量): 销售的商品数量
unit price(销售单价): 商品的销售单价
order date (订单日期): 订单的日期
purchase prices(进货价)表:
product id (商品 ID): 商品的唯一标识符
purchase price(进货单价): 商品的进货单价.
【要求】:需要根据表格数据查询出每个商品在 2023 年的利润，字段包括具体字段名。根据上面这两个表格，查询每个商品在 2023 年的利润，包含的字段:商品 ID、利润.
查询出来的数据按照商品ID 升序排列。要求查询出来的表格的字段如下:
product id: 商品的唯一标识符
profit: 2023 年的利润(利润=(销售单价-进货单价)* 销售数。量)。
profit_margin :单个产品的利润率 (利润率=(产品平均单价-产品进货单价)/产品进货单价)(round保留2位小数)


```SQL
SELECT
    so.product_id,
    SUM((so.unit_price - pp.purchase_price) * so.quantity) AS total_profit,
    ROUND(
        CASE 
            WHEN SUM(so.quantity) = 0 THEN 0
            ELSE (
                (SUM(so.unit_price * so.quantity) * 1.0 / SUM(so.quantity) - pp.purchase_price)
                / pp.purchase_price
            ) * 100
        END,
        2
    ) AS profit_margin
FROM
    sales_orders so
JOIN
    purchase_prices pp
    ON so.product_id = pp.product_id
WHERE
    YEAR(so.order_date) = 2023
GROUP BY
    so.product_id
ORDER BY
    so.product_id ASC;

```

#3 