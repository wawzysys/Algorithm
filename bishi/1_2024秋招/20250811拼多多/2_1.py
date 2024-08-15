import heapq

def process_jobs(jobs):
    # 初始化最小堆和变量
    min_heap = []
    cur = 0  # 当前时间
    tol = 0  # 总完成耗时

    # 处理每个作业
    for ti, wi in sorted(jobs, key=lambda x: x[0]):
        # 如果当前时间小于作业布置时间，更新当前时间
        if cur < ti:
            cur = ti
        
        # 将作业添加到最小堆
        heapq.heappush(min_heap, (wi, ti))
        
        # 处理可完成的作业
        while min_heap and cur >= ti:
            # 从堆中取出完成时间最短的作业
            w, t = heapq.heappop(min_heap)
            cur += w  # 更新当前时间为作业完成时间
            tol += cur - t  # 更新总完成耗时

    # 处理剩余的作业
    while min_heap:
        w, t = heapq.heappop(min_heap)
        cur += w
        tol += cur - t

    return tol

# 测试作业数据
jobs = [(1, 5), (4, 1), (7, 3), (10, 2)]
total_time = process_jobs(jobs)
print("Total completion time:", total_time)
