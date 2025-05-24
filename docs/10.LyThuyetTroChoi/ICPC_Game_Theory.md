# ICPC - Lý thuyết trò chơi (Game Theory)

## 1. Khái niệm cơ bản
Lý thuyết trò chơi là ngành nghiên cứu các tình huống trong đó hành động của mỗi người chơi ảnh hưởng đến kết quả của người khác. Trong ICPC, thường gặp các bài toán hai người chơi, lần lượt di chuyển và tối ưu theo chiến lược.

- **Trò chơi hai người**: Hai người chơi (Player 1 và Player 2) thi đấu theo lượt.
- **Trò chơi tổng bằng 0**: Nếu một người thắng thì người còn lại thua.
- **Trạng thái thắng/thua**: Một trạng thái gọi là **winning** nếu người chơi đến lượt có thể di chuyển để đưa trò chơi về trạng thái **losing** của đối thủ.

## 2. Các dạng bài phổ biến

### 2.1 Trò chơi Nim (Nim Game)
- Có `n` đống sỏi, mỗi đống có `a_i` viên.
- Hai người thay phiên lấy bất kỳ số sỏi nào từ một đống.
- Người không còn lượt chơi là người thua.
- Điều kiện thắng: XOR tất cả các đống, nếu khác 0 thì người chơi hiện tại có chiến lược thắng.

```cpp
bool isWinning(vector<int>& heaps) {
    int xor_sum = 0;
    for (int h : heaps) xor_sum ^= h;
    return xor_sum != 0;
}
```

### 2.2 Trò chơi Grundy (Sprague-Grundy)
- Mỗi trạng thái trò chơi có một giá trị Grundy (hoặc Nimbers).
- Trạng thái thua có Grundy = 0.
- Trạng thái có thể chuyển về các trạng thái có Grundy `{g1, g2, ..., gn}` thì Grundy của trạng thái đó là **mex** của tập đó (minimum excluded number).

```cpp
int grundy(int x) {
    if (x == 0) return 0;
    set<int> s;
    for (int move : allowed_moves(x)) {
        s.insert(grundy(x - move));
    }
    return mex(s);
}
```

### 2.3 Trò chơi dạng xếp quân, đi ô
- Các bài toán bàn cờ (chơi trên grid, đi theo quy tắc)
- Cách giải: quy mỗi trạng thái thành Grundy number và xử lý giống như Nim.

## 3. Chiến thuật tổng quát
- Duyệt qua tất cả trạng thái có thể, tính Grundy.
- Tổng XOR của các Grundy tương ứng với trạng thái trò chơi ban đầu: nếu khác 0 là người đi trước thắng.
- Memoization hoặc quy hoạch động giúp tối ưu.

## 4. Thư viện và template sử dụng

```cpp
int grundy[MAXN];
bool vis[MAXN];

int compute_grundy(int u) {
    if (vis[u]) return grundy[u];
    vis[u] = true;
    set<int> s;
    for (int v : next_states(u)) {
        s.insert(compute_grundy(v));
    }
    int g = 0;
    while (s.count(g)) g++;
    return grundy[u] = g;
}
```

## 5. Một số bài mẫu
- [SPOJ - ANARC09G](https://www.spoj.com/problems/ANARC09G/)
- [Codeforces - Game with Coins](https://codeforces.com/problemset/problem/820/A)