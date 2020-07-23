print("Enter the number:")
num=int(input())
print("Prime numbers upto", num, "are:")
for i in range(2,num+1):
    for j in range(2,i):
        if (i % j) == 0:
            break
        else:
            print(i)
            break
