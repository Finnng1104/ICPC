# Tổng hợp các kỹ thuật hình học trong ICPC

## 1. Tọa độ và hình học phẳng cơ bản

- Kiểm tra giao điểm 2 đoạn thẳng
- Kiểm tra 3 điểm thẳng hàng
- Tính diện tích tam giác, tứ giác
- Tính khoảng cách từ điểm đến đường thẳng

Ví dụ (C++):
```cpp
struct Point {
    double x, y;
    Point operator-(const Point& p) const {
        return {x - p.x, y - p.y};
    }
    double cross(const Point& p) const {
        return x * p.y - y * p.x;
    }
};

bool collinear(Point a, Point b, Point c) {
    return (b - a).cross(c - a) == 0;
}
```

## 2. Góc, vector, hướng

- Góc giữa hai vector
- Vector đơn vị (unit vector)
- Vector pháp tuyến
- Quay điểm quanh điểm khác

Ví dụ (C++):
```cpp
double dot(Point a, Point b) {
    return a.x * b.x + a.y * b.y;
}
double angle(Point a, Point b) {
    return acos(dot(a, b) / (sqrt(dot(a, a)) * sqrt(dot(b, b))));
}
```

## 3. Đa giác

- Kiểm tra điểm có nằm trong đa giác không (ray casting)
- Tính diện tích đa giác (công thức shoelace)
- Kiểm tra đa giác lồi

Ví dụ:
```cpp
double polygon_area(const vector<Point>& pts) {
    double area = 0;
    int n = pts.size();
    for (int i = 0; i < n; ++i)
        area += pts[i].cross(pts[(i+1)%n]);
    return fabs(area) / 2.0;
}
```

## 4. Hình tròn

- Tâm đường tròn ngoại tiếp tam giác
- Giao điểm đường thẳng và đường tròn
- Giao điểm hai đường tròn

Ví dụ:
```cpp
Point circumcenter(Point a, Point b, Point c) {
    double d = 2 * (a.x*(b.y - c.y) + b.x*(c.y - a.y) + c.x*(a.y - b.y));
    double ux = ((a.x*a.x + a.y*a.y)*(b.y - c.y) +
                 (b.x*b.x + b.y*b.y)*(c.y - a.y) +
                 (c.x*c.x + c.y*c.y)*(a.y - b.y)) / d;
    double uy = ((a.x*a.x + a.y*a.y)*(c.x - b.x) +
                 (b.x*b.x + b.y*b.y)*(a.x - c.x) +
                 (c.x*c.x + c.y*c.y)*(b.x - a.x)) / d;
    return {ux, uy};
}
```

## 5. Bao lồi (Convex Hull)

- Sử dụng Graham Scan hoặc Andrew's Monotone Chain
- Dùng cho bài toán: tìm diện tích nhỏ nhất bao toàn bộ điểm

Ví dụ (Monotone Chain):
```cpp
vector<Point> convex_hull(vector<Point> pts) {
    sort(pts.begin(), pts.end(), [](Point a, Point b) {
        return a.x < b.x || (a.x == b.x && a.y < b.y);
    });
    vector<Point> hull;
    for (int pass = 0; pass < 2; ++pass) {
        size_t start = hull.size();
        for (auto& p : pts) {
            while (hull.size() >= start + 2 &&
                   (hull[hull.size()-1] - hull[hull.size()-2]).cross(p - hull.back()) <= 0)
                hull.pop_back();
            hull.push_back(p);
        }
        hull.pop_back();
        reverse(pts.begin(), pts.end());
    }
    return hull;
}
```

## 6. Sweep Line và Closest Pair

- Closest pair of points: độ phức tạp O(n log n)
- Sử dụng sweep line với set tự cân bằng

Gợi ý thuật toán:
```cpp
// Closest pair of points dùng chia để trị (divide and conquer)
```

