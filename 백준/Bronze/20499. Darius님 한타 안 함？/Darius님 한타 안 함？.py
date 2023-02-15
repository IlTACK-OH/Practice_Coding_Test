import re

kda_ori = input()
kda_list = list(map(int,re.sub('[/]',' ',kda_ori).split()))

if kda_list[0]+kda_list[2] < kda_list[1] or kda_list[1]==0:
  print('hasu')
else:
  print('gosu')