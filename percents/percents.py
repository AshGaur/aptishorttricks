import random
import math
import time
import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join('..')))
import colors
import ranger
from edit_range import all_ranges

deno_start = all_ranges.get('percents').get('deno_start')
deno_end   = all_ranges.get('percents').get('deno_end')

lst = []
cur_data = {}

def practice():
	lst,cur_data = ranger.rangemaker("per",deno_start,deno_end)
	accu_data = {}
	try:
		with open('accuracy.json','r') as f:
			accu_data = json.loads(f.read())
	except:
		print(colors.WARNING+"Please initialise first !!!"+colors.ENDC)
		sys.exit()

	attempted = accu_data.get('Attempted')
	correct = accu_data.get('Correct')
	prev_record = accu_data.get('best')
	cur_time = prev_record
	sttime = time.time()
	#------------Range----------------------------
	num = 1
	deno = random.choice(lst)#random.randint(deno_start,deno_end)
	#---------------------------------------------
	print("%d/%d = "%(num,deno),end=" ")

	userans = input()
	if userans == "exit":
		sys.exit()
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
		print(colors.OKGREEN+"Correct !!!"+colors.ENDC)
		cur_time = time.time()-sttime
		print("Time taken:",format(cur_time,'.4f'),"sec")
		correct+=1
		del lst[lst.index(deno)]
	else:		
		print(colors.FAIL+"Wrong !!!"+colors.ENDC)
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
	ranger.write_range("per",lst,cur_data)
