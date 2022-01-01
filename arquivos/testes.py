menorP, maiorP, quantV = -9, 9, 2
nums = []

for c in range(menorP, maiorP):

    cont = c
    nums.append(cont)

    for c2 in range(1, 100):

        cont += 0.01
        nums.append(round(cont, 2))

nums.append(maiorP)

print(len(nums))

zero = nums.index(0)
#nums.pop(zero)
numsA = nums[:]
numsA.pop(zero)
print(nums)