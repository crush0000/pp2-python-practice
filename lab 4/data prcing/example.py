# import datetime
# x=datetime.datetime.now()
# y=datetime.datetime.now()
# print(y.month)
# print(x.strftime("%A"))

# import datetime
# date = datetime.datetime.now()-datetime.timedelta(days=5)
# print(date)


# b=int(input())
# c=int(input())
# a=[i**2 for i in range(c+1)]
# print(a)


# a=[i**2 for i in range(2,6)]
# print(a)
# b=(i**2 for i in range(2,6))
# # for i in b:
# #     print(i)

# print(sum(b))

# b=int(input())
# a=[i for i in range(1,b) if i%2==0]

# print(a)

# def squares(a,b):
#     while a <= b:
#         yield a * a
#         a += 1
# a, b = int(input()), int(input())
# nums = []
# for x in squares(a, b):
#     nums.append(x)
# print(nums)


# def square(a,b):
#     while a<=b:
#         yield b*b
#         b=b+1
# a,b=int(input()),int(input())
# v=[]
# for i in square(a,b):
#     v.append(i)
# print(i)

# import math

# def de_rad(degree):
#     radian=degree*(math.pi/180)
#     return radian
# degree=int(input())
# radian=de_rad(degree)
# print(radian)

# for i in x["imdata"]:
#     dn = i ["l1PhysIf"]["attributes"]["dn"]
#     descr= i ["l1PhysIf"]["attributes"]["descr"]
#     speed= i ["l1PhysIf"]["attributes"]["speed"]
#     mtu= i ["l1PhysIf"]["attributes"]["mtu"]
#     print(dn,"                           ",descr,speed,mtu)









# n=int(input())
# def nextsq(n):
#     # n=int(input())
#     squares=nextsq(n)
#     for i in squares:
#         if i%3==0:
#             print(i,end=" ")
# nextsq(n)


def nextsq(n):
    for i in range(1,n+1):
        yield i
n=int(input())
squares=nextsq(n)
for i in squares:
    if i%3==0:
        print(i,end=" ")




