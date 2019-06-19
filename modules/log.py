print("welcome")
a=input("Enter a vlaue:")
b=input("Enter b value:")
print("before conversion a=%s,b=%s"%(a,b))
try:
    a=float(a)
    b=float(b)
    print("after conversion: a=%s, b=%s"%(a,b))
    res=a/b
    print("result=%s"%res)
except ZeroDivisionError as err:
    print("expecting b!=0")
except ValueError as err:
    print("expecting digits only for a,b")
except Exception as err:
    print(err)
    print("something went wrong, contact with admin.")
except:
    print("sometinh went wrong in machine")
print("thnak you")