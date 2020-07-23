print("Enter th number:")
num=int(input())
print("Prime numbers upto", num, "are:")
for l in range(2,num+1):
    if l > 1:
        for j in range(, l):
            if (l % j) == 0:
                break
            else:
                print(l)
