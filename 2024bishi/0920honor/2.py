
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
def main():
    N = sint()
    jobs = []
    
    for _ in range(N):
        job = lint()
        job_id, reward, start, end = job
        jobs.append((start, end, reward))
    jobs.sort(key=lambda x: x[1])
    
   
    dp = [0] * (N + 1)
    
    end_times = [job[1] for job in jobs]
    def binary_search(current_start):
        left, right = 0, len(end_times) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if end_times[mid] <= current_start:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result
    
    for i in range(1, N + 1):
        current_start, current_end, current_reward = jobs[i-1]
        index = binary_search(current_start)
        if index != -1:
            dp[i] = max(dp[i-1], dp[index + 1] + current_reward)
        else:
            dp[i] = max(dp[i-1], current_reward)
    print(dp[N])

if __name__ == "__main__":
    main()
