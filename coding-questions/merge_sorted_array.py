array1 = [1, 3, 5, 9, 10]
array2 = [2, 4, 6, 7, 8]
output = []

pointer1 = 0
pointer1End = len(array1)
pointer2 = 0
pointer2End = len(array2)

while pointer1 < pointer1End and pointer2 < pointer2End:
    if array1[pointer1] < array2[pointer2]:
        output.append(array1[pointer1])
        pointer1 += 1
    else:
        output.append(array2[pointer2])
        pointer2 += 1

while pointer1 < pointer1End:
    output.append(array1[pointer1])
    pointer1 += 1

while pointer2 < pointer2End:
    output.append(array2[pointer2])
    pointer2 += 1

print(output)
