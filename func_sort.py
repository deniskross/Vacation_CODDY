list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]
list_a_reversed = list_a[::-1]
list_b_reversed = list_b[::-1]
a = len(list_a)
b = len(list_b)
res = []

index_a = 0
index_b = 0

while index_a < a and index_b < b:
    if list_a_reversed[index_a] > list_b_reversed[index_b]:
            res.append(list_a_reversed[index_a])
            index_a += 1
    else:
        res.append(list_b_reversed[index_b])
        index_b += 1
while index_a < a:
    res.append(list_a_reversed[index_a])
    index_a += 1
while index_b < b:
    res.append(list_b_reversed[index_b])
    index_b += 1

print(res)