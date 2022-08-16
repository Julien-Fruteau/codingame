# Solution submitted (len : 67)

res=1
for i in range(1, int(input())+1):
    res*=i
print(f"{res}")


# Fancy algo (exactly the same len ! : 67)

f=lambda x: 1 if x == 0 else x * f(x-1)
print(f"{f(int(input()))}")
