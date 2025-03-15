#include <stdio.h>
#include <string.h>

/*
算法思路：
这是一个订票系统，处理两种请求：订票和助力
1. 订票请求：
   - 检查剩余票数是否足够
   - 如果足够，扣除相应票数并标记成功
   - 如果不够，标记失败
2. 助力请求：
   - 查找对应订单
   - 如果找到且助力次数未超过30次，增加助力次数
   - 如果找不到或助力次数已达上限，标记失败
*/

#define MAX_ORDERS 10000

// 订单结构体
typedef struct
{
    char uid[9];      // 用户唯一标识
    char order_id[9]; // 订单ID
    int tickets;      // 请求票数
    int success;      // 是否成功
    int assist_count; // 被助力的次数
    int position;     // 订单在队列中的位置
} Order;

int N;                    // 总票数
Order orders[MAX_ORDERS]; // 订单队列
int order_count = 0;      // 当前订单数
int assists[MAX_ORDERS];  // 助力记录
int total_assists = 0;    // 当前总助力数

// 判断助力是否有效
int is_assist_valid(int assist_pos, int order_pos)
{
    return assist_pos < order_pos && assists[assist_pos] == 0;
}

// 处理订单请求
void process_order(char *uid, char *order_id, int tickets)
{
    if (tickets <= N) // 票数充足
    {
        N -= tickets; // 扣除票数
        printf("%s %s %d success\n", uid, order_id, tickets);
    }
    else // 票数不足
    {
        printf("%s %s %d failure\n", uid, order_id, tickets);
    }
}

// 处理助力请求
void process_assist(char *uid, char *order_id)
{
    // 查找订单
    for (int i = 0; i < order_count; i++)
    {
        if (strcmp(orders[i].order_id, order_id) == 0)
        {
            // 检查助力次数是否达到上限
            if (orders[i].assist_count < 30)
            {
                orders[i].assist_count++;
                orders[i].position--;
                printf("%s %s %d success\n", uid, order_id, orders[i].tickets);
            }
            else
            {
                printf("%s %s %d failure\n", uid, order_id, orders[i].tickets);
            }
            return;
        }
    }
    // 订单未找到
    printf("%s %s failure\n", uid, order_id);
}

int main()
{
    // 读取总票数
    scanf("%d", &N);
    char uid[9], order_id[9];
    int tickets;

    // 处理输入的请求
    while (scanf("%s", uid) != EOF)
    {
        int type;
        scanf("%d", &type);
        if (type == 0) // 订票请求
        {
            scanf("%s %d", order_id, &tickets);
            process_order(uid, order_id, tickets);
        }
        else if (type == 1) // 助力请求
        {
            scanf("%s", order_id);
            process_assist(uid, order_id);
        }
    }

    return 0;
}
