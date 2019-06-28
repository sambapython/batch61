"""
lkjdsflksdja kljfdslkj fa
"""
print("welcome")
A_VALUE = input("Enter a value:")
B_VALUE = input("Enter b value:")
print(f"before conversion a={A_VALUE},b={B_VALUE}")
try:
    A_VALUE = float(A_VALUE)
    B_VALUE = float(B_VALUE)
    print(f"after conversion a={A_VALUE},b={B_VALUE}")
    RES = A_VALUE / B_VALUE
    print("result=", RES)
except ValueError as err:
    print("expecting digits")
except ZeroDivisionError as err:
    print("expecting b!=0")
except Exception as err:
    print("ERROR:", err)
print("thank you!!")
print("main block statements....")
