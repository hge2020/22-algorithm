arr = input()

b = 0
num_zero = 0
num_one = 0
for i in range(arr):
    if ((i == '0') & (b == 0)):
        b = 0 
    elif ((i == '0') & (b == 1)):
        num_zero += 1
        b = 0
    elif ((i == '1') & (b == 1)):
        b = 1
    elif ((i == '1') & (b == 0)):
        b = 1
        num_one += 1

print(num_zero if(num_zero < num_one) else num_one)