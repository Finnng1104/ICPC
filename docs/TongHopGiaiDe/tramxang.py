so_tram = int(input())

luong_xang_moi_tram = list(map(int, input().split()))
thoi_gian_cho_1_lit = list(map(int, input().split()))

luong_xang_moi_tram *= 2
thoi_gian_cho_1_lit *= 2

thoi_gian_nho_nhat = float('inf')

for vi_tri_bat_dau in range(so_tram):
    tong_xang = 0
    tong_thoi_gian = 0

    for i in range(vi_tri_bat_dau, vi_tri_bat_dau + so_tram):
        if tong_xang >= so_tram:
            break

        xang_can_thiet = so_tram - tong_xang
        xang_se_do = min(luong_xang_moi_tram[i], xang_can_thiet)

        tong_xang += xang_se_do
        tong_thoi_gian += xang_se_do * thoi_gian_cho_1_lit[i]

    if tong_xang >= so_tram:
        thoi_gian_nho_nhat = min(thoi_gian_nho_nhat, tong_thoi_gian)

if thoi_gian_nho_nhat == float('inf'):
    print("-1")
else:
    print(thoi_gian_nho_nhat)