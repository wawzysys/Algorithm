#include <stdio.h>
#include <stdlib.h>

// 定义磁盘请求结构体
typedef struct
{
    int request_number; // 请求的磁道号
} DiskRequest;

// 先来先服务调度算法
void fcfs(DiskRequest requests[], int num_requests, int start_position)
{
    int current_position = start_position; // 当前磁头位置
    int total_distance = 0;                // 总移动距离
    int i;

    printf("FCFS磁盘调度算法:\n");
    printf("初始磁头位置: %d\n", start_position);

    for (i = 0; i < num_requests; i++)
    {
        int distance = abs(requests[i].request_number - current_position);
        total_distance += distance;
        current_position = requests[i].request_number; // 移动磁头到新的请求位置
        printf("处理磁道号 %d, 移动距离 %d\n", requests[i].request_number, distance);
    }

    printf("总移动距离: %d\n", total_distance);
}

int main()
{
    DiskRequest requests[] = {{45}, {20}, {78}, {34}, {65}, {123}, {87}};
    int num_requests = sizeof(requests) / sizeof(requests[0]);
    int start_position = 50; // 假设初始磁头位置为50

    // 调用FCFS算法
    fcfs(requests, num_requests, start_position);

    return 0;
}
