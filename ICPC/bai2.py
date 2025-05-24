# 📝 Bài 2: Tìm đường đi ngắn nhất trên lưới
# ===============================================
"""
Đề bài: Cho một lưới NxM, mỗi ô là '.' (đường đi) hoặc '#' (tường).
Tìm đường đi ngắn nhất từ ô (1,1) đến ô (N,M).
Chỉ được di chuyển theo 4 hướng: lên, xuống, trái, phải.

Input:
- Dòng 1: N và M (1 ≤ N,M ≤ 1000)
- N dòng tiếp: Mỗi dòng gồm M ký tự '.' hoặc '#'

Output:
- Số bước đi ngắn nhất, -1 nếu không có đường đi

Ví dụ:
Input:
4 4
....
.#..
..#.
....

Output:
6
"""

from collections import deque

def solve():
    # Đọc input
    n, m = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]
    
    # Các hướng di chuyển: lên, phải, xuống, trái
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    # Khởi tạo BFS
    visited = [[False]*m for _ in range(n)]
    dist = [[-1]*m for _ in range(n)]
    q = deque()
    
    # Bắt đầu từ (0,0)
    q.append((0, 0))
    visited[0][0] = True
    dist[0][0] = 0
    
    # BFS
    while q:
        x, y = q.popleft()
        
        # Kiểm tra đích
        if x == n-1 and y == m-1:
            print(dist[x][y])
            return
        
        # Thử 4 hướng
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # Kiểm tra điều kiện
            if (0 <= nx < n and 0 <= ny < m and 
                not visited[nx][ny] and grid[nx][ny] == '.'):
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    
    # Không tìm thấy đường đi
    print(-1)

if __name__ == "__main__":
    solve()
