
def shortpali(input):
    inputArr = list(input)
    revInputArr = list(input)
    revInputArr.reverse()
    inputArr.append(' ')
    inputArr += revInputArr
    table = [0]*len(inputArr)

    for i in range(len(table)):
        if i==0:
            continue
        j = table[i-1]

        while( j>0 and inputArr[i] != inputArr[j]):
            j = table[j-1]

        if (inputArr[i] == inputArr[j]):
            table[i] = j + 1

    subOut = len(input) - table[-1]
    ans = revInputArr[:subOut]
    ans = ''.join(ans)
    return ans+input
print shortpali("sasi")