n = int(input())

def get_phase(G, W, R, T):
    cycle = G + W + R
    if T == 1:
        return "Guiding Beat"
    time_passed = T + 0.5
    t = time_passed % cycle
  
    if t < G:
        return "Guiding Beat"
    elif t < G + W:
        return "Warning Beat"
    else:
        return "Resting Phase"

for _ in range(n):
    G, W, R, T = map(int, input().split())
    print(get_phase(G, W, R, T))