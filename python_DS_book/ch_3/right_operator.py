def sum_of_lists(n):
    total = 0
    for i in range(1):
        lst_1 = [j ^ (j << i) for j in range(n)]
        total += sum(lst_1)

    return total 

print(sum_of_lists(2))