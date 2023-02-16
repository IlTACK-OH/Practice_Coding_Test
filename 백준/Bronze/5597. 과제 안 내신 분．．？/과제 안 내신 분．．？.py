attendance = [i for i in range(1,31)]
for _ in range(28):
    num = int(input())
    attendance.remove(num)

attendance.sort()

print(f"{attendance[0]}\n{attendance[1]}")