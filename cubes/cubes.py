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

start = all_ranges.get('cubes').get('start')
end   = all_ranges.get('cubes').get('end')

lst = []
cur_data = {}

def practice():
	lst,cur_data = ranger.rangemaker("cub",start,end)
	accu_data = {}
	try:
		with open('accuracy.json','r') as f:
			accu_data = json.loads(f.read())
	except:
		print(colors.WARNING+"Please initialise first !!!"++colors.ENDC)
		sys.exit()
	inp = ""
	attempted = accu_data.get('Attempted')
	correct = accu_data.get('Correct')
	prev_record = accu_data.get('best')
	cur_time = prev_record
	sttime = time.time()
	#------------Range----------------------------
	num = random.choice(lst)#random.randint(start,end)
	#---------------------------------------------
	print("Cube of %d:"%num,end=" ")
	try:
		inp = input()
		userans = int(inp)
		correctans = math.pow(num,3)
		attempted+=1
		print("-"*15)
		if correctans==userans:
			print(colors.OKGREEN+"Correct !!!"+colors.ENDC)
			cur_time = time.time()-sttime
			print("Time taken:",format(cur_time,'.4f'),"sec")
			correct+=1
			del lst[lst.index(num)]
		else:		
			print(colors.FAIL+"Wrong !!!"+colors.ENDC)
			print("Correct ans is: %d"%correctans)
		print("-"*15)	

		incorrect = attempted-correct
		accu_data['Attempted'] 	= attempted
		accu_data['Correct'] 	= correct
		accu_data['Incorrect'] 	= incorrect
		accu_data['best'] 	= cur_time if cur_time<prev_record else prev_record
		if accu_data.get('best') < prev_record:
			print("New best Record")
		print("Current Record:",format(accu_data.get('best'),'.4f'),"sec")
		with open('accuracy.json','w') as f:
			f.write(json.dumps(accu_data,separators=(",",":")))
		accuracy_val = float(correct)/attempted
		print("Accuracy: {}%".format(format(accuracy_val*100,'.3f')))
		ranger.write_range("cub",lst,cur_data)
	except:
		if inp=="exit":
			sys.exit()
		else:
			print("Invalid Input !!!")
