n = int(input("n:"))
evens = (x for x in range(1,n) if x % 2 == 0)
print(list(evens))