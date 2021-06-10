import re
# total = 0
# for i in open("regex_sum_1266539.txt"):
#     total += sum(list(map(int,re.findall("[0-9]+",i))))
# print(total)

print(sum([int(i) for i in re.findall("[0-9]+",open("regex_sum_1270174.txt").read())]))
