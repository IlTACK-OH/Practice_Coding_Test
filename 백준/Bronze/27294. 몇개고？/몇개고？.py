time, achol = map(int,input().split())

if achol:
    print(280)
else:
    if time <= 11 or time > 16:
        print(280)
    else:
        print(320)