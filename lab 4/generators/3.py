n = int(input("n:"))
divisibleby3 = (x for x in range(1,n) if x % 3 == 0 and x % 4 == 0)
print(list(divisibleby3))