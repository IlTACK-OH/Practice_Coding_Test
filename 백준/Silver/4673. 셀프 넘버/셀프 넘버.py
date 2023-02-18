num = 2
num_set = set([2])
while True:
    sum_num = num  
    for i in str(num):
        sum_num += int(i)
    
    num_set.add(sum_num)
    num += 1
    
    if num == 10000:
        break
    
for i in range(1,10001):
    if i not in num_set:
        print(i)