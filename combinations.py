def generate_combinations(list, fullList, m, startIndex, level):
    count = 0
    if level == m:
        print(list)
        return 1
    for i in range(startIndex, len(fullList)):
        list.append(fullList[i])
        count += generate_combinations(list, fullList, m, i+1, level+1)
        list.pop()
    return count

n = 6
m = 3
list = []
for i in range(1, n+1):
    list.append(i)

count = generate_combinations([], list, m,0, 0)
print(count)