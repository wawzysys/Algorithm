from datetime import datetime, timedelta

T = int(input())
for _ in range(T):
    data = input().split()
    m = int(data[0])
    times = []
    for i in range(m):
        hour = int(data[1 + 2 * i])
        minute = int(data[1 + 2 * i + 1])
        time_obj = datetime(2000, 1, 1, hour, minute)
        times.append(time_obj)

    # Filter times between 08:00 and 18:00
    count_valid_times = sum(1 for t in times if datetime(2000, 1, 1, 8, 0) <= t <= datetime(2000, 1, 1, 18, 0))

    if count_valid_times < 2:
        print('Absent')
        continue

    times.sort()
    first_clock_in = times[0]
    last_clock_out = times[-1]

    # Total working duration
    total_work_duration = last_clock_out - first_clock_in

    # Subtract lunch break overlapping time
    lunch_start = datetime(2000, 1, 1, 12, 0)
    lunch_end = datetime(2000, 1, 1, 14, 0)

    # Calculate overlapping time between working period and lunch break
    overlap_start = max(first_clock_in, lunch_start)
    overlap_end = min(last_clock_out, lunch_end)
    if overlap_start < overlap_end:
        lunch_overlap = overlap_end - overlap_start
    else:
        lunch_overlap = timedelta(0)

    # Initial effective work time
    initial_effective_time = total_work_duration - lunch_overlap

    # Late arrival deduction
    scheduled_start = datetime(2000, 1, 1, 8, 0)
    if first_clock_in > scheduled_start:
        late_arrival = first_clock_in - scheduled_start
    else:
        late_arrival = timedelta(0)

    # Early departure deduction
    scheduled_end = datetime(2000, 1, 1, 18, 0)
    if last_clock_out < scheduled_end:
        early_departure = scheduled_end - last_clock_out
    else:
        early_departure = timedelta(0)

    # Total deductions
    total_deductions = late_arrival + early_departure

    # Final effective work time
    final_effective_time = initial_effective_time - total_deductions

    # Convert final effective time to minutes (can be negative)
    final_minutes = int(final_effective_time.total_seconds() // 60)
    print(final_minutes)
