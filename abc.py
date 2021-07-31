marksheet = []
students = []
scorelist = []
for i in range(int(input())):
    a = input()
    c = float(input())
    scorelist.append(c)
    marksheet.append([a,c])

scorelist = set(scorelist)
marksheet.sort(key = lambda x: x[1])
second_lowest = sorted(list(scorelist))
if len(second_lowest)<=2:
    second_lowest = second_lowest[0]
else:
    second_lowest = second_lowest[1]
print(second_lowest)
for i in range(len(marksheet)):
    if len(scorelist)==2:
        if second_lowest==marksheet[i][1]:
            students.append(marksheet[i][0])
    else:
        if second_lowest==marksheet[i][1]:
            students.append(marksheet[i][0])
students.sort()
for x in range(len(students)):
    print (students[x])