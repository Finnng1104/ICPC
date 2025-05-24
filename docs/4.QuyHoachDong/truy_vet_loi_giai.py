# 📘 Truy vết lời giải từ bảng DP
# Ví dụ: Xâu con chung dài nhất (LCS - Longest Common Subsequence)
# Cho 2 chuỗi A, B → tìm độ dài và in ra 1 xâu con chung dài nhất

# ✅ dp[i][j] = độ dài LCS của A[0..i-1] và B[0..j-1]

def lcs_trace(A, B):
    n, m = len(A), len(B)
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # ✅ Truy vết từ dp[n][m] để in xâu con
    i, j = n, m
    result = []
    while i > 0 and j > 0:
        if A[i-1] == B[j-1]:
            result.append(A[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return dp[n][m], ''.join(reversed(result))

# 📌 Ví dụ:
A = "ABCBDAB"
B = "BDCAB"
length, lcs_string = lcs_trace(A, B)
print(f"Độ dài LCS: {length}")
print(f"LCS: {lcs_string}")

# 🧠 Khi dùng:
# - Bài toán yêu cầu in lại phương án tối ưu
# - Phải lưu bảng dp[][] → từ điểm cuối quay ngược lại theo hướng chọn giá trị tối ưu
# - Áp dụng cho: truy vết dãy con, phân đoạn, chọn đồ,...