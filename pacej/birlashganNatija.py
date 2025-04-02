# # try:
# #     n = 0
# #     res = 100/0
# # except ZeroDivisionError:
# #     print("you cant`tv divide by zero!")
# # except ValueError:
# #     print("enter a valid numer")
# # else:
# #     print("result is red finall")
# from math import expm1
#
# from encodings.idna import ace_prefix
#
# try:
#     x= int("s")
#     inv = x/0
# except ValueError:
#     print("not vvlid")\
# except (ValueErrorб Typ)


# a = ["10", "twenty", 30]  # Aralash ro‘yxat
# try:
#     total = int(a[0]) + int(a[1])  # 'twenty' son emas, ValueError
# except (ValueError, TypeError) as e:
#     print("Error:", e)
# except IndexError:
#     print("Index out of range.")


def set_age(age):
    if age < 0:
       raise ValueError("Age connot be negative.")
    print(f"Age set to {age}")