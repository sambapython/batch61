a=1000
b=2000
c=3000
d=a+b+c
def fun(x,y):
	try:
		print(x,y)
		res=x+y
		print(res)
	except Exception as err:
		print(err)
print(a,b,c,d)
import pdb;pdb.set_trace()
for i in [1,2,0,3,4,5]:
	if i!=0:
		res=10/i 
		print(res)
import pdb;pdb.set_trace()
fun(10,20)
print("done")