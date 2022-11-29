n = int(input())
sum = 0
acc = 0

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array)

while(len(array) != 1):
    sum = array[0]+array[1] #새로운 카드 묶음의 덧셈개수
    array.pop(0)
    array.pop(0)
    acc = acc + sum #지금까지 쌓인 덧셈갯수 + 새로운 카드 묶음의 덧셈개수
    array.append(sum)
    array = sorted(array)


if (n == 1):
    print(0)
else:
    print(acc)



#sort
# pop(i)
# sum = sum + i
# acc = acc + sum
# append(sum)