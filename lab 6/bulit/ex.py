# def up_low(string):
#     up = sum(1 for char in string if char.isupper())
#     low = sum(1 for char in string if char.islower())
#     return up, low

# string = input()
# up, low = up_low(input_string)
# print(f"Up: {up}")
# print(f"Low: {low}")
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

# def is_palindrome(string):
#     return string == string[::-1]

# input_string = input("Enter a string: ")
# if is_palindrome(input_string):
#     print("The string is a palindrome")
# else:
#     print("The string is not a palindrom

text=str(input())
a=text[::-1]
if text==a:
    print("poli")
else:
    print("not poli")