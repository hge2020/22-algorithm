N, M = map(int, input().split())

arr = []
max = 0
for i in range(N):
        arr.append( list(map(int, input().split())) )
        arr_min = min(arr[i])
        if(max<arr_min):
            max = arr_min

print(max)