# 📝 Bài 8: Phân công công việc
# ===============================================
"""
Đề bài: Có N công việc và M nhân viên. Mỗi công việc i cần t[i] thời gian
và mỗi nhân viên j có năng suất p[j]. Một nhân viên chỉ có thể làm một
công việc tại một thời điểm. Tìm thời gian ngắn nhất để hoàn thành tất cả
công việc.

Input:
- Dòng 1: N và M (1 ≤ N,M ≤ 10^5)
- Dòng 2: N số nguyên t[i] (1 ≤ t[i] ≤ 10^9)
- Dòng 3: M số nguyên p[j] (1 ≤ p[j] ≤ 10^9)

Output:
- Thời gian ngắn nhất để hoàn thành tất cả công việc

Ví dụ:
Input:
4 2
5 3 4 2
2 3

Output:
6
"""

def can_complete(tasks, workers, time):
    # Sắp xếp công việc theo thời gian giảm dần
    tasks.sort(reverse=True)
    # Sắp xếp nhân viên theo năng suất giảm dần
    workers.sort(reverse=True)
    
    # Tính số công việc mỗi nhân viên có thể làm
    task_count = 0
    for p in workers:
        # Số công việc nhân viên này có thể làm trong thời gian time
        max_tasks = time // p
        # Lấy các công việc còn lại
        remaining = min(max_tasks, len(tasks) - task_count)
        if remaining <= 0:
            break
        task_count += remaining
    
    return task_count >= len(tasks)

def solve():
    # Đọc input
    n, m = map(int, input().split())
    tasks = list(map(int, input().split()))
    workers = list(map(int, input().split()))
    
    # Tìm kiếm nhị phân
    left = 1
    right = max(tasks) * n  # Thời gian tối đa có thể
    
    while left < right:
        mid = (left + right) // 2
        if can_complete(tasks, workers, mid):
            right = mid
        else:
            left = mid + 1
    
    # In kết quả
    print(left)
    
    # Phần mở rộng: In phân công chi tiết
    print("\nPhân công chi tiết:")
    
    # Sắp xếp lại để phân công
    tasks_with_index = [(t, i) for i, t in enumerate(tasks, 1)]
    tasks_with_index.sort(reverse=True)
    workers_with_index = [(p, i) for i, p in enumerate(workers, 1)]
    workers_with_index.sort(reverse=True)
    
    # Phân công công việc
    assignments = [[] for _ in range(m)]
    task_count = 0
    
    for p, worker_idx in workers_with_index:
        max_tasks = left // p
        remaining = min(max_tasks, len(tasks) - task_count)
        
        for i in range(remaining):
            if task_count < len(tasks):
                t, task_idx = tasks_with_index[task_count]
                assignments[worker_idx-1].append((task_idx, t))
                task_count += 1
    
    # In kết quả phân công
    for i, worker_tasks in enumerate(assignments, 1):
        if worker_tasks:
            print(f"Nhân viên {i} (năng suất {workers[i-1]}):")
            total_time = 0
            for task_idx, t in worker_tasks:
                print(f"  - Công việc {task_idx} (thời gian {t})")
                total_time += t
            print(f"  Tổng thời gian: {total_time}")
            print(f"  Thời gian thực tế: {left}")

if __name__ == "__main__":
    solve() 