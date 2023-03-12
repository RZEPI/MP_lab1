def permute(listToChange, fullList, level):
    if level == len(fullList):
        print(listToChange)
        return
    for i in fullList:
        listToChange[level] = i
        permute(listToChange, fullList, level+1)  

listToPermute = [1,2,3,4]
permute(listToPermute, listToPermute.copy(), 0)
