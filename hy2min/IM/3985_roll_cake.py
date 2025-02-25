L = int(input())
N = int(input())
cake = [0] * (L+1)

except_idx = -1
except_max = 0

received = [0] * (N+1)

for i in range(1,N+1):
    P, K = map(int, input().split())

    if K-P > except_max:
        except_max = K-P
        except_idx = i

    for j in range(P, K+1):
        if cake[j] == 0:
            cake[j] = i
            received[i] += 1
max_num = max(received)
max_idx = received.index(max_num)

print(except_idx)
print(max_idx)