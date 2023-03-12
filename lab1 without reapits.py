listToPermute = [1,2,3,4,5,6]
def permute(list, fullList, level, stop):
    count = 0
    if level == stop:
        print(list[0:stop])
        return 1
    fullListCopy = fullList.copy()
    for i in fullListCopy:
        list[level] = i
        fullList.remove(i)
        count += permute(list, fullList, level+1, stop)
        fullList = fullListCopy.copy()
    return count

count = permute(listToPermute, listToPermute.copy(), 0, 4)
print(count)