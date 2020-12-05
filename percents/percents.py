import random
import math
import time
import json
import sys

accu_data = {}
try:
	with open('accuracy.json','r') as f:
		accu_data = json.loads(f.read())
except:
	print("Please initialise first !!!")
	sys.exit()

attempted = accu_data.get('Attempted')
correct = accu_data.get('Correct')
prev_record = accu_data.get('best')
cur_time = prev_record
sttime = time.time()
#------------Range----------------------------
num = 1
deno = random.randint(1,20)
#---------------------------------------------
print("%d/%d = "%(num,deno),end=" ")

userans = input()
#******** Correct Ans calc *************
ans = str((float(num)/deno)*100)
befdec = ans.split(".")[0]
afdec = ans.split(".")[1][:2]
correctans = list()
correctans.append(befdec+"."+afdec)
if len(afdec)==1:
	correctans.append(befdec)
#******** Correct Ans calc *************
attempted+=1
print("-"*15)
if userans in correctans:
	print("Correct !!!")
	cur_time = time.time()-sttime
	print("Time taken:",format(cur_time,'.4f'),"sec")
	correct+=1
else:		
	print("Wrong !!!")
	print("Correct ans is: %s"%correctans[0])
print("-"*15)	

incorrect = attempted-correct
accu_data['Attempted'] 	= attempted
accu_data['Correct'] 	= correct
accu_data['Incorrect'] 	= incorrect
accu_data['best'] 	= cur_time if cur_time<prev_record else prev_record
#print("-"*15)
if accu_data.get('best') < prev_record:
	print("New best Record")
print("Current Record:",format(accu_data.get('best'),'.4f'),"sec")
with open('accuracy.json','w') as f:
	f.write(json.dumps(accu_data,separators=(",",":")))
accuracy_val = float(correct)/attempted
print("Accuracy: {}%".format(format(accuracy_val*100,'.3f')))
