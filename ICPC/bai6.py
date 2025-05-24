# 📝 Bài 6: Tìm xâu con chung dài nhất
# ===============================================
"""
Đề bài: Cho hai xâu S và T, tìm xâu con chung dài nhất (LCS) của chúng.
Xâu con là một dãy các ký tự liên tiếp trong xâu gốc.

Input:
- Dòng 1: Xâu S (1 ≤ |S| ≤ 1000)
- Dòng 2: Xâu T (1 ≤ |T| ≤ 1000)

Output:
- Dòng 1: Độ dài của LCS
- Dòng 2: Một LCS (nếu có nhiều đáp án, in ra bất kỳ)

Ví dụ:
Input:
ABCDGH
AEDFHR

Output:
3
ADH
"""

def solve():
    # Đọc input
    s = input().strip()
    t = input().strip()
    n, m = len(s), len(t)
    
    # Khởi tạo mảng DP
    # dp[i][j]: độ dài LCS của s[0..i-1] và t[0..j-1]
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    # Tính DP
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # In độ dài LCS
    print(dp[n][m])
    
    # Tìm một LCS
    lcs = []
    i, j = n, m
    
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            lcs.append(s[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    # In LCS
    print("".join(reversed(lcs)))
    
    # Phần mở rộng: In tất cả các LCS
    print("\nTất cả các LCS:")
    
    def find_all_lcs(i, j, current):
        if i == 0 or j == 0:
            if current:
                print("".join(reversed(current)))
            return
        
        if s[i-1] == t[j-1]:
            current.append(s[i-1])
            find_all_lcs(i-1, j-1, current)
            current.pop()
        else:
            if dp[i-1][j] >= dp[i][j-1]:
                find_all_lcs(i-1, j, current)
            if dp[i][j-1] >= dp[i-1][j]:
                find_all_lcs(i, j-1, current)
    
    find_all_lcs(n, m, [])

if __name__ == "__main__":
    solve() 