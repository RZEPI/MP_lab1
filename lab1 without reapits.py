def backtrack(array, lengthOfPremutation, start, permutation):
    if start == lengthOfPremutation:
        print(permutation)
        return 1
    count = 0
    for i in range(start, len(array)):
        array[start], array[i] = array[i], array[start]
        permutation[start] = array[start]
        count += backtrack(array, lengthOfPremutation, start + 1, permutation)
        array[start], array[i] = array[i], array[start]
    return count


def permute(array, lengthOfPremutation):
    count = 0
    permutation = [0] * lengthOfPremutation
    count = backtrack(array, lengthOfPremutation, 0, permutation)
    return count

count = permute([1,2,3, 4, 5, 6], 4)
print(count)