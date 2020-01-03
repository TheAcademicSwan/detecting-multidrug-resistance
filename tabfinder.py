F = open("mpileup_map_SRR+number_number.tab", 'r+')
# Note : The number after SRR is variable and may change on how you name each file, as will the number after. My file was named "mpileup_map_SRR5070516_2.tab".
i = F.readline()
a = []
b = []
c = []
d = []
e = []
g = [a, b, c, d, e]
while len(i) > 0:
    i = i.split('\t')
    for j in range(5):
        g[j].append(i[j])
    i = F.readline()
there = False
final = []
for i in range(len(e)):
    e[i] = e[i].lower()
    if 't' in e[i] and '*' not in e[i] and '.' not in e[i] and ',' not in e[i]:
        there = True
#        letter = "T"
    elif 'c' in e[i] and '*' not in e[i] and '.' not in e[i] and ',' not in e[i]:
        there = True
#        letter = "C"
    elif 'g' in e[i] and '*' not in e[i] and '.' not in e[i] and ',' not in e[i]:
        there = True
#        letter = "G"
    elif 'a' in e[i] and '*' not in e[i] and '.' not in e[i] and ',' not in e[i]:
        there = True
#        letter = "A"
    if there:
        final.append(1)
    else:
        final.append(0)
    there = False
points = []
for i in range(len(final)):
    if final[i] == 1:
        points.append(i)
print(points)
