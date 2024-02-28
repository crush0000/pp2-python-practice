import math
# n=int(input())
# def fac(n):
#     if n==1:
#         return 1
#     return fac(n-1)*n
# print(fac(n))


# string=input()
# up=0
# low=0

# for char in string:
#     if char.isupper:
#         up=up+1
#     elif char.islower:
#         low+=1
# print("UP :",up)
# print("LOW :",low)




# text=str(input())
# a=text[::-1]
# if text==a:
#     print("poli")
# else:
#     print("not poli")



# def test():
#     num = int(input())
#     time = int(input())
#     print(f"Square root of {num} after {time} miliseconds is {math.sqrt(num)}")
# test()

def all_true(tuple):
    return all(tuple)


tuple1 = (True, True, True)
print(all_true(tuple1)) 

tuple2 = (True, False, True)
print(all_true(tuple2))  

tuple1 = (True, True, False)
print(all_true(tuple1)) 

tuple4 = (False, False, False)
print(all_true(tuple4)) 
