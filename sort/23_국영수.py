n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))

array = sorted(array, key = lambda student: (-student[1], student[2], student[0]))

for i in array:
    print(i[0])