import math

num = 1
for i in range(1,21):
	deno = i
	ans = str((float(num)/deno)*100)
	befdec = ans.split(".")[0]
	afdec = ans.split(".")[1][:2]
	print("%d/%d = %s"%(num,deno,befdec+"."+afdec))


