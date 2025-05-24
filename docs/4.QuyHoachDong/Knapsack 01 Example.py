def knapsack_01(n, W, weights, values):
    # Khởi tạo bảng dp có (n+1) hàng và (W+1) cột với giá trị ban đầu là 0
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Duyệt qua từng món đồ
    for i in range(1, n + 1):
        # Duyệt qua từng mức trọng lượng từ 0 đến W
        for w in range(W + 1):
            # Nếu có thể chọn món đồ thứ i (tức trọng lượng của nó <= w hiện tại)
            if weights[i - 1] <= w:
                # Chọn giá trị lớn nhất giữa:
                # - Không chọn món thứ i: dp[i-1][w]
                # - Chọn món thứ i: dp[i-1][w - weights[i-1]] + values[i-1]
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # Nếu không thể chọn, giữ lại giá trị cũ
                dp[i][w] = dp[i - 1][w]

    # Trả về giá trị tối đa đạt được khi xét tất cả món và trọng lượng tối đa W
    return dp[n][W]

# Ví dụ dữ liệu đầu vào
n = 4  # Số lượng đồ vật
W = 8  # Trọng lượng tối đa balo
weights = [3, 4, 5, 2]  # Trọng lượng của từng món
values = [30, 50, 60, 40]  # Giá trị tương ứng của từng món

# In kết quả
print(knapsack_01(n, W, weights, values))  # Output: 90
